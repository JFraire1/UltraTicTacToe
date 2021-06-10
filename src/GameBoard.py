from itertools import islice


class GameBoard:
    def __init__(self, screen):
        self.screen = screen
        self.gridValues = {}
        for i in range(3):
            for j in range(3):
                self.gridValues[(i, j)] = 0
        self.playGrid = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.turnCount = 0

    def iterateTurn(self):
        self.turnCount += 1



    def drawBoard(self):


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
