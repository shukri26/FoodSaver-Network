from app import app, db, User, FoodListing, FoodRequest

# Create an application context
with app.app_context():
    # Create the database tables
    db.create_all()

    # Create and add user data with unique email addresses
    user1 = User(username='user1', email='user1@example.com')
    user2 = User(username='user2', email='user2@example.com')
    
    # Check if the users with these email addresses already exist
    existing_user1 = User.query.filter_by(email=user1.email).first()
    existing_user2 = User.query.filter_by(email=user2.email).first()
    
    if not existing_user1:
        db.session.add(user1)
    
    if not existing_user2:
        db.session.add(user2)
    
    db.session.commit()

    # Create and add food listing data
    food_listing1 = FoodListing(
        donor=user1,
        fooditem='Apples',
        quantity=10,
        expiry='2023-12-31',
        pickup_location='Location 1'
    )
    food_listing2 = FoodListing(
        donor=user2,
        fooditem='Bananas',
        quantity=15,
        expiry='2023-12-31',
        pickup_location='Location 2'
    )

    db.session.add(food_listing1)
    db.session.add(food_listing2)
    db.session.commit()

    # Create and add food request data
    food_request1 = FoodRequest(
        requester=user1,
        food_types='Oranges',
        quantity=5,
        delivery_time='2023-12-31',
    )
    food_request2 = FoodRequest(
        requester=user2,
        food_types='Grapes',
        quantity=8,
        delivery_time='2023-12-31',
    )

    db.session.add(food_request1)
    db.session.add(food_request2)
    db.session.commit()