from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from Model import db, Restaurant_Tables

class TableResource(Resource):
	@jwt_required
	def get(self):
		tables = Restaurant_Tables.query.all()
		return jsonify(restaurants=[i.serialize for i in tables])
