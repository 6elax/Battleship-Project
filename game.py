'''
Alexis Luo and Esha Rai
#Snapshot #1: (2/28) Finished targetboard.py and ship.py, oceanboard.py is in progress
#Snapshot #2: (3/7)  Classes Display, Oceanboard, and Battleshipplayer are in progress
#Snapshot #3: (3/16) Finished Oceanboard and Battleshipplayer class, also added case insensitivity. Classes display and game.py are in progress
#Snapshot #4: (3/20) Finished all classes except game.py with some bugs. 
'''

from battleshipplayer import BattleshipPlayer
from oceanboard import OceanBoard
from ship import Ship
from display import Display
from setting import Setting
from letter import Letter

'''
Places the 5 ships onto the Ocean board of 'player'
Creates 5 ships, asks player where it wants them placed, and puts them into
the Ocean board.
'''
def initPlayer(d: Display, player: BattleshipPlayer) -> None:
    # TODO
    carrier = Ship('Carrier', 5)
    battleship = Ship('Battleship', 4)
    destroyer = Ship('Destroyer', 3)
    submarine = Ship('Submarine', 3)
    patrolBoat = Ship('Patrol Boat', 2)
    ship_list = [carrier, battleship, destroyer, submarine, patrolBoat]

    for ship in ship_list:
        #print(d.displayOcean(player))
        
        while True:
            placement = input("Where should  the " + ship.getType() + " (size " + str(ship.getSize()) + ") be placed? ")
            orientation = input("What orientation (h/v)? ")
            if orientation == "h" or orientation == "H":   #horizontal with case insensitivity
                if player.placeShip(ship, placement, orientation) == True:
                    player.placeShip(ship, placement, orientation)
                    print('Your ship has been placed successfully! ')
                    print()
                    print(d.displayOcean(player))
                    print()
                    break
                else: #illegal, try again
                    print('This position is illegal, please input a new location. ')
                    continue
            elif orientation == "v" or orientation == "V": #vertical with case insensitivity
                ship.setHorizontal(False)
                if player.placeShip(ship, placement, orientation) == True:
                    player.placeShip(ship, placement, orientation)
                    print('Your ship has been placed successfully! ')
                    print()
                    print(d.displayOcean(player))
                    print()
                    break
                else: #illegal, try again
                    print('This position is illegal, please input a new location. ')
                    continue #how to do break and continue? keeps printing the above forever...
            else: #illegal, try again
                print('This orientation is invalid, please type the correct orientation (h/v) ')
                continue
    pass

'''
playerNumber calls a shot and p1/p2 player units are updated appropriately
return - True if all ships are sunk after the player's shot
'''
def turn(d: Display, p1: BattleshipPlayer, p2: BattleshipPlayer, playerNumber: int) -> bool:
    # TODO
    #loc = input(p1.getName(),"which grid are you shooting?") #loc like 'a1' or 'j10'
    print(d.displayUnits(p1,p2))
    
    if playerNumber == 1: #for player 1
        loc = input(p1.getName() + ", which grid are you shooting? ") #loc like 'a1' or 'j10'
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
                print("The location is illegal.")
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
                print("The location is illegal.")
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
            else:
                print("The location is illegal.")
                return False
            # x / r position
            if loc[-1] == '0': #10
                if loc[-2] == '1':
                    r = 9
                else:
                    print("The location is illegal.")
                    return False
            else:
                print("The location is illegal.")
                return False
        else:
            print("The location is illegal.")
            return False
        
        if p2.shipAt(r,c) != None: #checks if there is there is a ship in the given location
            '''shipHit = p2.shotAt(r,c)
            if shipHit[0] == True: #if a ship has already been hit
                print("You already hit a " + shipHit[2] + " here...")
            else: #doesnt work...?
            p2.markTargetHit(r,c)     #marks the location as hit'''
            shipShot = p2.shotAt(r,c) #returns the tuple (hit, sunk, name) of a ship
            if shipShot[1] == True:   #if ship is sunk
                print("You sunk " + p2.getName() + "'s " + shipShot[2] + "!")
                if p2.allShipsSunk() == True: #if all ships sunk
                    print("Congratulations, you have sunk all of " + p2.getName() + "'s ships!")
                    return True
            elif shipShot[0] == True:  #if ship is hit:
                print("You hit " + p2.getName() + "'s " + shipShot[2] + "!")
        else: #there is no ship, therefore it is a miss.
            print("Miss!!!")
            missed = p2.missedList
            missed.append((r,c))

    elif playerNumber == 2: #for player 2
        loc = input(p2.getName() + ", which grid are you shooting? ") #loc like 'a1' or 'j10'
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
                print("The location is illegal.")
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
                print("The location is illegal.")
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
            else:
                print("The location is illegal.")
                return False
            # x / r position
            if loc[-1] == '0': #10
                if loc[-2] == '1':
                    r = 9
                else:
                    print("The location is illegal.")
                    return False
            else:
                print("The location is illegal.")
                return False
        else:
            print("The location is illegal.")
            return False

        if p1.shipAt(r,c) != None: #checks if there is there is a ship in the given location
            '''shipHit = p1.shotAt(r,c)
            if shipHit[0] == True: #if a ship has already been hit
                print("You already hit a " + shipHit[2] + " here...")
            else: #doesnt work...?
            p1.markTargetHit(r,c)     #marks the location as hit'''
            shipShot = p1.shotAt(r,c) #returns the tuple (hit, sunk, name) of a ship
            if shipShot[1] == True:   #if ship is sunk
                print("You sunk " + p1.getName() + "'s " + shipShot[2] + "!")
                if p1.allShipsSunk() == True: #if all ships sunk
                    print("Congratulations, you have sunk all of " + p1.getName() + "'s ships!")
                    return True
            elif shipShot[0] == True:  #if ship is hit:
                print("You hit " + p1.getName() + "'s " + shipShot[2] + "!")
        else: #there is no ship, therefore it is a miss.
            print("Miss!!!")
            missed = p1.missedList
            missed.append((r,c))
                    
    return False

