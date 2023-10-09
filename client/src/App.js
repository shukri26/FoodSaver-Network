// App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './LoginPage';
import FoodListing from './FoodListing';
import './App.css'

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/foodlisting" element={<FoodListing />} />
          {/* Add your other routes here */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;