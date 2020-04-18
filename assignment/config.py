import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'

SECRET_KEY = 't1NP63m4wnBg6nyHYgfhfghghdhgdhg'


TESTING = False #Suppress send and this has to be same
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
# MAIL_DEBUG = True
MAIL_USERNAME = 'snehadevelop@gmail.com' # username
MAIL_PASSWORD = '##############'
MAIL_DEFAULT_SENDER = ('Sneha Thippeswamy','snehadevelop@gmail.com') #default sender that you want to set eg, tsneh..@gmail.com
MAIL_MAX_EMAILS = None #to avoid sendinng multiple mails eg, by mistake if it sends 100 mails then it restricts to 5 to avoid such cases
MAIL_SUPPRESS_SEND = False
MAIL_ASCII_ATTACHMENTS = False
