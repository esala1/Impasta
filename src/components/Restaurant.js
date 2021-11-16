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
        <div className="col-4 alignCenter">
            <br />
            <div className="name">{props.restaurantData.res_name}</div>
            <img src={props.restaurantData.res_photo} width="150" height="200" alt={props.restaurantData.res_name} className="img1" />
            <div className="center">{props.restaurantData.res_address}</div>
            <div className="center">Rating: {props.restaurantData.res_rating}</div>
            <div className="center">Total Ratings: {props.restaurantData.res_user_rating}</div>
            <a href={'/menu/' + props.restaurantData.res_name + '/' + props.restaurantData.res_address}>
                <button type="button" className="btn btn-outline-dark">View Menu</button>
            </a>
        </div>
    );
}
