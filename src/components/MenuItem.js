import React from 'react';
import PropTypes from 'prop-types';

/* eslint-disable react/prop-types */

export default function MenuItem({
  name, price, description, nutrition, onClick,
}) {
  return (
    <div className="col-4 alignLeft">
      <div className="title1">{name}</div>
      <div>{`Price: ${price}`}</div>
      <div>{`Description: ${description}`}</div>
      <div>{`Nutrition: ${nutrition}`}</div>
      <button type="button" onClick={onClick}>Add to Fav</button>
      <br />
    </div>
  );
}

MenuItem.defaultProps = {
  name: 'Gyan',
  price: '$20',
  description: 'this is the description',
  nutrition: 'Calories: 100, Total Fat: 10, Serving Size: 5',
};

MenuItem.propTypes = {
  name: PropTypes.string,
  price: PropTypes.string,
  description: PropTypes.string,
  nutrition: PropTypes.string,
};
