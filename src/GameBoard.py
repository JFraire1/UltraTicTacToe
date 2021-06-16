from itertools import islice
import pygame
from ColorsFontsImages import ColorsFontsImages as asset
from gamePiece import gamePiece

class GameBoard:
    HORIZONTALLINE1 = (asset.white, [37.5, 100, 400, 20], 0, 10)
    HORIZONTALLINE2 = (asset.white, [37.5, 400, 400, 20], 0, 10)
    VERTICALLINE1 = (asset.white, [50, 100, 20, 400], 0, 10)
    VERTICALLINE2 = (asset.white, [50, 375, 20, 400], 0, 10)
    # todo update with actual positions and sizes

    LINELIST = (HORIZONTALLINE1, HORIZONTALLINE2, VERTICALLINE1, VERTICALLINE2)

    GAMEPIECEPOS = ((20, 50, 70), (90, 120, 150)) # todo update with actual positions

    def __init__(self, screen, colorX, colorO):
        self.screen = screen
        self.colorX = colorX
        self.colorO = colorO
        self.gridDisplay = []
        for i in LINELIST:
            self.gridDisplay.append((self.screen, i[0], i[1], i[2], i[3]))
        self.gridValues = {}
        self.gamePieces = {}
        for i in range(3):
            gPosX = GameBoard.GAMEPIECEPOS[0][i]
            for j in range(3):
                gPosY = GameBoard.GAMEPIECEPOS[1][j]
                self.gridValues[(i, j)] = ("", 0)
                self.gamePieces[(i, j)] = gamePiece(gamePiece.XFACE, colorX, gamePiece.SIZELARGE, gPosX, gPosY)
        self.turnCount = 0

    def iterateTurn(self):
        self.turnCount += 1
        # todo actually do something here? might not be needed

    def drawBoard(self):
        for i in self.gridDisplay:
            pygame.draw.rect(i[0], i[1], i[2], i[3], i[4])
        for gridPos in self.gridValues:
            if self.gridValues[gridPos] != ("", 0):
                self.gamePieces[gridPos].show()

    def updateBoard(self, pos, face, size):
        # todo this is looking kinda promising, actually
        # just make the board, see the position, (0,0) of the inserted piece,
        # its face, and double check to make sure the size is greater than the piece already there
        # find size of existing piece: self.gridValues[pos][1]
        # replace if need be self.gridValues[pos] = (face, size)
        # if need be, update size of piece at that position
        # x = self.gamePieces[pos]
        # x.setSize(size)
        # x.setFace(face)





def turn(board, num):
    if num % 2 == 1:
        print("Player X Turn")
        i = (int(input("Enter a row number:")) - 1)
        j = (int(input("Enter a column number:")) - 1)
        board[i][j] = "X"

    elif num % 2 == 0:
        print("Player O Turn")
        i = (int(input("Enter a row number:")) - 1)
        j = (int(input("Enter a column number:")) - 1)
        board[i][j] = "O"

    return board


def checkWinner(board):
    x_win = False
    o_win = False

    for i in range(len(board)):
        if board[i].count("X") == 3:
            return "x_win"
        elif board[i].count("O") == 3:
            return "o_win"

    columns = separateColumns(board)
    for i in range(len(columns)):
        if columns[i].count("X") == 3:
            return "x_win"
        elif columns[i].count("O") == 3:
            return "o_win"

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return "x_win"
        elif board[0][0] == "O":
            return "o_win"

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return "x_win"
        elif board[0][2] == "O":
            return "o_win"

    if x_win == False and o_win == False:
        num = 0
        for i in range(len(board)):
            num += board[i].count(" ")

        if num == 0:
            return "tie"
        else:
            return "unfinished"


def separateColumns(board):
    columns = []
    divisions = [3, 3, 3]
    for k in range(len(board[0])):
        for i in range(len(board)):
            columns.append(board[i][k])
    column = iter(columns)
    columns = [list(islice(column, elem))
               for elem in divisions]

    return columns
