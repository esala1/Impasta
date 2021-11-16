import React from 'react';
/* eslint-disable react/prop-types */
/* eslint-disable react/jsx-one-expression-per-line */
/* eslint-disable prefer-template */
/* eslint-disable react/destructuring-assignment */
/* eslint-disable react/jsx-indent */
/* eslint-disable indent */
/* eslint-disable jsx-a11y/alt-text */

export default function MenuItem(props) {
    return (
        <div className="col-4 alignLeft">
            <div>Name: {props.data.name}</div>
            <div>Price: {props.data.price}</div>
            <div>Description: {props.data.description}</div>
            <div>Nutrition: {props.data.nutrition}</div>
            <br />
        </div>
    );
}
