import './App.css';
import React from 'react';
/* eslint-disable max-len */
/* eslint-disable no-unused-vars */
/* eslint-disable react/jsx-one-expression-per-line */
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const args = (document.getElementById('data') == null) ? ({
    restaurants: [],
  }) : JSON.parse(document.getElementById('data').text);
  return (
    <div>
      <nav className="navbar navbar-light bg-light">
        <div style={{ marginLeft: '2%' }} className="navbar-brand">Impasta</div>
        <a href="/logout" style={{ marginRight: '2%' }}>
          <button type="button" className="btn btn-outline-dark">Logout</button>
        </a>
      </nav>
    </div>
  );
}

export default App;
