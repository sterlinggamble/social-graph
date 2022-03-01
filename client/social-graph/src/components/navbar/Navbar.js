import React from "react";
import "./Navbar.css";
import { FaRedditAlien, FaTwitter } from "react-icons/fa";
import { FiEdit2, FiPlus } from "react-icons/fi";
import { MdPostAdd, MdGraphicEq } from "react-icons/md";
import { CgOptions } from "react-icons/cg";

// FaEdit, FaPlus, MdAddToPhotos, MdOutlineRecommend, MdOutlinePostAdd 

class Navbar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            graphs: []
        }
    }

    render() {
        return (
            <div className="navbar">
                <div className="items">
                    <div className="pfp">
                        {/* <img src="https://ui8-core.herokuapp.com/img/content/avatar.jpg" alt="" /> */}
                        <MdGraphicEq className='temp-logo' />
                    </div>
                    <div className="divider" />
                    <div className='graph-icons'>
                        <div className="graph-icon">
                            <FiPlus className='reddit-icon' />
                        </div>
                        <div className='graph-icon' style={{ backgroundColor: "#f7931a" }}></div>
                        <div className='graph-icon' style={{ backgroundColor: "#1f8ded" }}></div>
                        <div className='graph-icon' style={{ backgroundColor: "#ff7977" }}></div>
                    </div>
                    {/* <div className='divider' /> */}
                    {/* <div className='create-button' /> */}
                    <div className="divider" />
                    <div className="graph-icon">
                        <FiEdit2 className='reddit-icon' />
                    </div>
                    <div className="graph-icon">
                        <FaRedditAlien className='reddit-icon' />
                    </div>
                    <div className="graph-icon">
                        <FaTwitter className='twitter-icon' />
                    </div>
                    <div className="graph-icon">
                        <MdPostAdd className='reddit-icon' />
                    </div>
                    <div className="graph-icon">
                        <CgOptions className='reddit-icon' />
                    </div>

                </div>
            </div>
        );
    }
}

export default Navbar;