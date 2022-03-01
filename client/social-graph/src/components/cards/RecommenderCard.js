import React, { useState } from "react";
import { CardTitle } from "./CardTitle";
import { FiPlus } from "react-icons/fi";
import "./Recommender.css";
import Editor from "../editor/Editor";

function RecommenderCard(props) {
    const [recommenders, setRecommenders] = useState(props.recommenders);
    const [selected, setSelected] = useState(0);
    const [show, setShow] = useState(false);

    const showEditor = () => { setShow(true) };
    const hideEditor = () => { setShow(false) };

    return (
        <div className="recommender-card">
            <div className="card-container">
                <div className="card-header">
                    <CardTitle title={"Recommender"} markerColor={"#B5E4CA"} />
                    {/* add recommender button */}
                    {/* <a href=""> */}
                    <FiPlus className="plus-icon" />
                    {/* </a> */}
                </div>

                <div className="card-body">
                    {/* <div className="dropdown-closed"></div> */}
                    <select name="recommenders" id="">
                        <option value="Default">Default</option>
                        <option value="Fast">Fast</option>
                        <option value="Sports">Sports</option>
                    </select>
                    <button className="edit-button" onClick={showEditor}>Edit</button>
                </div>
            </div>
            <Editor show={show} handleClose={hideEditor} />

        </div>
    );
}

export default RecommenderCard;

