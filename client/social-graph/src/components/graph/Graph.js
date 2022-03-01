import React, { useState, useEffect, useRef } from "react";
import NameCard from "../cards/NameCard";
import AddPostCard from "../cards/AddPostCard";
import PostsCard from "../cards/PostsCard";
import RecommenderCard from "../cards/RecommenderCard";
import ForceLayout from "./ForceGraph";
import Footer from "./Footer";
import './Graph.css'

function Graph(props) {
    const [title, setTitle] = useState(props.title);
    const [editMode, setEditMode] = useState(false);
    const [tweets, setTweets] = useState([]);
    const [nodes, setNodes] = useState([]);
    const [links, setLinks] = useState([]);

    const addTweet = tweet => setTweets([...tweets, tweet]);

    const ws = useRef(null);

    useEffect(() => {
        ws.current = new WebSocket("ws://localhost:8000/recommendations/live/0");

        const apiCall = { event: "open connection" };

        ws.current.onopen = (event) => {
            ws.current.send(JSON.stringify(apiCall));
        }

        ws.current.onmessage = (event) => {
            const json = JSON.parse(event.data);
            console.log('Message from server ', json);

            if (json.type === "twitter_post") {
                for (const post of json.data) {
                    setTweets(prev => [...prev, post]);
                }
            } else if (json.type === "graph") {
                setNodes(prev => [...prev, ...json.nodes]);
                setLinks(prev => [...prev, ...json.links]);
            }
        }
    }, []);

    let footer;
    let cardsHeight = '100vh';

    if (editMode) {
        footer = <Footer />;
        cardsHeight = 'calc(100vh - 80px)';
    }

    return (
        <div style={{ height: '100vh', position: 'relative', width: 'calc(100% - 80px)', left: '80px' }}>
            <div className="graph">
                <div className="graph-container">
                    <h1 className="title">{title}</h1>
                    {/* <ForceDirected /> */}
                    <ForceLayout width={950} height={710} nodes={nodes} links={links} />
                </div>
                <div className="cards" style={{ height: cardsHeight }}>
                    <NameCard />
                    <AddPostCard addTweet={addTweet} />
                    <PostsCard title={"Twitter Posts"} markerColor={'#b1e5fc'} posts={tweets} type={"twitter"} />
                    <PostsCard title={"Reddit Posts"} markerColor={'#ffad96'} posts={[]} />
                    <RecommenderCard />
                </div>
            </div>
            {footer}
        </div>

    );
}

export default Graph;