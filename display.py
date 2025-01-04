from battleshipplayer import BattleshipPlayer
from ship import Ship
from letter import Letter
import subprocess

'''
Display - a class that handles the display of the Battleship game. It handles
all the printing and inputing for the game. It has some methods that help
move the cursor around for a more pleasant user game experience.
'''
class Display:

    #### DO NOT MODIFY LINES BELOW ####
    # move to 1, 1
    def home(self) -> None:
        print(u'\u001b[H', end='')

    # move cursor to line, col
    def moveTo(self, line, col) -> None:
        print(u'\u001b[' + f"{line};{col}H", end='')

    # move cursor to column col 
    def moveToColumn(self, col) -> None:
        print(u'\u001b[' + f"{col}G", end='')

    # clear to the end of line (keeping cursor at the current position)
    def clearToEndOfLine(self) -> None:
        print(u'\u001b[K', end='')

    # clear to the end of screen (keeping cursor at the current position)
    def clearToEndOfScreen(self) -> None:
        print(u'\u001b[J', end='')

    # clear screen and move to top left (1,1) of screen
    def clearScreen(self) -> None:
        self.home()
        self.clearToEndOfScreen()

    # return the proper column position for player X
    def playerColumn(self, playerNum: int) -> str:
        if playerNum== 2:
            column = 76
        else:
            column = 0
        return column

    # display message for player X
    def message(self, msg: str, playerNum = 1) -> None:
        self.moveToColumn(self.playerColumn(playerNum))
        print(msg)

    # ask for input from player X
    def ask(self, msg: str, playerNum = 1) -> str:
        self.moveToColumn(self.playerColumn(playerNum))
        return input(msg)

    def newLine(self):
        print()
    #### DO NOT MODIFY LINES ABOVE ####

    #### MODIFY BELOW ####
    # display the Ocean board of the player
    def displayOcean(self, player: BattleshipPlayer) -> None: 
        
        #original board displayed
        list_letter = ["a","b","c","d","e","f","g","h","i","j"]
        print("  ",end='')
        for a in range(10):
            print(a+1,end=" ")
        print()
        for y in range(len(list_letter)):
            print(list_letter[y], end=' ')
            for x in range(10):
                theShip = player.shipAt(x, y)
                if theShip != None:
                    shipName = theShip.getType()
                    print(shipName[0], end=' ')
                else:
                    print('.', end=' ')
            print()


    # display both player 1 and player 2 ocean & target units
    def displayUnits(self, p1: BattleshipPlayer, p2: BattleshipPlayer) -> None:

        #PLAYER 1
        print(p1.getName() + "'s Battleship Unit")
        #oceanboard
        print("Ocean")
        list_letter = ["a","b","c","d","e","f","g","h","i","j"]
        print("  ",end='')
        for a in range(10):
            print(a+1,end=" ")
        print()
        for y in range(len(list_letter)):
            print(list_letter[y], end=' ')
            for x in range(10):
                theShip = p1.shipAt(x, y)
                if theShip != None:
                    shipName = theShip.getType()
                    if theShip.isHitAt(x, y) == True:
                        print(Letter(shipName[0], 'red'), end=' ')
                    else:
                        print(shipName[0], end=' ')
                else:
                    print('.', end=' ')
            print()
        #targetboard
        print("Target")
        list_letter = ["a","b","c","d","e","f","g","h","i","j"]
        print("  ",end='')
        for a in range(10):
            print(a+1,end=" ")
        print()
        for y in range(len(list_letter)):
            print(list_letter[y], end=' ')
            for x in range(10):
                theShip = p2.shipAt(x, y)
                if theShip != None:
                    if theShip.isHitAt(x, y) == True:
                        print(Letter('X', 'red'), end=' ')
                    else:
                        print('.', end=' ')
                elif (x,y) in p2.getMissedList():
                    print('o', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()

        #PLAYER 2
        print(p2.getName() + "'s Battleship Unit")
         #oceanboard
        print("Ocean")
        list_letter = ["a","b","c","d","e","f","g","h","i","j"]
        print("  ",end='')
        for a in range(10):
            print(a+1,end=" ")
        print()
        for y in range(len(list_letter)):
            print(list_letter[y], end=' ')
            for x in range(10):
                theShip = p2.shipAt(x, y)
                if theShip != None:
                    shipName = theShip.getType()
                    if theShip.isHitAt(x, y) == True:
                        print(Letter(shipName[0], 'red'), end=' ')
                    else:
                        print(shipName[0], end=' ')
                else:
                    print('.', end=' ')
            print()
        #targetboard
        print("Target")
        list_letter = ["a","b","c","d","e","f","g","h","i","j"]
        print("  ",end='')
        for a in range(10):
            print(a+1,end=" ")
        print()
        for y in range(len(list_letter)):
            print(list_letter[y], end=' ')
            for x in range(10):
                theShip = p1.shipAt(x, y)
                if theShip != None:
                    if theShip.isHitAt(x, y) == True:
                        print(Letter('X', 'red'), end=' ')
                    else:
                        print('.', end=' ')
                elif (x,y) in p1.getMissedList():
                    print('o', end=' ')
                else:
                    print('.', end=' ')
            print()

'''#test codes
d = Display()
p1 = BattleshipPlayer("Mark")
d.displayOcean(p1)
p1.placeShip(Ship("Carrier", 5), 'a1', 'h')
d.displayOcean(p1)
p2 = BattleshipPlayer("Steve")
p2.placeShip(Ship("Battleship", 4), 'b9', 'v')
d.displayOcean(p2)
p2.placeShip(Ship("Submarine", 3), 'a9', 'v') #bug exists where it'll still place a ship where a ship already is
d.displayOcean(p2)

p1.shotAt(0,0)
p1.shotAt(2,5)
p2.shotAt(0,0)
p2.shotAt(2,5)

d.displayUnits(p1, p2)'''