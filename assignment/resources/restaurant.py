from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from Model import db, Restaurant

class RestaurantResource(Resource):
	@jwt_required
	def get(self):
		restaurants = Restaurant.query.all()
		return jsonify(restaurants=[i.serialize for i in restaurants])

	@jwt_required
	def post(self):
		json_data = request.get_json(force=True)
		
		if not json_data:
			return {'message': 'No input data provided'}, 400
		# Validate and deserialize input
		if json_data['name'] and type(json_data['name']) is not str:
			return {'message' : 'Please check restaurant name'}, 400

		if 'address' not in json_data:
			return {'message' : 'Address is mandatory'}, 400

		restaurant = Restaurant.query.filter_by(name= request.json['name']).first()
		#checking for task existence
		if restaurant:
			return {'message' : 'Restaurant already exists'}

		new_restaurant = Restaurant(name= request.json['name'], address=request.json['address'])
		db.session.add(new_restaurant)
		db.session.commit()

		return jsonify(restaurant=[new_restaurant.serialize])
