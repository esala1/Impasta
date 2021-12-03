import './App.css';
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import Restaurant from './components/Restaurant';
import 'bootstrap/dist/css/bootstrap.min.css';

/* eslint-disable react/prop-types */
/* eslint-disable no-unused-vars */
/* eslint-disable no-multiple-empty-lines */
/* eslint-disable no-multi-spaces */
/* eslint-disable max-len */
/* eslint-disable no-trailing-spaces */
/* eslint-disable prefer-template */
/* eslint-disable quotes */
/* eslint-disable react/jsx-indent-props */
/* eslint-disable object-curly-spacing */
/* eslint-disable quote-props */
/* eslint-disable prefer-const */
/* eslint-disable indent */
/* eslint-disable object-shorthand */
/* eslint-disable react/jsx-indent */
/* eslint-disable no-multi-assign */
/* eslint-disable block-spacing */
/* eslint-disable no-lone-blocks */
/* eslint-disable no-return-assign */
/* eslint-disable implicit-arrow-linebreak */
/* eslint-disable no-extra-semi */
/* eslint-disable space-before-blocks */
/* eslint-disable no-const-assign */
/* eslint-disable no-unused-expressions */
/* eslint-disable keyword-spacing */
/* eslint-disable no-use-before-define */
/* eslint-disable no-plusplus */
/* eslint-disable no-loop-func */
/* eslint-disable space-infix-ops */
/* eslint-disable semi */


