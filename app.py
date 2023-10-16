from flask import Flask, request, jsonify
from models import db, User, FoodListing, FoodRequest
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
import os

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)

with app.app_context():
    db.create_all()

class FoodListingForm(FlaskForm):
    fooditem = StringField('Food Item', validators=[DataRequired(), Length(min=1, max=255)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])

class FoodRequestForm(FlaskForm):
    fooditem = StringField('Food Item', validators=[DataRequired(), Length(min=1, max=255)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    requester_id = IntegerField('Requester ID', validators=[DataRequired(), NumberRange(min=1)])

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

@app.route('/food_requests', methods=['GET'])
def get_food_requests():
    food_requests = FoodRequest.query.all()
    request_list = [{'id': request.id, 'fooditem': request.fooditem, 'quantity': request.quantity,
                     'requester_id': request.requester_id} for request in food_requests]
    return jsonify({'food_requests': request_list})

@app.route('/food_listings', methods=['POST'])
def create_food_listing():
    form = FoodListingForm()
    if form.validate_on_submit():
        data = request.json
        new_listing = FoodListing(fooditem=data['fooditem'], quantity=data['quantity'],
                                   donor_id=data['donor_id'])
        db.session.add(new_listing)
        db.session.commit()
        return jsonify({'message': 'Food listing created successfully!'})
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400

@app.route('/food_requests', methods=['POST'])
def create_food_request():
    form = FoodRequestForm()
    if form.validate_on_submit():
        data = request.json
        new_request = FoodRequest(
            fooditem=data['fooditem'],
            quantity=data['quantity'],
            requester_id=data['requester_id']
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'Food request created successfully!'})
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400

@app.route('/food_listings/<int:listing_id>', methods=['PATCH'])
def update_food_listing(listing_id):
    form = FoodListingForm()
    if form.validate_on_submit():
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
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400

if __name__ == '__main__':
    app.run(debug=True)