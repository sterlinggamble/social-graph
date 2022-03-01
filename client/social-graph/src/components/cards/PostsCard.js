import React from "react";
import { CardTitle } from "./CardTitle";
import "./PostsCard.css";
import Post from "./Post";

function PostsCard(props) {
    const { title, markerColor, posts, type } = props;

    let postCards = posts.map((post) => <Post post={post} type={type} />);

    return (
        <div className="posts-card">
            <div className="container">
                <CardTitle title={title} markerColor={markerColor} />
                <div className="posts">
                    {postCards}
                </div>
            </div>

        </div>
    );
}

export default PostsCard;