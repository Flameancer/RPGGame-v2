#Main RPG game
#Jonathan Harris
#June 7, 2015

from __future__ import print_function

class Game:
    def __init__(self, name):
        self.name = name
        self.objects = {}
        self.p1 = None

        for i in range(10):
            self.objects[i] = i

    def printName(self):
        print(self.name)

    def printDic(self):
        self.p1 = Player("John")
        self.p1.printStuff(self.objects)

    def printPlayerName(self):
        print("The players name is " + self.p1.getName())



class Player:

    def __init__(self, name):
        self.name =name

    def printStuff(self,dictionary):
        print(dictionary)

    def getName(self):
        return self.name

        
if __name__ == '__main__':
    game = Game("lol")
    game.printDic()
    game.printPlayerName()
    #game.printName()
