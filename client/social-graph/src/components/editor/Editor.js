import React, { useState } from "react";
import "./Editor.css";
import { BiSkipPrevious, BiPlay, BiSkipNext, BiPause } from "react-icons/bi";
import ReactFlow, { removeElements, addEdge, Background, Controls } from 'react-flow-renderer';

const initialElements = [
    {
        id: '1',
        type: 'input', // input node
        data: { label: 'Input Node' },
        position: { x: 250, y: 25 },
    },
    // default node
    {
        id: '2',
        // you can also pass a React component as a label
        data: { label: <div>Default Node</div> },
        position: { x: 100, y: 125 },
    },
    {
        id: '3',
        type: 'output', // output node
        data: { label: 'Output Node' },
        position: { x: 250, y: 250 },
    },
    // animated edge
    { id: 'e1-2', source: '1', target: '2', animated: true },
    { id: 'e2-3', source: '2', target: '3' },
];

// const initialElements = [
//     {
//         id: '1',
//         type: 'input',
//         data: { label: 'Input Node' },
//         position: { x: 250, y: 25 },
//     },
//     {
//         id: '2',
//         data: { label: 'Another Node' },
//         position: { x: 100, y: 125 },
//     },
// ];

function NodeMenu(props) {
    const [node, setNode] = useState(null);

    const markerStyle = {
        backgroundColor: "#CAB9FF",
        height: '29px',
        width: '15px',
        borderRadius: '3px',
        marginRight: '10px'
    };

    return (
        <div className="node-menu">
            <div className="node-menu-container">
                <div className="node-title">
                    <div className="node-marker" style={markerStyle}></div>
                    <select name="nodes" id="" >
                        <option value="Actions">Actions</option>
                        <option value="Pools">Pools</option>
                        <option value="Similarity">Similarity</option>
                    </select>
                </div>
                <div className="node-type">
                    <select name="nodes" id="" >
                        <option value="Get Timeline">Get Timeline</option>
                        <option value="Get Favorites">Get Favorites</option>
                    </select>
                    <button className="edit-button">Add</button>
                </div>
            </div>
        </div>
    );
}

function Editor(props) {
    const [play, setPlay] = useState(true);
    const [elements, setElements] = useState(initialElements);
    const onElementsRemove = (elementsToRemove) => {
        setElements((els) => removeElements(elementsToRemove, els));
    };

    const onConnect = (params) => setElements((els) => addEdge(params, els));

    const { handleClose, show } = props;

    const showHideClassName = show ? "editor display-block" : "editor display-none";

    // Recommender Testing Controls
    const playButton = <BiPlay className="control-button" onClick={() => setPlay(!play)} />;
    const pauseButton = <BiPause className="control-button" onClick={() => setPlay(!play)} />;

    const testButton = play ? playButton : pauseButton;

    return (
        <div className={showHideClassName}>
            <div className="editor-main">
                <nav>
                    <div className="nav-container">
                        <select name="recommender" id="">
                            <option value="Default">Default</option>
                            <option value="Fast">Fast</option>
                            <option value="Sports">Sports</option>
                        </select>
                        <div className="controls">
                            <BiSkipPrevious className="control-button" />
                            {testButton}
                            <BiSkipNext className="control-button" />
                        </div>
                        <div className="nav-buttons">
                            <button className="cancel-button" onClick={handleClose}>Cancel</button>
                            <button className="save-button">Save</button>
                        </div>
                    </div>
                </nav>
                <div className="editor-body">
                    <div className="editor-cards">
                        <NodeMenu />
                    </div>

                    <div className="nodes">
                        <ReactFlow
                            elements={elements}
                            onElementsRemove={onElementsRemove}
                            onConnect={onConnect}
                            deleteKeyCode={8} /* 'delete'-key */
                        >
                            <Controls />
                            <Background color="#aaa" gap={16} />
                        </ReactFlow>
                    </div>
                </div>
            </div>

        </div>
    );
}

export default Editor;