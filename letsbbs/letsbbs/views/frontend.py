# -*- encoding:utf-8 -*-
from flask import Blueprint
from flask import render_template 
from letsbbs.models import User

frontend = Blueprint('frontend',__name__)

@frontend.route('/')
def index():
    return render_template('frontend/index.jinja')

@frontend.route('/view/<uid>')
def view(uid):
    if uid:
        user = User.query.get_or_404(uid)

    return render_template('frontend/view.jinja', user=user)
