import React, { useState } from 'react';
import { CardTitle } from "./CardTitle";
import './AddPostCard.css';

function AddPostCard(props) {
    const { addTweet } = props;
    const [url, setUrl] = useState("");

    const handleSubmit = event => {
        event.preventDefault();
        fetch(`http://127.0.0.1:8000/post_data/?url=${encodeURIComponent(url)}`)
            .then(response => response.json())
            .then(data => addTweet(data))
            .catch(error => console.log('error = ' + error));
    };

    const handleChange = event => {
        setUrl(event.target.value);
    };

    return (
        <div className="add-post-card">
            <div className="container">
                <CardTitle title={"Add Post"} markerColor={'#CAB9FF'} />
                <form onSubmit={evt => handleSubmit(evt)}>
                    <input type="text" placeholder="post url" value={url} onChange={evt => handleChange(evt)} />
                    <input type="submit" value="Submit" style={{ display: "none" }} />
                </form>
            </div>
        </div>
    );
}

export default AddPostCard;