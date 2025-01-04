from oceanboard import OceanBoard
from targetboard import TargetBoard
from letter import Letter
from ship import Ship
from board import Board
#from display import Display

class BattleshipPlayer:

    '''
    Models the Battleship Player
      player = Battleship("Joe")    # default 10x10 board

    State Variables
      name (str) - the name of the player
      score (int) - the score of the player
      ocean (OceanBoard) - the board which contains all of the ships
      target (TargetBoard) - the board whih contains all the shots made
    '''
                             # optional parameters default is 10x10
    def __init__(self, name: str, rsize=10, csize=10):
        self.name = name
        self.score = 0
        self.missedList = []
        self.ocean = OceanBoard(rsize, csize)
        self.target = TargetBoard(rsize, csize)

    def getName(self) -> str:
        return self.name

    def getOcean(self) -> OceanBoard:
        return self.ocean

    def getTarget(self) -> TargetBoard:
        return self.target

    def getScore(self) -> int:
        return self.score
    
    def getMissedList(self):
        return self.missedList
    
    ### DO NOT MODIFY ABOVE METHODS ###

    #### MODIFY BELOW ####
    ### Add the following methods below and any others you may find useful ###

    '''
    loc: grid location like 'a1' or 'j10'
    orientation: 'h' or 'v' for horizontal or vertical
    return: True if ship was successfully placed
    '''
    def placeShip(self, ship: Ship, loc: str, orientation: str) -> bool:
        # TODO
        # translation
        if len(loc) == 2:
            # y / c position   #also allows case insensitivity
            if loc[0] == 'a' or loc[0] == 'A':
                c = 0
            elif loc[0] == 'b' or loc[0] == 'B':
                c = 1
            elif loc[0] == 'c' or loc[0] == 'C':
                c = 2
            elif loc[0] == 'd' or loc[0] == 'D':
                c = 3
            elif loc[0] == 'e' or loc[0] == 'E':
                c = 4
            elif loc[0] == 'f' or loc[0] == 'F':
                c = 5
            elif loc[0] == 'g' or loc[0] == 'G':
                c = 6
            elif loc[0] == 'h' or loc[0] == 'H':
                c = 7
            elif loc[0] == 'i' or loc[0] == 'I':
                c = 8
            elif loc[0] == 'j' or loc[0] == 'J':
                c = 9
            else:
                print("The location is illegal. Please input another location.")
                return False
            # r / x position
            if loc[-1] == '1':
                r = 0
            elif loc[-1] == '2':
                r = 1
            elif loc[-1] == '3':
                r = 2
            elif loc[-1] == '4':
                r = 3
            elif loc[-1] == '5':
                r = 4
            elif loc[-1] == '6':
                r = 5
            elif loc[-1] == '7':
                r = 6
            elif loc[-1] == '8':
                r = 7
            elif loc[-1] == '9':
                r = 8
            else:
                print("The location is illegal. Please input another location.")
                return False
        elif len(loc) == 3:
            # y / c position   #also allows case insensitivity
            if loc[0] == 'a' or loc[0] == 'A':
                c = 0
            elif loc[0] == 'b' or loc[0] == 'B':
                c = 1
            elif loc[0] == 'c' or loc[0] == 'C':
                c = 2
            elif loc[0] == 'd' or loc[0] == 'D':
                c = 3
            elif loc[0] == 'e' or loc[0] == 'E':
                c = 4
            elif loc[0] == 'f' or loc[0] == 'F':
                c = 5
            elif loc[0] == 'g' or loc[0] == 'G':
                c = 6
            elif loc[0] == 'h' or loc[0] == 'H':
                c = 7
            elif loc[0] == 'i' or loc[0] == 'I':
                c = 8
            elif loc[0] == 'j' or loc[0] == 'J':
                c = 9
            # x / r position
            if loc[-1] == '0': #10
                if loc[-2] == '1':
                    r = 9
                else:
                    print("The location is illegal. Please input another location.")
                    return False
            else:
                print("The location is illegal. Please input another location.")
                return False
        else:
            print("The location is illegal.")
            return False

        if self.ocean.placeShip(ship, r, c, orientation) == True:
            self.ocean.placeShip(ship, r, c, orientation)
            return True
        else:
            return False

    def shipAt(self, r, c) -> Ship:
        for ship in (self.ocean.ships):
            for loc in (self.ocean.singleShipLoc(ship)):
                if loc == (r,c):
                    return ship
        return None

    '''
    Process the shot at (r, c) and return (hit, sunk, name)
      - Determine if there is a hit
      - Check if the ship is sunk
      - Get the name of the ship (if there is a hit)
      - Mark the ship as being hit
    '''
    def shotAt(self, r: int, c: int) -> bool:
        # TODO

        hit = False
        sunk = False
        name = ''
        ship = self.shipAt(r, c) #ship = returned ship from shipAt method
        
        if ship != None:

            #testing to see if 'hit' is True or not (code taken from Ship's isHitAt/markHitAt method)
            x = ship.loc[0]
            y = ship.loc[1]
            if ship.horizontal == True:  #horizontal
                if c == y:
                    for i in range(ship.size):
                        if x+i == r:
                            ship.status[i] = 1 
                            hit = True
            else:                        #vertical
                if r == x:
                    for i in range(ship.size):
                        if y+i == c:
                            ship.status[i] = 1 
                            hit = True

            #testing to see if 'sunk' is True or not (code taken from Ship's isSunk method)
            a = 0
            for char in ship.status:
                if char == 1:
                    a = a + 1
            if a == len(ship.status):
                sunk = True

            name = ship.type
        
        else:
            self.missedList.append((r,c))

        return (hit, sunk, name)

    def markTargetHit(self, r: int, c: int) -> None:
        # TODO
        ship1 = self.shipAt(r, c) #ship = returned ship from shipAt method
        if ship1 != None:
            TargetBoard.markHit(r,c)
        pass

    def markTargetMiss(self, r: int, c: int) -> None:
        # TODO
        ship2 = self.shipAt(r, c) #ship = returned ship from shipAt method
        if ship2 == None:
            TargetBoard.markMiss(r, c)
        pass

    def allShipsSunk(self):
        return(self.ocean.allShipsSunk())

    '''
    Resets both the ocean and target board so that game could
    be restarted
    '''
    def resetUnit(self) -> None:
        # TODO
        self.ocean.ships = []
        self.target.resetBoard()
        pass

    '''
    Adds num to the score
    '''
    def updateScore(self, num: int) -> None:
        # TODO
        self.score += num
        pass


