#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

from flask import Flask
from flaskext.actions import Manager
from letsbbs import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()

