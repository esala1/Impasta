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
  resName: 'Hard Rock Cafe',
  resPhoto: 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photo_reference=Aap_uEAdwcg69Dd2xs_eN-hEk4ca4Hfw1Y46iqXjLUHijX702kbtmAnAXBXQA4vd0-VegEf1PBRnZMZYzCuqfR95fBpwHSrJI9SwZjccJIezpui4wHQsbjqtp9QHdOK0Pw3SrQDy3EdV2gk3IyFHzzo43eCBYr_GAPsWCUAzkWRhxqOB8iIJ&key=AIzaSyCtYqvgeuX6zKfIZsguSp8ctQ9IKSRBN7I',
  resAddress: '215 Peachtree St NE, Atlanta, GA 30303, USA',
  resRating: '4.1',
  resUserRating: '4962',
};

Restaurant.propTypes = {
  resName: PropTypes.string,
  resPhoto: PropTypes.string,
  resAddress: PropTypes.string,
  resRating: PropTypes.string,
  resUserRating: PropTypes.string,
};
