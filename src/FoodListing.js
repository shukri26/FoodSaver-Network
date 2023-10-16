import React, { useState, useEffect } from 'react';
import './FoodListing.css'; // Import your CSS file

function FoodListing() {
  const [foodListings, setFoodListings] = useState([]);
  const [newFoodListing, setNewFoodListing] = useState({
    fooditem: '',
    quantity: '',
    donor_id: '', // Add donor_id to match your backend data model
  });
  
  const [newFoodRequest, setNewFoodRequest] = useState({
    food_types: '',
    quantity: '',
    delivery_time: '',
  });

  useEffect(() => {
    // Fetch food listings from the backend when the component mounts
    fetch('https://foodsaver.onrender.com/food_listings') // Replace with your backend URL
      .then((response) => response.json())
      .then((data) => {
        setFoodListings(data.food_listings);
      })
      .catch((error) => {
        console.error('An error occurred:', error);
      });
  }, []);

  const handleNewFoodListingChange = (e) => {
    const { name, value } = e.target;
    setNewFoodListing({ ...newFoodListing, [name]: value });
  };

  const handleNewFoodRequestChange = (e) => {
    const { name, value } = e.target;
    setNewFoodRequest({ ...newFoodRequest, [name]: value });
  };

  const handleSubmitNewFoodListing = (e) => {
    e.preventDefault();

    fetch('https://foodsaver.onrender.com/food_listings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newFoodListing),
    })
      .then((response) => {
        if (response.ok) {
          // Refresh the food listings after creating a new one
          fetch('https://foodsaver.onrender.com/food_listings')
            .then((response) => response.json())
            .then((data) => {
              setFoodListings(data.food_listings);
              setNewFoodListing({
                fooditem: '',
                quantity: '',
                donor_id: '', // Reset donor_id
              });
            });
        } else {
          console.error('Food listing creation failed');
        }
      })
      .catch((error) => {
        console.error('An error occurred:', error);
      });
  };

  const handleSubmitNewFoodRequest = (e) => {
    e.preventDefault();

    fetch('https://foodsaver.onrender.com/food_requests', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newFoodRequest),
    })
      .then((response) => {
        if (response.ok) {
          // Handle successful food request submission
          console.log('Food request submitted successfully!');
          // You can add logic to reset the form or show a success message here
        } else {
          console.error('Food request submission failed');
        }
      })
      .catch((error) => {
        console.error('An error occurred:', error);
      });
  };

  return (
    <div className="container">
      <div className="form-container">
        <form className="form" onSubmit={handleSubmitNewFoodListing}>
          <h2>Create New Food Listing</h2>
          <div className="form-group">
            <label htmlFor="fooditem">Food Item:</label>
            <input
              type="text"
              id="fooditem"
              name="fooditem"
              value={newFoodListing.fooditem}
              onChange={handleNewFoodListingChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="quantity">Quantity:</label>
            <input
              type="text"
              id="quantity"
              name="quantity"
              value={newFoodListing.quantity}
              onChange={handleNewFoodListingChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="donor_id">Donor ID:</label>
            <input
              type="text"
              id="donor_id"
              name="donor_id"
              value={newFoodListing.donor_id}
              onChange={handleNewFoodListingChange}
            />
          </div>
          <button type="submit">Create Food Listing</button>
        </form>
      </div>

      <div className="form-container">
        <form className="form" onSubmit={handleSubmitNewFoodRequest}>
          <h2>Create New Food Request</h2>
          <div className="form-group">
            <label htmlFor="food_types">Food Types:</label>
            <input
              type="text"
              id="food_types"
              name="food_types"
              value={newFoodRequest.food_types}
              onChange={handleNewFoodRequestChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="quantity">Quantity:</label>
            <input
              type="text"
              id="quantity"
              name="quantity"
              value={newFoodRequest.quantity}
              onChange={handleNewFoodRequestChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="delivery_time">Delivery Time:</label>
            <input
              type="text"
              id="delivery_time"
              name="delivery_time"
              value={newFoodRequest.delivery_time}
              onChange={handleNewFoodRequestChange}
            />
          </div>
          <button type="submit">Create Food Request</button>
        </form>
      </div>

      <h2>Food Listings</h2>
      <ul className="food-listings">
        {foodListings.map((listing) => (
          <li key={listing.id} className="food-listing">
            Food Item: {listing.fooditem}, Quantity: {listing.quantity}, Donor ID: {listing.donor_id}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default FoodListing;