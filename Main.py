#Main RPG game
#Jonathan Harris
#June 7, 2015

from __future__ import print_function

class Player:
    def __init__(self):
        self.name = None
        self.playerClass = None
        self.health = 0

    def setName(self, playerName):
        self.name = playerName

    def getName(self):
        return self.name


if __name__ == '__main__':
    player = Player()
    print("Hello young sir/ma'am. Let me tell you a story.")
    print("But first I must know your name. So tell me there. What is your name.")
    name = raw_input()
    player.setName(name)
    print("OK " + player.getName() + " but before we continue, you need a profession.")
    print("Since this is a DnD type game, you need to choose a class and a race.")
