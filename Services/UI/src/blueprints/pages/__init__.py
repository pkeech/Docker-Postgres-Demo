## IMPORT FLASK EXTENSIONS
from flask import render_template, Blueprint, current_app, request, redirect, url_for

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