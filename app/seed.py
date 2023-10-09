from app import app, db, User, FoodListing, FoodRequest


with app.app_context():
    
    user1 = User(username='user1', email='user1@example.com')
    user2 = User(username='user2', email='user2@example.com')
    db.session.add_all([user1, user2])
    db.session.commit()

    
    food_listing1 = FoodListing(fooditem='Apples', quantity=10, donor=user1)
    food_listing2 = FoodListing(fooditem='Bananas', quantity=20, donor=user1)
    food_listing3 = FoodListing(fooditem='Oranges', quantity=15, donor=user2)
    db.session.add_all([food_listing1, food_listing2, food_listing3])
    db.session.commit()

    
    food_request1 = FoodRequest(food_types='Apples', quantity=5, requester=user2)
    food_request2 = FoodRequest(food_types='Bananas', quantity=10, requester=user2)
    db.session.add_all([food_request1, food_request2])
    db.session.commit()

print("Data has been seeded successfully!")


