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

greets = ['Greetings', 'Hi', 'Howdy', 'Bonjour', 'Hey', 'Howdy-Do', "What's Up", 'Hello']
planet = ['World', 'Earth', 'Nature', 'Cosmos', 'Macrocosm', 'Universe', 'Terra']

if __name__ == '__main__':

    print("{0} {1}".format(greets[randint(1, len(greets)-1)], planet[randint(1, len(planet)-1)], end=""))
