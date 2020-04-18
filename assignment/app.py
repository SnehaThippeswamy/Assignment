from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Task import TaskResource
from resources.auth import SignupApi, LoginApi
from resources.restaurant import RestaurantResource
from resources.RestaurantTables import TableResource
from resources.booking import BookingResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(SignupApi, '/auth/signup')
api.add_resource(LoginApi, '/auth/login')
api.add_resource(RestaurantResource, '/restaurant')
api.add_resource(TableResource, '/restaurantTables')
api.add_resource(BookingResource, '/booking')
