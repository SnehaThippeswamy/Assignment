from flask import Response, request
from flask_jwt_extended import create_access_token
from Model import db, User
from flask_restful import Resource
import datetime

class SignupApi(Resource):
	def post(self):
		body = request.get_json()
		user = User(**body)	
		db.session.add(user)
		db.session.commit()
		id = user.id
		return {'id': str(id)}, 200

class LoginApi(Resource):
	def post(self):
		body = request.get_json()
		user = User.query.filter_by(email=body.get('email')).first()
		expires = datetime.timedelta(days=7)
		access_token = create_access_token(identity=str(user.id), expires_delta=expires)
		return {'token': access_token}, 200