#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-12-14

@author: CaiKnife
'''

class Song(object):
    count = 0
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.__class__.count += 1

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
print happy_bday.__class__.count

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
print bulls_on_parade.__class__.count