from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from apis.twitter import TwitterAPI
from recommenders import tf_idf, test_data
from data_types import *

from collections import deque

twitter = TwitterAPI()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

default_system = {
    'nodes': [
        {'type': 'pool', 'data': [], 'data_type': TWITTER_POST},
        {
            'type': 'action',
            'function': {
                'name': 'twitter_author',
                'args': {'data': []}
            },
            'data': [],
            'data_type': TWITTER_USER
        },
        {
            'type': 'action',
            'function': {
                'name': 'timeline',
                'args': {'data': [], 'limit': 5}
            },
            'data': [],
            'data_type': TWITTER_POST
        },
        {
            'type': 'similarity',  # reduce similairty to action node
            'function': {
                'name': 'tf-idf',
                'args': {'data': []}
            },
            'data': [],
            'data_type': TWITTER_POST
        },
        {'type': 'pool', 'data': [], 'data_type': TWITTER_POST}
    ],
    'edges': {
        'to': [[1], [2], [3], [4]],
        'from': [[], [0], [1], [2], [3]]
    }
}

# class Node():
#     def __init__(self, type=None, data=[], function=None):
#         self.type = type
#         self.data = data
#         self.function = function  # function = {'name': '', 'args':{}}

#     def __str__(self):
#         node = {
#             'type': self.type,
#             'function': self.function,
#             'data': self.data
#         }
#         return str(node)


class Recommender():
    def __init__(self, system, data, ws=None):
        self.nodes = system['nodes']
        self.edges = system['edges']
        self.nodes[0]['data'] = data  # add orginal post to start pool
        self.websocket = ws

        # Graph
        self.twitter_users = {}
        self.twitter_posts = {}
        self.graph_nodes = []
        self.links = []

    async def run(self):
        to_edges = self.edges['to']
        from_edges = self.edges['from']
        # TODO: add type of post filter (twitter or reddit)
        for edge in to_edges:
            queue = deque(edge)  # Breadth first node execution
            while queue:
                index = queue.popleft()  # index of node from edge
                node = self.nodes[index]
                if 'function' in node:  # Action Node or Similarity Node
                    function = functions[node['function']['name']]

                    # get args to pass to function
                    args = node['function']['args']

                    # add seed posts for similairity calculations
                    if node['type'] == 'similarity':
                        args['seed_data'] = self.nodes[0]['data']

                    # get data from prev nodes and add to args
                    for i in from_edges[index]:
                        args['data'] += self.nodes[i]['data']
                    # execute function
                    # and update current node's data with response

                    res = function(**args)
                    self.nodes[index]['data'] = res

                    if self.websocket:
                        data = {
                            'type': node['data_type'],
                            'data': res
                        }
                        await self.send(data)
                        await self.send(self.graph(data))

                else:  # Pool Node
                    for i in from_edges[index]:
                        self.nodes[index]['data'] += self.nodes[i]['data']

        return self.nodes

    def graph(self, data):
        if data['type'] == TWITTER_POST:
            for post in data['data']:
                post_id = post['id']
                # add node
                if post_id not in self.twitter_posts:
                    self.twitter_posts[post_id] = len(self.graph_nodes)
                    self.graph_nodes.append({"name": post_id, "group": 1})

                # add links
                user_id = post['user']['id']
                if user_id in self.twitter_users:
                    posts = self.twitter_users[user_id]
                    for id in posts:
                        self.links.append({
                            "source": self.twitter_posts[id],
                            # "source": self.twitter_posts[posts[0]],
                            "target": self.twitter_posts[post_id],
                            "value": 1
                        })

                self.twitter_users.setdefault(user_id, [])
                self.twitter_users[user_id].append(post_id)

        return {
            'type': 'graph',
            'nodes': self.graph_nodes,
            'links': self.links
        }

    async def send(self, data):
        await self.websocket.send_json(data)

# @app.get("/")
# async def root():
#     return {"message": "hello world"}


def user_timeline(data=[], limit=20):
    posts = []
    for id in data:
        posts += twitter.user_timeline(id, limit)
    # posts = test_data
    return posts


def twitter_author(data=[]):
    return list({tweet['user']['id'] for tweet in data})
    # return []


functions = {
    # twitter
    'timeline': user_timeline,
    'twitter_author': twitter_author,
    # similarity
    'tf-idf': tf_idf
}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/timeline")
async def timeline(id):
    return twitter.user_timeline(id, 5)


@app.get("/post_data/")
async def post_data(url: str = ''):
    url = url.encode('iso-8859-1').decode('utf-8')
    if "twitter.com" in url:
        end = url.split('/')[-1]
        # url from share button adds '?s=20' at the end
        post_id = end.split('?')[0]
        return twitter.tweet_info(post_id)
    else:
        return {"error": "Invalid URL"}


@app.get("/recommendations/{recommender_id}")
async def recommendations(recommender_id):
    return {}

# Live Recommendations
@app.websocket("/recommendations/live/{recommender_id}")
async def live_recommendations(websocket: WebSocket, recommender_id: int):
    # recommendation system nodes and edges
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # if 'action' in data:
            if data:
                rec = Recommender(default_system, test_data[:2], websocket)
                nodes = await rec.run()
                await websocket.send_json(nodes)
                # await websocket.send_text(f"Message text was: {data}")

    except WebSocketDisconnect:
        print("Client has disconnected")


@app.websocket("/recommender/editor/{recommender_id}")
async def rec_editor(websocket: WebSocket, recommender_id: int):

    return {"item_id": item_id}
