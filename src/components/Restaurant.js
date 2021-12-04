import React from 'react';
import PropTypes from 'prop-types';

export default function Restaurant({
  resName, resPhoto, resAddress, resRating, resUserRating,
}) {
  return (
    <div className="col-4 alignCenter">
      <br />
      <div className="name">{resName}</div>
      <img src={resPhoto} width="150" height="200" alt={resName} className="img1" />
      <div className="center">{resAddress}</div>
      <div className="center">{`Rating: ${resRating}`}</div>
      <div className="center">{`Total Ratings: ${resUserRating}`}</div>
      <a href={`/menu/ + ${resName} + / + ${resAddress}`}>
        <button type="button" className="btn btn-outline-dark">View Menu</button>
      </a>
    </div>
  );
}

Restaurant.defaultProps = {
  resName: 'Hyatt Regency Atlanta',
  resPhoto: 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photo_reference=Aap_uEBs72iKIpmXmMEHi3ZNMNAFMPVsFQPLZdX1tWspY1ilGfolgTb8DsCMYO0NwyvuP-V3tjbicfMpkYhK_gXmgFNJ8NLzp67BfHTcayW1uPA0rMd3uot7HPFhziPPyXn_NPZv9pi64-CR1YsUlVzuWXnkqid4sgjdZDPZshHw4jnYcMfR&key=AIzaSyCtYqvgeuX6zKfIZsguSp8ctQ9IKSRBN7I',
  resAddress: '265 Peachtree St NE, Atlanta, GA 30303, USA',
  resRating: '4.3',
  resUserRating: '8375',
};

Restaurant.propTypes = {
  resName: PropTypes.string,
  resPhoto: PropTypes.string,
  resAddress: PropTypes.string,
  resRating: PropTypes.string,
  resUserRating: PropTypes.string,
};