'''#test codes
player = BattleshipPlayer('Mark', 10, 10)
placing = player.placeShip(Ship('Carrier', 5), 'b2', 'h')
print('**197: ', placing)                     #returns True
ship = player.shipAt(0, 0)                  # None – no ship there
print('**199: ',ship)
ship = player.shipAt(1, 1)                  # returns the Carrier ship
print('**201: ',ship)
(hit, sunk, name) = player.shotAt(0, 0)     # False, False, “”
print('**203: ',(hit, sunk, name))
(hit, sunk, name) = player.shotAt(1, 1)     # True, False, “Carrier”
print('**205: ',(hit, sunk, name))
(hit, sunk, name) = player.shotAt(2, 1)     # True, False, “Carrier”
print('**207: ',(hit, sunk, name))
(hit, sunk, name) = player.shotAt(3, 1)     # True, False, “Carrier”
print('**209: ',(hit, sunk, name))
(hit, sunk, name) = player.shotAt(4, 1)     # True, False, “Carrier”
print('**211: ',(hit, sunk, name))
(hit, sunk, name) = player.shotAt(5, 1)     # True, True, “Carrier” - SUNK!!
print('**213: ',(hit, sunk, name))
allSunk = player.allShipsSunk()     # True – since the Carrier was only ship placed
print('**215: ',allSunk)'''