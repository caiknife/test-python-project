#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-12-15

@author: caiknife
'''

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)
        

        