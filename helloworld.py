##########################################################################################
#
# FileName : helloworld.py
#
# Description : The main workhorse of this project!  The Place where all the magic Happens
#               This program, when run will print a random greeting to the screen using synonyms
#               for 'hello' and 'world'
#               Variables greets and planet are lists and can have words added to allow for a wider
#               range of available greetings
#
# Version : 1.01
#
# Author : Christian Weaver  aka: Dreddsparc
#
##########################################################################################
from random import *
import kivy
from kivy.app import App
from kivy.uix.button import Button
kivy.require('1.0.0')

greets = ['Greetings', 'Hi', 'Howdy', 'Bonjour', 'Hey', 'Howdy-Do', "What's Up", 'Hello', 'Yo']
planet = ['World', 'Earth', 'Nature', 'Cosmos', 'Macrocosm', 'Universe', 'Terra', 'Round Not Flat Planet']
greeting = "{0} {1}".format(greets[randint(1, len(greets)-1)], planet[randint(1, len(planet)-1)])


class HelloWorldApp(App):
    def build(self):
        return Button(text=greeting)


if __name__ == '__main__':
    HelloWorldApp().run()
