from flask import jsonify, request, session
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask_mail import Message,Mail
from Model import db, Restaurant, Restaurant_Tables, User, Book
from datetime import datetime

mail = Mail()

class BookingResource(Resource):
	@jwt_required
	def get(self):
		json_data = request.get_json()
		if not json_data:
			restaurants = Restaurant.query.all()
			return jsonify(message = "Please select the Restaurant.",restaurants=[i.serialize for i in restaurants])

		if not 'name' in json_data:
			return {'message': 'Restaurant name not found, please select restaurant'}, 400

		if 'id' in json_data and 'name' in json_data:
			restaurant = Restaurant.query.filter_by().filter_by(id= request.json['id'], name=request.json['name']).first()

		if 'name' in json_data:
			restaurant = Restaurant.query.filter_by().filter_by(name=request.json['name']).first()

		session['restaurant_id'] = restaurant.id
		restaurant_tables = Restaurant_Tables.query.filter_by(restaurant_id= restaurant.id).all()

		return jsonify(message = "Please select the Table that you want to book.",restaurants=[i.serialize for i in restaurant_tables])

	@jwt_required
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'Restaurant name and table found, please select..'}, 400

		if 'number' not in json_data:
			return {'message' : 'Please Select table.'}, 400

		if 'no_of_guests' not in json_data:
			return {'message' : 'Please specify number of guests.'}, 400

		if 'reserved_date' not in json_data:
			return {'message' : 'Reservation date missing'}, 400

		exist = Book.query.filter_by(restaurant_id=session['restaurant_id'], table_id=json_data['number'],
			reserved_date=datetime.strptime(json_data['reserved_date'],'%d-%m-%Y').date())

		if exist:
			return {'message' : 'Already reserved'}, 400

		new_reservation = Book(user_id=get_jwt_identity(), restaurant_id=session['restaurant_id'], table_id=json_data['number'], 
			no_of_guests=json_data['no_of_guests'],reserved_date=datetime.strptime(json_data['reserved_date'],'%d-%m-%Y').date(), 
			bill=(int(json_data['no_of_guests']) * 500))

		# table = Restaurant_Tables.query.filter_by(restaurant_id= session['restaurant_id'], number=json_data['number']).first()
		db.session.add(new_reservation)
		db.session.commit()

		email_id = User.query.filter_by(id=get_jwt_identity()).first()

		msg = Message('Booking confirmation.',recipients=[email_id.email])
		
		msg.body ='Hi {},Your booking has been confirmed, your total bill is {}Rs'.format(email_id.name,(int(json_data['no_of_guests']) * 500))
		
		mail.send(msg)
		return jsonify(status="reservation confirmed please check the mail")



