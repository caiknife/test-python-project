#!/usr/bin/env python
# coding:utf8

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install -U " + dist.project_name, shell=True)
