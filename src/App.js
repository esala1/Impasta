import './App.css';
import React from 'react';
import Restaurant from './components/Restaurant';
import MenuItem from './components/MenuItem';
import 'bootstrap/dist/css/bootstrap.min.css';

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
            {restaurants.map((restaurantData) => (
              <Restaurant
                res_name={restaurantData.res_name}
                res_photo={restaurantData.res_photo}
                res_address={restaurantData.res_address}
                res_rating={restaurantData.res_rating}
                res_user_rating={restaurantData.res_user_rating}
              />
            ))}
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
      <div className="title">{`${restaurantName} Menu`}</div>
      <div className="container">
        <div className="row">
          {foodItems.map((item) => (
            <MenuItem
              name={item.name}
              price={item.price}
              description={item.description}
              nutrition={item.nutrition}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
