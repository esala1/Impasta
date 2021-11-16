import './App.css';
import React from 'react';
import Restaurant from './components/Restaurant';
import MenuItem from './components/MenuItem';
import 'bootstrap/dist/css/bootstrap.min.css';
/* eslint-disable max-len */
/* eslint-disable no-unused-vars */
/* eslint-disable react/jsx-one-expression-per-line */

function App() {
  const args = (document.getElementById('data') == null) ? ({
    artist_ids: [],
    username: 'John',
    has_artists_saved: false,
  }) : JSON.parse(document.getElementById('data').text);
  let foodItems = [];
  let restaurants = [];
  if ('foodItems' in args) {
    foodItems = args.foodItems;
  }
  if ('restaurants' in args) {
    restaurants = args.restaurants;
  }

  if (args.page === 'homepage') {
    return (
      <div>
        <nav className="navbar navbar-light bg-light">
          <div style={{ marginLeft: '2%' }} className="navbar-brand">Impasta</div>
          <a href="/logout" style={{ marginRight: '2%' }}>
            <button type="button" className="btn btn-outline-dark">Logout</button>
          </a>
        </nav>
        <div className="title">Restaurants Near You</div>
        <div className="container">
          <div className="row">
            {restaurants.map((restaurantData) => <Restaurant restaurantData={restaurantData} />)}
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
        <a href="/logout" style={{ marginRight: '2%' }}>
          <button type="button" className="btn btn-outline-dark">Logout</button>
        </a>
      </nav>
      <div className="title">{restaurantName} Menu</div>
      <div className="container">
        <div className="row">
          {foodItems.map((item) => <MenuItem data={item} />)}
        </div>
      </div>
    </div>
  );
}

export default App;
