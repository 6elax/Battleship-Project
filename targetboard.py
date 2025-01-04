from board import Board

#=============================================================================
# Battleship Target Board - this is the vertical board in the Battleship
# game that tracks hits and misses. In the game, when the player guesses and
# hits, a red peg is placed at the coordinate. If it misses, a white peg
# is placed at the coordinate.
# 
# Methods
#    markHit(r, c) - place a "red peg" at (r, c)
#    markMiss(r, c) - place a "white peg" at (r, c)
#    isHit(r, c) - is there a a "red peg" at (r, c)?
#    isEmpty(r, c) - is there any peg at (r, c)?
#=============================================================================
class TargetBoard(Board):

    def __init__(self, rsize, csize):
        # just call the parent's __init__
        super().__init__(rsize, csize)
        # TODO
        pass

    # place a "red peg" at (r, c)
    def markHit(self, r:int, c:int) -> None:
        # TODO
        self.board[r][c] = 'redpeg'
        pass

    # place a "white peg" at (r, c)
    def markMiss(self, r: int, c: int) -> None:
        # TODO
        self.board[r][c] = 'whitepeg'
        pass

    # is there a "red peg" (a hit) at (r, c)?
    def isHit(self, r: int, c: int) -> bool:
        # TODO
        if self.board[r][c] == 'redpeg':
            return True
        return False
        pass

    # is there a any peg at (r, c)?
    def isEmpty(self, r: int, c: int) -> bool:
        # TODO
        if self.board[r][c] == 'redpeg' or self.board[r][c] == 'whitepeg':
            return False
        return True
        pass


'''#test codes
target = TargetBoard(10, 10)
target.markHit(3,4)
target.markMiss(5,7)
what = target.isEmpty(3, 4)
print(what)
what = target.isHit(3, 4)
print(what)
what = target.isHit(5, 7)    
print(what)'''