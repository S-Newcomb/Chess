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

                if (row == 0 and col == 1):
                    occ = Rook(pos,"White")
                elif (row == 6 or row == 7):
                    occ = Rook(pos,"Black")
                else: 
                    occ = None                    

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

    def getSquareAtPos(self, pos):
        num = pos[0] * 8 + pos[1] 

        #If pos is out of bounds then return None
        if (num > 63 or num < 0):
            return None
        return self.squares[num]
    
    def getPieceAtPos(self, pos):
        square = self.getSquareAtPos(pos)
        return square.occupied

class Square:
        number = int
        position = [int, int]
        occupied = None
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
    name = str
    position = [int, int]
    color = str

    def __init__(self, pos, col):
        self.position = pos
        self.color = col

    def inCheck(self):
        pass

    """Checks that the square reached by pos is a valid square for this piece"""
    def isSquareValid(self, square):
        if square == None:
            return False

        """if inCheck(self):
            return False"""

        #Is that square occupied by another of your pieces?
        piece = square.occupied
        if (piece != None and piece.color == self.color):
            return False
        
        return True
        
    """ Checks whether every square in a line determined by change in x and y is valid """
    def isLineValid(self, board, changeInX, changeInY, range):
        if (range == 0): range = 7
        validSquares = []
        newPos = self.position
        newPos[0] += changeInX
        newPos[1] += changeInY
        count = 0
        while self.isSquareValid(board.getSquareAtPos(newPos)) and count < range:
            validSquares.append(board.getSquareAtPos(newPos))
            newPos[0] += changeInX
            newPos[1] += changeInY
            count += 1
        return validSquares

    #Should be implemented in all subclasses, is this necessary?
    def getValidMoves(self):
        pass
    
    def move(self, board, square):
        if (self == None):
            print("You can't move nothing!")
            return
        validMoves = self.getValidMoves()
        if square in validMoves:
            #Remove Piece from current square
            board.getSquareAtPos(self.position).occupied = None
            #Move Piece to new square
            self.position = square.position
            #Mark that square is occupied by this piece
            square.occupied = self


class Pawn(Piece):
    pass

class Rook(Piece):
    Piece.name = "Rook"

    def getValidMoves(self):
        validMoves = []
        validMoves.extend(super().isLineValid(board, 1, 0, 0))  #Right
        validMoves.extend(super().isLineValid(board, -1, 0, 0)) #Left
        validMoves.extend(super().isLineValid(board, 0, 1, 0))  #Up
        validMoves.extend(super().isLineValid(board, 0, -1, 0)) #Down
        return validMoves



class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

def drawBoard(board):
    for s in range(64):
        square = board.squares[s]
        if (square.position[1] == 7):
            if (square.occupied == None):
                print(square.color[0] + ' ')
            else:
                print(square.occupied.name + ' ')
        else:
            if (square.occupied == None):
                print(square.color[0] + ' ', end = "")
            else:
                print(square.occupied.name + ' ', end = "")


board = Board()
board.populateSquares()
drawBoard(board)
testPiece = board.getPieceAtPos([0,1])
testPiece.move(board, board.getSquareAtPos([5,1]))
print(testPiece.position)
drawBoard(board)
