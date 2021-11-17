import React from 'react';
/* eslint-disable react/prop-types */

export default function Restaurant({
  restaurantData,
}) {
  return (
    <div className="col-4 alignCenter">
      <br />
      <div className="name">{restaurantData.res_name}</div>
      <img src={restaurantData.res_photo} width="150" height="200" alt={restaurantData.res_name} className="img1" />
      <div className="center">{restaurantData.res_address}</div>
      <div className="center">{`Rating: ${restaurantData.res_rating}`}</div>
      <div className="center">{`Total Ratings: ${restaurantData.res_user_rating}`}</div>
      <a href={`/menu/ + ${restaurantData.res_name} + / + ${restaurantData.res_address}`}>
        <button type="button" className="btn btn-outline-dark">View Menu</button>
      </a>
    </div>
  );
}
