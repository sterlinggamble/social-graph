import React from "react";
import { CardTitle } from "./CardTitle";
import './NameCard.css';

class NameCard extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e) {
        const name = e.target.value;
        this.props.onChange(name);
    }

    render() {
        return (
            <div className="name-card">
                <div className="container">
                    <CardTitle title={"Name"} markerColor={'#B5E4CA'} />
                    <form action="">
                        <input type="text" placeholder="graph name" />
                    </form>
                </div>
            </div>
        );
    }
}


export default NameCard;
