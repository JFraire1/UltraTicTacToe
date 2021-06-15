import pygame
from ColorsFontsImages import ColorsFontsImages as asset

class colorPicker:
    LEFTBOUND = 0
    RIGHTBOUND = 1
    UPPERBOUND = 2
    LOWERBOUND = 3

    def __init__(self, screen, color=asset.red, x=0, y=0, size=10, hasOutline=True, outLineWidth=3,
                 outlineColor=asset.white, enlargeAmount=2, selectColor=asset.white, isSelected=False, selectable=True):
        self.screen = screen
        self.pos = x, y
        self.color = color
        self.size = size
        self.hasOutline = hasOutline
        self.outLineWidth = outLineWidth
        self.outlineColor = outlineColor
        self.bounds = self._getBounds()
        self.enlargeAmount = enlargeAmount
        self.selectColor = selectColor
        self.isSelected = isSelected
        self.selectable = selectable

    def setSelected(self, switch):
        if self.selectable:
            self.isSelected = switch

    def setSelectable(self, switch):
        self.selectable = switch

    def _getBounds(self):
        return self.pos[0] - self.size, self.pos[0] + self.size, self.pos[1] - self.size, self.pos[1] + self.size

    def getColor(self):
        return self.color

    def isHovering(self, mousePos=None):
        if mousePos == None:
            mousePos = pygame.mouse.get_pos()
        if (self.bounds[colorPicker.LEFTBOUND] <= mousePos[0] <= self.bounds[colorPicker.RIGHTBOUND]
                and self.bounds[colorPicker.UPPERBOUND] <= mousePos[1] <= self.bounds[colorPicker.LOWERBOUND]):
            return True

    def show(self):
        tempSize = self.size
        if not self.selectable:
            self.unSelectableShow()
            return
        tempLineColor = self.outlineColor
        self.selectedShow()
        pygame.draw.circle(self.screen, self.color, self.pos, self.size)
        if self.hasOutline:
            pygame.draw.circle(self.screen, self.outlineColor, self.pos, self.size, self.outLineWidth)
        self.outlineColor = tempLineColor
        self.size = tempSize

    def hoverShow(self):
        tempLineColor = self.outlineColor
        tempSize = self.size
        if not self.isSelected:
            self.size += self.enlargeAmount
        self.show()
        self.size = tempSize
        self.outlineColor = tempLineColor

    def selectedShow(self):
        if self.isSelected:
            self.outlineColor = self.selectColor
            self.size += self.enlargeAmount
            return True
        return False

    def unSelectableShow(self):
        pygame.draw.circle(self.screen, asset.gray, self.pos, self.size)
        if self.hasOutline:
            pygame.draw.circle(self.screen, asset.lightGray, self.pos, self.size, self.outLineWidth)

    def toString(self):
        attributes = (self.color, self.pos, self.size, self.hasOutline, self.outLineWidth,
                      self.outlineColor, self.bounds, self.enlargeAmount)
        string = ""
        for i in attributes:
            string += str(i) + "-"
        return string
