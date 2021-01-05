#Hopefully a fully working chess game built from scratch in python

class Board:
    #A class to represent the chess board
    squares = {}

    def populateSquares(self):
       # print("here")
        for row in range(8):
            for col in range(8):
                number = row * 8 + col
                pos = [row, col]
                occ = row == 0 or row == 1 or row == 6 or row == 7

                #Even rows have black - white pattern
                if (row % 2 ==  0):
                    if (col % 2 == 0):
                        color = "Black"
                    else: color = "White"
                #Odd rows have white - black pattern
                else: 
                    if (col % 2 == 0):
                        color = "White"
                    else: color = "Black"
                
                self.squares[number] = (Square(pos, occ, color))

class Square(Board):
        number = int
        position = [int, int]
        occupied = bool
        color = str
       
        def __init__(self, pos, occ, color):
            self.position = pos
            self.occupied = occ
            self.color = color

class Row:
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8

class Piece:
    position = [int, int]
    color = str

    """Checks if sqaure is within the board"""
    def outOfBounds(self, pos):
        if (pos[0] > 7 or pos[0] < 0):
            return True
        if (pos[1] > 7 or pos[1] < 0):
            return True 
        return False

    def inCheck(self):
        pass

    """Checks that the square reached by pos is a valid square for this piece"""
    def isSquareValid(self, pos):
        if outOfBounds(pos):
            return False
        if inCheck(self):
            return False

    def isLineValid(self, changeInX, changeInY, range):
        if (range == 0): range = 9
        validSquares = []
        newPos = self.position
        newPos[0] + changeInX
        newPos[1] + changeInY
        count = 0
        while isSquareValid(newPos) and count < range:
            validSquares.append()
            newPos[0] + changeInX
            newPos[1] + changeInY

class Pawn(Piece):
    pass

class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

board = Board()
board.populateSquares()
for s in range(64):
    square = board.squares[s]
    if (square.position[1] == 7):
        print(square.color[0] + ' ')
    else:
        print(square.color[0] + ' ', end = "")
