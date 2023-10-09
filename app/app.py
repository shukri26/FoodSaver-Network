from flask import Flask, request, jsonify
from models import db, User, FoodListing, FoodRequest
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/student/FoodSaver-Network/app/db/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify({'users': user_list})

@app.route('/food_listings', methods=['GET'])
def get_food_listings():
    food_listings = FoodListing.query.all()
    listing_list = [{'id': listing.id, 'fooditem': listing.fooditem, 'quantity': listing.quantity,
                     'donor_id': listing.donor_id} for listing in food_listings]
    return jsonify({'food_listings': listing_list})

@app.route('/food_listings', methods=['POST'])
def create_food_listing():
    data = request.json
    new_listing = FoodListing(fooditem=data['fooditem'], quantity=data['quantity'],
                               donor_id=data['donor_id'])
    db.session.add(new_listing)
    db.session.commit()
    return jsonify({'message': 'Food listing created successfully!'})

@app.route('/food_listings/<int:listing_id>', methods=['PATCH'])
def update_food_listing(listing_id):
    data = request.json
    listing = FoodListing.query.get(listing_id)
    if listing:
        if 'fooditem' in data:
            listing.fooditem = data['fooditem']
        if 'quantity' in data:
            listing.quantity = data['quantity']
        db.session.commit()
        return jsonify({'message': 'Food listing updated successfully!'})
    else:
        return jsonify({'message': 'Food listing not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
