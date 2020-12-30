## IMPORT FLASK & EXTENSIONS
from flask import Flask, g
from src.extensions import db, migrate 

## IMPORT BLUEPRINTS
from .blueprints.pages import page

## [FOR DOCKER PURPOSES] Redirect Logs to STDOUT
import logging, os
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

## Define Flask Application
def create_app(settings_override=None):
    ## Create Application with Instance Folder
    app = Flask(__name__, instance_relative_config=True)

    ## Load Configurations
    app.config.from_object('src.config.settings')

    ## Initialize Extenstions
    extensions(app)

    ## Create Application Context
    with app.app_context():

        ## Register Blueprints
        app.register_blueprint(page)

        ## Create Database Objects
        import src.models
        db.create_all()

        ## Application Logging (STDOUT)
        app.logger.addHandler(stream_handler)

        ## Return Application
        return app

## Load (Stage) Flask Extensions
def extensions(app):
    ## Initialize ORM
    db.init_app(app)

    ## Initialize DB Migrations
    migrate.init_app(app, db)
    
    return None