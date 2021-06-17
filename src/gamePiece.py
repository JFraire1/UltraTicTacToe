import pygame
from ColorsFontsImages import ColorsFontsImages as asset

class gamePiece:
    XFACE = 0
    OFACE = 1

    SIZESMALL = 15
    SIZEMEDIUM = 25
    SIZELARGE = 32

    LEFTBOUND = 0
    RIGHTBOUND = 1
    UPPERBOUND = 2
    LOWERBOUND = 3

    DEMOLIST = (15, 25, 35)

    def __init__(self, screen, face, color, size, x=0, y=0):
        self.pos = x, y
        self.screen = screen
        self.color = color
        self.size = size
        self.face = face
        self.text = self._setText()
        self.textPos = self._setTextPos()
        self.bounds = self._getBounds()
        self.i = self._findI()
        self.isBeingDragged = False

    def _setTextPos(self):
        return self.pos[0] - self.text.get_width() / 2, self.pos[1] - self.text.get_height() / 2

    def _findI(self):
        for i in range(len(gamePiece.DEMOLIST)):
            if gamePiece.DEMOLIST[i] == self.size:
                return i

    def _setText(self):
        if self.face == gamePiece.XFACE:
            return pygame.font.Font(asset.joystix, self.size).render("X", True, asset.black)
        else:
            return pygame.font.Font(asset.joystix, self.size).render("O", True, asset.black)

    def _getBounds(self):
        return self.pos[0] - self.size, self.pos[0] + self.size, self.pos[1] - self.size, self.pos[1] + self.size

    def setSize(self, size):
        self.size = size
        self.text = self._setText()
        self.textPos = self._setTextPos()

    def setBeingDragged(self, switch):
        self.isBeingDragged = switch

    def cycleSize(self):
        self.i += 1
        self.i %= len(gamePiece.DEMOLIST)
        self.size = gamePiece.DEMOLIST[self.i]
        self.text = self._setText()
        self.textPos = self._setTextPos()

    def isHovering(self):
        mousePos = pygame.mouse.get_pos()
        if (self.bounds[gamePiece.LEFTBOUND] <= mousePos[0] <= self.bounds[gamePiece.RIGHTBOUND]
                and self.bounds[gamePiece.UPPERBOUND] <= mousePos[1] <= self.bounds[gamePiece.LOWERBOUND]):
            return True

    def setPos(self, pos):
        self.pos = pos
        self.text = self._setText()
        self.textPos = self._setTextPos()


    def setColor(self, color):
        self.color = color

    def setFace(self, face):
        self.face = face
        self.text = self._setText()
        self.textPos = self._setTextPos()

    def show(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.size)
        self.screen.blit(self.text, self.textPos)

    def hoverShow(self):
        self.show()

    def toString(self):
        attributes = self.pos, self.screen, self.color, self.size, self.face
        string = ""
        for i in attributes:
            string += str(i)
        return string
