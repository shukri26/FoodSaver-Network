from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)

    # One-to-Many Relationship 1: User to FoodListing (Donor to Donated Food)
    food_listings = db.relationship('FoodListing', backref='donor', lazy=True)

    # One-to-Many Relationship 2: User to FoodRequest (Recipient to Requested Food)
    food_requests = db.relationship('FoodRequest', backref='requester', lazy=True)

class FoodListing(db.Model):
    __tablename__ = 'food_listing'

    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key to link to the User who created the listing
    fooditem = db.Column(db.String)
    quantity = db.Column(db.Integer)
    expiry = db.Column(db.Integer)
    pickup_location = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Many-to-Many Relationship: FoodListing to FoodRequest (Matched Donations)
    food_requests = db.relationship(
        'FoodRequest',
        secondary='donations',
        back_populates='food_listings'
    )

class FoodRequest(db.Model):
    __tablename__ = 'food_request'

    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key to link to the User who made the request
    food_types = db.Column(db.String)
    quantity = db.Column(db.Integer)
    delivery_time = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Many-to-Many Relationship: FoodListing to FoodRequest (Matched Donations)
    food_listings = db.relationship(
        'FoodListing',
        secondary='donations',
        back_populates='food_requests'
    )

# Create an association table for the many-to-many relationship
donations = db.Table(
    'donations',
    db.Column('food_listing_id', db.Integer, db.ForeignKey('food_listing.id')),
    db.Column('food_request_id', db.Integer, db.ForeignKey('food_request.id'))
)
    