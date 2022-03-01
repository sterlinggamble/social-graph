import React from 'react';

export const CardTitle = props => {
    const markerStyle = {
        backgroundColor: props.markerColor,
        height: '29px',
        width: '15px',
        borderRadius: '3px',
        marginRight: '10px'
    };

    const titleStyle = {
        fontWeight: 'bold',
        fontSize: '20px',
        margin: '0',
    }

    return (
        <div style={{ marginBottom: '18px', display: 'flex', alignItems: 'center' }}>
            <div className="marker" style={markerStyle}></div>
            <p style={titleStyle}>{props.title}</p>
        </div>
    );
}