def playBattleship(d: Display, settings: Setting) -> None:
    cont = "Y"
    while cont.lower() == 'y':

        manual = input("Do you want to view the instructions on how to play the game Battleship? Type 'Y' if yes. ")
        if manual.lower() == 'y':
            print()
            print(Letter("How to Play Battleship!", 'red'))
            print()
            print('''In Battleship, the goal is win by sinking your opponent's ships. Battleship is played with 2 players. To get started, enter a name for yourself (ex: "player-100"), then your opponent will enter a name for themselves.''')
            print()
            print("Once you start the game, you will first need to place your own ships. To start, you should see five ships: a carrier, battleship, cruiser, submarine and destroyer. Place a ship by selecting it, and then selecting a tile on your board where you'd like to place the ship. You can also rotate a ship by entering the orientation (vertical/horizonta) you want it in. Once you've placed all your ships, the game moves onto the shooting phase.")
            print()
            print("In the shooting phase, players take turns shooting at the opponent's ships. On your turn, type in a tile on your opponent's board that you haven't yet shot at. If you hit an enemy ship, that tile will return with a red '", end='')
            print(Letter("X", 'red'),end='')
            print("'. If you miss, that tile will return with a 'o'.")
            print()
            print("The game continues until a player has lost all their ships. The player left standing wins!")
            print()
            print()

        print("The game will start now!")
        print()

        # player 1 name/placing ships
        name1 = input("What is your name Player 1? ")
        player1 = BattleshipPlayer(name1, 10, 10)
        print("Hi " + name1 + "! Let's start by placing your ships.")
        print()
        print(d.displayOcean(player1))
        print()
        initPlayer(d, player1)
        print()
        print("Thank you for successfully placing your ships! Now it is the next player's turn.")
        print()

        # player 2 name/placing ships
        name2 = input("What is your name Player 2? ")
        player2 = BattleshipPlayer(name2, 10, 10)
        print("Hi " + name2 + "! Let's start by placing your ships.")
        print()
        print(d.displayOcean(player2))
        print()
        initPlayer(d, player2)
        print()
        print("Thank you for successfully placing your ships! Now we will start the shooting phase.")
        print()

        # take turns between player 1 and 2 until one player sinks the other's ships
        theTurn = False
        while theTurn == False:
            if turn(d, player1, player2, 1) == True:
                print("Congrats on winning " + name1 + "! The game is now over! ")
                theTurn = True
            
            if turn(d, player1, player2, 2) == True:
                print("Congrats on winning " + name2 + "! The game is now over!")
                theTurn = True

        # update the score
        if player2.allShipsSunk() == True:
            player1.updateScore(1)
        if player1.allShipsSunk() == True:
            player2.updateScore(1)

        # check if they want to play again
        cont = input("Do you want to play again? (Type 'Y' to play again) ")
    print("Game Over! Thank you for playing!")

def main():
    d = Display()
    #d.message(Letter('X', 'red'))  # example of writing a red X  (you can remove this...)
    d.message("Let's play Battleship!")

    settings = Setting()
    settings.setSetting('mode', 'basic')
    settings.setSetting('numplayers', 2)

    playBattleship(d, settings)

if __name__ == "__main__":
    main()



'''How to Play Battleship

In Battleship, the goal is win by sinking your opponent's ships. Battleship is played with 2 players. To get started, enter a name for yourself (ex: "player-100"), then your opponent will enter a name for themselves. 

Once you start the game, you will first need to place your own ships. To start, you should see five ships: a carrier, battleship, cruiser, submarine and destroyer. Place a ship by selecting it, and then selecting a tile on your board where you'd like to place the ship. You can also rotate a ship by entering the orientation (vertical/horizonta) you want it in. Once you've placed all your ships, the game moves onto the shooting phase.

In the shooting phase, players take turns shooting at the opponent's ships. On your turn, type in a tile on your opponent's board that you haven't yet shot at. If you hit an enemy ship, that tile will return with a red 'X'. If you miss, that tile will return with a 'o'.

The game continues until a player has lost all their ships. The player left standing wins!'''