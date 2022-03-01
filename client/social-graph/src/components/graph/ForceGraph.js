import React, { useState, useEffect, useRef } from "react";
import * as d3 from "d3";
import { data } from "./TestData"

function ForceLayout(props) {
    const { width, height, nodes, links } = props;

    const mountPoint = useRef(null);

    useEffect(() => {
        console.log("component updated", nodes);
        const force = d3.layout.force()
            .charge(-120)
            // .linkDistance(50)
            .size([width, height])
            .nodes(nodes)
            .links(links);

        const svg = d3.select(mountPoint.current)
        // .append('svg')
        // .attr('width', width)
        // .attr('height', height);

        svg.selectAll("*").remove();

        const link = svg.selectAll('line')
            .data(links)
            .enter()
            .append('line')
            // .join('line')
            .style('stroke', '#999999')
            .style('stroke-opacity', '0.6')
            .style('stroke-width', (d) => Math.sqrt(d.value));

        const color = d3.scale.category20();
        const node = svg.selectAll('circle')
            .data(nodes)
            .enter()
            .append('circle')
            // .join('circle')
            .attr('r', 5)
            .style('stroke', '#f4f4f4') // node border color
            .style('stroke-width', 1.5)
            .style('fill', (d) => color(d.group)) // each node color-coded by group
            .call(force.drag);

        force.on('tick', () => {
            link
                .attr('x1', (d) => d.source.x)
                .attr('y1', (d) => d.source.y)
                .attr('x2', (d) => d.target.x)
                .attr('y2', (d) => d.target.y);

            node
                .attr('cx', (d) => d.x)
                .attr('cy', (d) => d.y);
        });

        force.start();

    }, [nodes, links, width, height]);

    const style = {
        width,
        height,
        // border: '1px solid #323232'
        margin: '0 auto'
    }

    return <svg className="svg-canvas" style={style} ref={mountPoint} />;
}


export default ForceLayout;