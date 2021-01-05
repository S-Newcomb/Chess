#Hopefully a fully working chess game built from scratch in python

class Board:
    #A class to represent the chess board
    squares = []

    def populateSquares(self):
       # print("here")
        for row in range(8):
            for col in range(8):
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
                
                self.squares.append(Square(pos, occ, color))

class Square(Board):
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

board = Board()
board.populateSquares()
for square in board.squares:
    if (square.position[1] == 7):
        print(square.color[0] + ' ')
    else:
        print(square.color[0] + ' ', end = "")
