import React from 'react';
/* eslint-disable react/prop-types */
/* eslint-disable react/jsx-one-expression-per-line */
/* eslint-disable prefer-template */
/* eslint-disable react/destructuring-assignment */
/* eslint-disable react/jsx-indent */
/* eslint-disable indent */
/* eslint-disable jsx-a11y/alt-text */

export default function Restaurant(props) {
    return (
        <div className="col-4 alignLeft">
            <br />
            <img src={props.restaurantData.res_photo} width="150" height="200" alt={props.restaurantData.res_name} />
            <div>Name: {props.restaurantData.res_name}</div>
            <div>Address: {props.restaurantData.res_address}</div>
            <div>Rating: {props.restaurantData.res_rating}</div>
            <div>Total Ratings: {props.restaurantData.res_user_rating}</div>
            <a href={'/menu/' + props.restaurantData.res_name + '/' + props.restaurantData.res_address}>
                <button type="button" className="btn btn-outline-dark">View Menu</button>
            </a>
        </div>
    );
}
