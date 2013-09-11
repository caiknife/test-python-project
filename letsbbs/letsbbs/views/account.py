#coding: utf-8
from flask import Blueprint

account = Blueprint('account', __name__)

@account.route('/')
def index():
    pass

@account.route('/<username>')
def profile(username):
    pass

