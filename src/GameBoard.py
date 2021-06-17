import pygame
from itertools import islice
from gamePiece import gamePiece
from ColorsFontsImages import ColorsFontsImages as asset

class GameBoard:
    HORIZONTALLINE1 = (asset.white, [55, 220, 390, 20], 0, 10)
    HORIZONTALLINE2 = (asset.white, [55, 330, 390, 20], 0, 10)
    VERTICALLINE1 = (asset.white, [175, 115, 20, 350], 0, 10)
    VERTICALLINE2 = (asset.white, [295, 115, 20, 350], 0, 10)

    LINELIST = (HORIZONTALLINE1, HORIZONTALLINE2, VERTICALLINE1, VERTICALLINE2)

    GAMEPIECEPOS = ((125, 245, 365), (175, 285, 395))

    def __init__(self, screen, colorX, colorO):
        self.screen = screen
        self.colorX = colorX
        self.colorO = colorO
        self.gridDisplay = []
        for i in GameBoard.LINELIST:
            self.gridDisplay.append((self.screen, i[0], i[1], i[2], i[3]))
        self.gridValues = {}
        self.gamePieces = {}
        self.gridFaces = [["", "", ""], ["", "", ""], ["", "", ""]]
        for i in range(3):
            gPosX = GameBoard.GAMEPIECEPOS[0][i]
            for j in range(3):
                gPosY = GameBoard.GAMEPIECEPOS[1][j]
                self.gridValues[(i, j)] = (0)
                self.gamePieces[(i, j)] = gamePiece(self.screen, gamePiece.XFACE, asset.white, gamePiece.SIZELARGE, gPosX, gPosY)
        self.turn = 0

    def show(self):
        for i in self.gridDisplay:
            pygame.draw.rect(i[0], i[1], i[2], i[3], i[4])
        for gridPos in self.gridValues:
            if self.gridValues[gridPos] != (0):
                self.gamePieces[gridPos].show()

    def updateBoard(self, pos, face, size):
        if self.gridValues[pos] >= size:
            return False
        self.gridValues[pos] = size
        piece = self.gamePieces[pos]
        piece.setSize(size)
        piece.setFace(face)
        if face == gamePiece.XFACE:
            piece.setColor(self.colorX)
            self.gridFaces[pos[1]][pos[0]] = "X"
        else:
            piece.setColor(self.colorO)
            self.gridFaces[pos[1]][pos[0]] = "O"
        return True

    def checkWinner(self):
        return checkWinner(self.gridFaces)

    def isHovering(self):
        return False

    def toString(self):
        return "Only here to satisfy buttonAssets class"


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
            num += board[i].count("")

        if num == 0:
            return "full"
        else:
            return "no_win"


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
