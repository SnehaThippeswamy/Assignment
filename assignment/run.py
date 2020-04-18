from flask import Flask

def create_app(config_filename):
	app = Flask(__name__)
	app.config.from_object(config_filename)
	# app.config.from_envvar('ENV_FILE_LOCATION')

	from app import api_bp
	app.register_blueprint(api_bp, url_prefix='/api')

	from Model import db
	db.init_app(app)

	from flask_jwt_extended import JWTManager
	jwt = JWTManager(app)

	from resources.booking import mail
	mail.init_app(app)

	return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)