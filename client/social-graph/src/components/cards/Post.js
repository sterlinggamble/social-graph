import React, { useState } from "react";
import "./Post.css"


function Post(props) {
    const { post, type } = props;
    const [saved, setSaved] = useState(null);

    let name1, name2, text, profilePic;
    if (type === "twitter") {
        name1 = post.user.name;
        name2 = post.user.screen_name
        text = post.text
        profilePic = post.user.profile_image_url
    }

    return (
        <div className="post">
            <div className="post-container">
                <div className="profile-pic">
                    {profilePic && <img src={profilePic} className="search-image" />}
                </div>
                <div className="right-container">
                    <div className="names">
                        <p className="name-1">{name1}</p>
                        <p className="name-2">@{name2}</p>
                    </div>
                    <div className="content">
                        <p>{text}</p>
                    </div>
                </div>
            </div>
        </div>
    );

}

export default Post;