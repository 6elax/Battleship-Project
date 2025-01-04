#=============================================================================
# Models one of the plastic ships in the Battleship game
# The plastic ships have 2-5 holes in them depending on the size of the ship.
# When a hit is registered, a red peg is placed in the plastic hole.
# 
# The class has the following attributes:
# 
#    type (str) - like "Cruiser"
#    size (int) - 3
#    status (list) - [0, 0, 0] to model the plastic holes that get filled with red pegs
#    loc (int, int) - the row, col location of the ship - ex. (3, 5)
#    horizontal (bool) - boolean if horizontal in orientation - ex. True
# 
#    In the above example, the ship is a "Cruiser" and occupies (3, 5), (3, 6), (3, 7)
#    If it were vertical instead, the ship would occupy (3, 5), (4, 5) and (5, 5)
#
# Methods
#    markHitAt(r, c) - modify the status of the ship to a 'hit' at (r, c) - "fill in the
#                      plastic hole with a red peg"
#    isHitAt(r, c) - is the a "red peg" at (r, c)?
#    isSunk() - the entire ship is sunk - all the status[] are 'hit's (i.e. filled with "red pegs")
#=============================================================================
from turtle import hideturtle


class Ship:

    #### DO NOT MODIFY LINES BELOW ####
    def __init__(self, type: str, size: int):
        '''
        Constructor
        type - Name of the ship
        size - how many pegs are in the ship
        '''
        self.type = type
        self.size = size
        self.status = [0 for _ in range(size)]  # models the plastic pegs marking a 'hit'
        self.loc = (0, 0)                       # default initialization
        self.horizontal = True                  # default initialization

    def getType(self) -> str:
        return self.type

    def getSize(self) -> int:
        return self.size

    # r, c valid numbers are 0 - 9 representing rows A - J and columns 1 - 10
    # Assume that r and c are valid
    def setLocation(self, r: int, c: int):
        self.loc = (r, c)

    def getLocation(self):
        return self.loc

    def setHorizontal(self, h: bool) -> None:
        self.horizontal = h

    def isHorizontal(self) -> bool:
        return self.horizontal
    #### DO NOT MODIFY LINES ABOVE ####

    ### Add the following methods below and any others you may find useful ###
    def markHitAt(self, r: int, c: int):
        # TODO
        x = self.loc[0]
        y = self.loc[1]
        if self.horizontal == True:  #horizontal
            if c == y:
                for i in range(self.size):
                    if x+i == r:
                        self.status[i] = 1
        else:                        #vertical
            if r == x:
                for i in range(self.size):
                    if y+i == c:
                        self.status[i] = 1 
        pass

    def isSunk(self) -> bool:
        # TODO
        x = 0
        for i in self.status:
            if self.status[i] == 1:
                x = x + 1
        if x == len(self.status):
            return True
        return False

    def isHitAt(self, r: int, c: int) -> bool:
        # TODO
        x = self.loc[0]
        y = self.loc[1]
        if self.horizontal == True:  #horizontal
            if c == y:
                for i in range(self.size):
                    if x+i == r:
                        if self.status[i] == 1:
                            return True
        else:                        #vertical
            if r == x:
                for i in range(self.size):
                    if y+i == c:
                        if self.status[i] == 1:
                            return True
        return False

'''#test cases
ship = Ship('Battleship', 4)
ship.setLocation(3, 5)
ship.setHorizontal(False) #i.e. ship covers (3,5) (3,6) (3,7) (3,8)

ship.markHitAt(3, 6)
ship.markHitAt(3, 7)
hit = ship.isHitAt(3, 7) #True
print(hit)
hit = ship.isHitAt(3, 8) #False
print(hit)

sunk = ship.isSunk() #False
print(sunk)
ship.markHitAt(3, 5)
ship.markHitAt(3, 8)
sunk = ship.isSunk() #True
print(sunk)

ship.markHitAt(0, 2) #illegal
hit = ship.isHitAt(0,2) #False
print(hit)'''