## IMPORT PYTHON MODULES
import os

## FLASK SETTINGS
SECRET_KEY = os.environ.get('SECRET_KEY', default="asldkfasdlkjflaksdjflksadjl")

## FLASK-SQLALCHEMY SETTINGS
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', default='postgresql://test:test@db/test')
SQLALCHEMY_TRACK_MODIFICATIONS = False