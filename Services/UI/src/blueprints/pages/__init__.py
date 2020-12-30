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

## ROUTE: ADD ACCOUNTS
@page.route("/add_default")
def add_default():
    ## DEFINE DEFAULT USER ACCOUNTS
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')

    ## Search For Existing Account
    if User.query.filter_by(username='admin').first() != None:
        return "Accounts (Admin) Already Created!"

    if User.query.filter_by(username='guest').first() != None:
        return "Accounts (Guest) Already Created!"

    ## Create User Accounts
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    ## Return Response
    return "Accounts Added !!"

## ROUTE: SEARCH ACCOUNT
@page.route("/search/<username>")
def search(username):
    ## SEARCH FOR USER ACCOUNT
    account = User.query.filter_by(username=username).first_or_404(description='No user account found with the username:  {}'.format(username))

    ## RETURN RESPONSE
    return f"<h1>Results</h1><table><tr><th>ID</th><th>Username</th><th>Email</th></tr><tr><td>{ account.id }</td><td>{ account.username }</td><td>{ account.email }</td></tr></table>"

## ROUTE: SEARCH ALL
@page.route("/search")
def search_all():
    ## SEARCH ALL ACCOUNTS
    accounts = User.query.all()

    ## CREATE RESPONSE
    resp = "<h1>Results</h1><table><tr><th>ID</th><th>Username</th><th>Email</th></tr>"

    ## LOOP THROUGH RESULTS
    for account in accounts:
        resp = resp + f"<tr><td>{ account.id }</td><td>{ account.username }</td><td>{ account.email }</td></tr>"

    ## CLOSE OUT TABLE
    resp = resp + "</table>"

    ## DISPLAY PAGE
    return resp

## ROUTE: DELETE ACCOUNT
@page.route("/delete/<username>")
def delete_account(username):
    ## SEARCH FOR USER ACCOUNT
    account = User.query.filter_by(username=username).first_or_404(description='No user account found with the username:  {}'.format(username))
    
    ## DELETE ACCOUNT
    db.session.delete(account)
    db.session.commit()

    ## DISPLAY RESPONSE
    return f"{ username } Account Deleted Succesfully !"