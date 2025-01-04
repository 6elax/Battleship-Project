from cgi import FieldStorage
from board import Board
from ship import Ship

'''
The Ocean Board is the portion of the Battleship Unit that holds
ships that the player had placed and keeps track of hits upon each
ship that the opponent has guessed correctly.
'''
class OceanBoard(Board):

    def __init__(self, rsize, csize):
        # call parent's __init__
        super().__init__(rsize, csize) 
        # TODO
        self.ships = []


    #list of all existing ship locations
    def shipListLocs(self, shiplist):
        shipLocs = []
        for existingShip in shiplist:
            if existingShip.isHorizontal == True:
                (a,b) = existingShip.getLocation()
                for i in range(existingShip.getSize()):
                    shipLocs.append((a+i,b))
            else: #vertical
                (a,b) = existingShip.getLocation()
                for i in range(existingShip.getSize()):
                    shipLocs.append((a,b+i))
        return(shipLocs)

    # return False if ship could not be placed at r, c
    #    either r, c are illegal
    #    or ship is too big to be placed there
    #    or another ship is already there
    # Modify 'ship' with the given (r, c) and orientation
    # Add 'ship' to the the OceanBoard's list of 'ships' if placed successfully
    def placeShip(self, ship: Ship, r:int, c:int, orientation:str) -> bool:
        # TODO
        s = ship.size
        list_of_ship = self.shipListLocs(self.ships)
        if orientation.lower() == 'h': #horizontal! allows case insensitivity WRONG
            if r+s<=9 and r>=0 and c<=9 and c>=0: #makes sure the positions are legal
                for i in range(r,r+s): #locations of ship in the r value
                    for k in list_of_ship: #checks if there is another ship in loc
                        if (i,c) == k:
                            return False
                ship.setLocation(r,c)
                self.ships.append(ship) 
                return True

        if orientation.lower() == 'v': #vertical! allows case insensitivity
            if c+s<=9 and c>=0 and r<=9 and r>=0: #makes sure the positions are legal
                for i in range(c,c+s): #locations of ship in the c value
                    for k in list_of_ship: #checks other ship locs
                        if (r,i) == k:
                            return False
                ship.setHorizontal(False)
                ship.setLocation(r,c)
                self.ships.append(ship) 
                return True
        return False

    #returns the locations a single ship occupies
    def singleShipLoc(self, ship):
        ship_List = []
        if ship.horizontal == True: #horizontal ship
            for i in range(ship.size):
                ship_List.append((ship.loc[0]+i, ship.loc[1]))
        else:                       #vertical ship
            for i in range(ship.size):
                ship_List.append((ship.loc[0], ship.loc[1]+i))
        return(ship_List)

    # are all 'ships' in the OceanBoard sunk?
    def allShipsSunk(self):
        # TODO
        x = 0
        for ship in self.ships:
            if ship.isSunk() == True:
                x = x + 1
        if len(self.ships) == x:
            return True
        return False



'''#test codes
ocean = OceanBoard(10, 10)
carrier = Ship('Carrier', 5)
placed = ocean.placeShip(carrier, 1, 1, 'V') #returns True
print(placed)
r, c = carrier.getLocation()                 # returns 1, 1
print(r,c)
horizontal = carrier.isHorizontal()          #returns False
print(horizontal)
placed = ocean.placeShip(Ship("Battleship", 4), 0, 1, 'h') # returns False
print(placed)
placed = ocean.placeShip(Ship("Battleship", 4), 0, 1, 'v') # returns True
print(placed)
placed = ocean.placeShip(Ship("Destroyer", 3), 1, 0, 'v') # returns False
print(placed)
placed = ocean.placeShip(Ship("Submarine", 3), 1, 0, 'h') # returns True
print(placed)'''