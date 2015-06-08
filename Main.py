# Main RPG game
# Jonathan Harris
# June 7, 2015

from __future__ import print_function

class Race:
    def __init__(self):
        self.races = ["Human","Elf","Dwarf","Halfing", "Gnome"]

class Player:

    def __init__(self):
        self.name = None
        self.level = 1
        self.playerClass = None
        self.armorClass = 0
        self.initiative = 0
        self.proficiency = 0
        self.hp = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.race = Race()

    def setName(self, playerName):
        self.name = playerName

    def getName(self):
        return self.name




if __name__ == '__main__':
    player = Player()
    print("Hello young sir/ma'am. Let me tell you a story.")
    print(
        "But first I must know your name. So tell me there. What is your name.")
    name = raw_input()
    player.setName(name)
    print("OK " + player.getName() +
          " but before we continue, you need a profession.")
    print(
        "Since this is a DnD type game, you need to choose a class and a race.")
