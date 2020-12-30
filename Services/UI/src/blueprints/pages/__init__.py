## IMPORT FLASK EXTENSIONS
from flask import render_template, Blueprint, current_app, request, redirect, url_for
from src.extensions import db
from src.models import User

## IMPORT PYTHON MODULES
import requests, os

## Define Blueprint
page = Blueprint('page', __name__, template_folder='templates')

## ROUTE: INDEX
@page.route("/")
def index():
    ## RENDER PAGE
    #return render_template('index.html')
    return "HELLO WORLD"

@page.route("/add_default")
def add_default():
    ## DEFINE DEFAULT USER ACCOUNTS
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')

    ## Create User Accounts
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    ## Return Response
    return "Accounts Added !!"