function App() {
  const args = (document.getElementById('data') == null) ? ({
    artist_ids: [],
    username: 'Gyandeep',
    page: 'homepage',
    restaurants: [
      {
        res_photo: 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photo_reference=Aap_uEBs72iKIpmXmMEHi3ZNMNAFMPVsFQPLZdX1tWspY1ilGfolgTb8DsCMYO0NwyvuP-V3tjbicfMpkYhK_gXmgFNJ8NLzp67BfHTcayW1uPA0rMd3uot7HPFhziPPyXn_NPZv9pi64-CR1YsUlVzuWXnkqid4sgjdZDPZshHw4jnYcMfR&key=AIzaSyCtYqvgeuX6zKfIZsguSp8ctQ9IKSRBN7I',
        res_name: 'Hyatt Regency Atlanta',
        res_address: '265 Peachtree St NE, Atlanta, GA 30303, USA',
        res_rating: '4.3',
        res_user_rating: '8375',
      },
      {
        res_photo: 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photo_reference=Aap_uECD8mGsRCLkCf5T7aooUd3w_pUrG8485tegCQIdUSYIDLpUhtwJben2qvA57qPqRCvFlsSvwkGZn793fq0QntquNGLkG9SUl9HEB-_RRUMGiJaTAm8ECR7S9LQR5q4de1ywMijHFNFtebPzcp51Qfgbi0tXNaY_9jHnDZwos-Nd89yN&key=AIzaSyCtYqvgeuX6zKfIZsguSp8ctQ9IKSRBN7I',
        res_name: 'STATS Brewpub',
        res_address: '300 Marietta St NW Suite 101, Atlanta, GA 30313, USA',
        res_rating: '4.1',
        res_user_rating: '854',
      },
      {
        res_photo: 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photo_reference=Aap_uEAdwcg69Dd2xs_eN-hEk4ca4Hfw1Y46iqXjLUHijX702kbtmAnAXBXQA4vd0-VegEf1PBRnZMZYzCuqfR95fBpwHSrJI9SwZjccJIezpui4wHQsbjqtp9QHdOK0Pw3SrQDy3EdV2gk3IyFHzzo43eCBYr_GAPsWCUAzkWRhxqOB8iIJ&key=AIzaSyCtYqvgeuX6zKfIZsguSp8ctQ9IKSRBN7I',
        res_name: 'Hard Rock Cafe',
        res_address: '215 Peachtree St NE, Atlanta, GA 30303, USA',
        res_rating: '4.1',
        res_user_rating: '4962',
      },
    ],
  }) : JSON.parse(document.getElementById('data').text);
  const [searchInput, setSearchInput] = useState();
  const [searchRestaurants, setSearchRestaurants] = useState([]);
  let foodItems = [];
  let restaurants = [];
  const [favoriteFoods, setfavoriteFoods]  = useState([]);
  const [favoriteButtons, setFavoriteButtons] = useState([]);

  if ('foodItems' in args) {
    foodItems = args.foodItems;
  }
  if (searchRestaurants.length !== 0) {
    restaurants = searchRestaurants;
  } else if ('restaurants' in args) {
    restaurants = args.restaurants;
  }

  function onButtonSearch(e) {
    e.preventDefault();
    console.log(JSON.stringify({ search_input: searchInput }));
    fetch('/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ search_input: searchInput }),
    }).then((response) => response.json())
      .then((data) => {
        console.log(data)
        setSearchRestaurants(data.search_restaurant_list);
      });
  }

  function onClickSave() {
    let requestData = { favoriteFoods: favoriteFoods };
    fetch('/save', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    })
      .then((response) => response.json())
      .then((data) => {
        window.location.replace("/favorite-foods");
      });
  }

  function onClickAdd(i) {
    const updatedFavoriteButtons = [...favoriteButtons, i];
    setFavoriteButtons(updatedFavoriteButtons);    
    const updatedFoods = [...favoriteFoods, foodItems[i]];
    setfavoriteFoods(updatedFoods);
  }

  function onClickDelete(i) {
    const index = favoriteButtons.indexOf(i);
    if (index > -1) {
      const updatedFavoriteButtons = [...favoriteButtons.slice(0, index), ...favoriteButtons.slice(index+1)];
      setFavoriteButtons(updatedFavoriteButtons);
    }
    const updatedFoods = [...favoriteFoods.slice(0, i), ...favoriteFoods.slice(i + 1)];
    setfavoriteFoods(updatedFoods);
  }

  function MenuItem({
    name, price, description, nutrition, i,
  }) {
    return (
      <div className="col-4 alignLeft">
        <div className="title1">{name}</div>
        <div>{`Price: ${price}`}</div>
        <div>{`Description: ${description}`}</div>
        <div>{`Nutrition: ${nutrition}`}</div>
        {favoriteButtons.includes(i) ? (
          <button type="button" className="btn btn-danger" onClick={() => onClickDelete(i)}>Delete from Favorites</button>
        ): (
          <button type="button" className="btn btn-primary" onClick={() => onClickAdd(i)}>Add to Favorites</button>
        )}
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

  if (args.page === 'homepage') {
    const restaurantList = restaurants.map((restaurantData, idx) => (
      <Restaurant
        restaurantData={restaurantData}
      />
    ));
    
    return (
      <div>
        <nav className="navbar navbar-light bg-light">
          <div style={{ marginLeft: '2%' }} className="navbar-brand">Impasta</div>
          <form onSubmit={onButtonSearch}>
            <input type="text" onChange={(e) => setSearchInput(e.target.value)} value={searchInput} />
            <button type="submit">Search</button>
          </form>
          <a href="/favorite-foods" style={{ marginLeft: '72%' }}>
            <button type="button" className="btn btn-outline-dark">Favorite Foods</button>
          </a>
          <a href="/logout">
            <button type="button" className="btn btn-outline-dark">Logout</button>
          </a>
        </nav>
        <div className="title">Restaurants Near You</div>
        <div className="container">
          <div className="row">
            {restaurantList}
          </div>
          <br />
        </div>
      </div>
    );
  }
  const restaurantName = args.restaurant_name;
  return (
    <div>
      <nav className="navbar navbar-light bg-light">
        <div style={{ marginLeft: '2%' }} className="navbar-brand">Impasta</div>
        <a href="/favorite-foods" style={{ marginLeft: '72%' }}>
          <button type="button" className="btn btn-outline-dark">Favorite Foods</button>
        </a>
        <a href="/logout" style={{ marginRight: '2%' }}>
          <button type="button" className="btn btn-outline-dark">Logout</button>
        </a>
      </nav>
      <div className="title">{`${restaurantName} Menu`}</div>
      <button type="button" className="btn btn-success" onClick={onClickSave}>Save All</button>
      <div className="container">
        <div className="row">
          {foodItems.map((item, idx) => 
          (
            <MenuItem
              name={item.name}
              price={item.price}
              description={item.description}
              nutrition={item.nutrition}
              i={idx}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
