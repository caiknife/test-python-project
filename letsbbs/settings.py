# -*- encoding:utf-8 -*-

# SQL Alchemy settings
DB_URI = 'sqlite:///letsbbs.db'

SECRET_KEY = 'eV#oz^8D3.71p=]SGKLRT@vY3`>F~s49'

import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + ROOT_PATH +'/letsbbs.db'