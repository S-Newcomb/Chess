#Hopefully a fully working chess game built from scratch in python

class Board:
    #A class to represent the chess board
    squares = {}

    def populateSquares(self):
       # print("here")
        for x in range(8):
            for y in range(8):
                number = x * 8 + y
                pos = [x, y]
                
                if (y == 1):
                    occ = Pawn(pos,"White")
                elif (y == 6):
                    occ = Pawn(pos,"Black")
                elif (y == 0):
                    occ = self.populateKingRow(0,pos,"White")
                elif (y == 7):
                    occ = self.populateKingRow(7,pos,"Black")
                else: 
                    occ = None                    

                #Even rows have black - white pattern
                if (x % 2 ==  0):
                    if (y % 2 == 0):
                        color = "Black"
                    else: color = "White"
                #Odd rows have white - black pattern
                else: 
                    if (y % 2 == 0):
                        color = "White"
                    else: color = "Black"
                
                self.squares[number] = (Square(pos, occ, color))

    #Populates given row with classic pieces (non pawns)
    def populateKingRow(self, row, pos, color):
        if (pos[1] == row):
            if (pos[0] == 0 or pos[0] == 7):
                return Rook(pos, color)
            elif (pos[0] == 1 or pos[0] == 6):
                return Knight(pos, color)
            elif (pos[0] == 2 or pos[0] == 5):
                return Bishop(pos, color)
            elif (pos[0] == 3):
                return Queen(pos, color)
            else:
                return King(pos, color)



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
        
        #Pawns cannot attack up
        if (piece != None and self.name == "Pawn" and piece.position[0] == self.position[0]):
            return False
        #Pawns cannot move diagonally unless capturing
        if (piece == None and self.name == "Pawn" and 
        (square.position[0] == self.position[0] + 1 or square.position[0] == self.position[0] - 1)):
            return False
        
        return True
        
    """ Checks whether every square in a line determined by change in x and y is valid """
    def isLineValid(self, board, changeInX, changeInY, range):
        if (range == 0): range = 7
        validSquares = []
        newPos = self.position.copy()
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

    """Lots to do here:
        - Handle taken pieces """

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
        else: 
            print("Not a valid move")

#TODO: Allow Pawns to move 2 spaces on first move, check position pawn is moving from
class Pawn(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col   
        self.name = "Pawn"

    def getValidMoves(self):
        validMoves = []
        #Up or forward depends on color
        if (self.color == "White"):
            up = 1
        else:
            up = -1
        #If the pawn has not moved
        if ((self.color == "White" and self.position[1] == 1) or
            (self.color == "Black" and self.position[1] == 6)):
            validMoves.extend(super().isLineValid(board, 0, up, 2))  #Can move up 2 
        else:
            validMoves.extend(super().isLineValid(board, 0, up, 1))  #Up
        validMoves.extend(super().isLineValid(board, 1, up, 1))  #Right Diagonal
        validMoves.extend(super().isLineValid(board, -1, up, 1)) #Left Diagonal
        return validMoves

class Rook(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "Rook"

    def getValidMoves(self):
        validMoves = []
        validMoves.extend(super().isLineValid(board, 1, 0, 0))  #Right
        validMoves.extend(super().isLineValid(board, -1, 0, 0)) #Left
        validMoves.extend(super().isLineValid(board, 0, 1, 0))  #Up
        validMoves.extend(super().isLineValid(board, 0, -1, 0)) #Down
        return validMoves

class Knight(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "Knight"

class Bishop(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "Bishop"

    def getValidMoves(self):
        validMoves = []
        validMoves.extend(super().isLineValid(board, 1, 1, 0))  #Right Forward Diag
        validMoves.extend(super().isLineValid(board, -1, 1, 0)) #Left Forward Diag
        validMoves.extend(super().isLineValid(board, 1, -1, 0)) #Right Back Diag
        validMoves.extend(super().isLineValid(board, -1, -1, 0)) #Left Back Diag
        return validMoves

class Queen(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "Queen"

    def getValidMoves(self):
        validMoves = []
        validMoves.extend(super().isLineValid(board, 1, 0, 0))  #Right
        validMoves.extend(super().isLineValid(board, -1, 0, 0)) #Left
        validMoves.extend(super().isLineValid(board, 0, 1, 0))  #Up
        validMoves.extend(super().isLineValid(board, 0, -1, 0)) #Down
        validMoves.extend(super().isLineValid(board, 1, 1, 0))  #Right Forward Diag
        validMoves.extend(super().isLineValid(board, -1, 1, 0)) #Left Forward Diag
        validMoves.extend(super().isLineValid(board, 1, -1, 0)) #Right Back Diag
        validMoves.extend(super().isLineValid(board, -1, -1, 0)) #Left Back Diag
        return validMoves

class King(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "King"

def drawBoard(board):
    for y in range(8):
        print("")
        for x in range(8):
            invrow = 7-y
            square = board.getSquareAtPos([x, invrow])
            if (square.occupied == None):
                print("|  " + square.color[0] + '  |', end = "")
            else:
                print("|" + square.occupied.name[0:4] + ' |', end = "")
    print("")



board = Board()
board.populateSquares()
drawBoard(board)
testPawn = board.getPieceAtPos([3, 6])
testPawn.move(board, board.getSquareAtPos([3,4]))
drawBoard(board)
testQueen = board.getPieceAtPos([3,7])
testQueen.move(board, board.getSquareAtPos([3,5]))
drawBoard(board)
testQueen.move(board, board.getSquareAtPos([7,1]))
drawBoard(board)



# testRook = board.getPieceAtPos([0,1])
# testRook.move(board, board.getSquareAtPos([0,6]))
# drawBoard(board)

# drawBoard(board)
# testPawn2 = board.getPieceAtPos([1, 6])
# testPawn2.move(board, board.getSquareAtPos([1,4]))
# drawBoard(board)