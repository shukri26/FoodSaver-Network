import React, { useState, useEffect } from 'react';

function FoodListing() {
  const [foodListings, setFoodListings] = useState([]);
  const [newFoodListing, setNewFoodListing] = useState({
    fooditem: '',
    quantity: '',
    expiry: '',
    pickup_location: '',
  });

  useEffect(() => {
    // Fetch food listings from the backend when the component mounts
    fetch('YOUR_API_ENDPOINT_HERE')
      .then((response) => response.json())
      .then((data) => {
        setFoodListings(data.foodListings); // Assuming your API returns a list of food listings
      })
      .catch((error) => {
        console.error('An error occurred:', error);
      });
  }, []);

  // Function to handle input changes for the new food listing
  const handleNewFoodListingChange = (e) => {
    const { name, value } = e.target;
    setNewFoodListing({ ...newFoodListing, [name]: value });
  };

  // Function to submit a new food listing
  const handleSubmitNewFoodListing = (e) => {
    e.preventDefault();

    // Send the new food listing data to the backend (POST request)
    fetch('YOUR_API_ENDPOINT_HERE', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newFoodListing),
    })
      .then((response) => {
        if (response.ok) {
          // Refresh the food listings after creating a new one
          // You can also add a new food listing to the existing list without a refresh
          fetch('YOUR_API_ENDPOINT_HERE')
            .then((response) => response.json())
            .then((data) => {
              setFoodListings(data.foodListings);
              setNewFoodListing({
                fooditem: '',
                quantity: '',
                expiry: '',
                pickup_location: '',
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

  return (
    <div>
      <h2>Food Listings</h2>
      <ul>
        {foodListings.map((listing) => (
          <li key={listing.id}>
            Food Item: {listing.fooditem}, Quantity: {listing.quantity}
          </li>
        ))}
      </ul>
      <h2>Create New Food Listing</h2>
      <form onSubmit={handleSubmitNewFoodListing}>
        <div>
          <label htmlFor="fooditem">Food Item:</label>
          <input
            type="text"
            id="fooditem"
            name="fooditem"
            value={newFoodListing.fooditem}
            onChange={handleNewFoodListingChange}
          />
        </div>
        <div>
          <label htmlFor="quantity">Quantity:</label>
          <input
            type="text"
            id="quantity"
            name="quantity"
            value={newFoodListing.quantity}
            onChange={handleNewFoodListingChange}
          />
        </div>
        <div>
          <label htmlFor="expiry">Expiry:</label>
          <input
            type="text"
            id="expiry"
            name="expiry"
            value={newFoodListing.expiry}
            onChange={handleNewFoodListingChange}
          />
        </div>
        <div>
          <label htmlFor="pickup_location">Pickup Location:</label>
          <input
            type="text"
            id="pickup_location"
            name="pickup_location"
            value={newFoodListing.pickup_location}
            onChange={handleNewFoodListingChange}
          />
        </div>
        <button type="submit">Create Food Listing</button>
      </form>
    </div>
  );
}

export default FoodListing;