import pygame
from ColorsFontsImages import ColorsFontsImages as asset


class Slider:
    DRAGCIRCLE = 1
    DRAGRECTANGLE = 2

    LEFTBOUND = 0
    RIGHTBOUND = 1
    UPPERBOUND = 2
    LOWERBOUND = 3

    ALIGNMENTLEFT = 0
    ALIGNMENTCENTER = 1
    ALIGNMENTRIGHT = 2

    ALIGNMENTTOP = 0
    ALIGNMENTBOTTOM = 2

    def __init__(self, screen, x=0, y=0, HorizontalAlignment=-1, VerticalAlignment=-1, barColor=asset.white,
                 emptyBarColor=asset.black, hasOutline=True, outlineColor=asset.gray, barWidth=360, barHeight=5,
                 dragShape=DRAGRECTANGLE, dragColor=asset.white, dragWidth=10, dragHeight=7, dragSize=8,
                 defaultValue=1.0, outLineWidth=1, enlargeAmount=0):
        self.screen = screen
        self.horizontalAlignment = HorizontalAlignment
        self.verticalAlignment = VerticalAlignment
        self.pos = (x, y)
        self.barColor = barColor
        self.emptyBarColor = emptyBarColor
        self.hasOutline = hasOutline  # draws a separate rectangle only outline
        self.outlineColor = outlineColor
        self.barWidth = barWidth
        self.barHeight = barHeight
        self.dragShape = dragShape
        self.dragWidth = dragWidth
        self.dragHeight = dragHeight
        self.dragSize = dragSize
        self.value = defaultValue
        self.dragPos = self._setDragPos()
        self.dragY = self._setDragY()
        self._setPos()
        self.barBounds = self._setBarBounds()  # use bound constants to access
        self.dragBounds = self._setDragBounds()  # use bound constants to access
        self.outLineWidth = outLineWidth
        self.dragColor = dragColor
        self.enlargeAmount = enlargeAmount
        self.beingDragged = False

    def _setPos(self):
        if self.horizontalAlignment > 0:
            if self.horizontalAlignment == self.ALIGNMENTLEFT:
                self.pos = (0, self.pos[1])
            if self.horizontalAlignment == self.ALIGNMENTCENTER:
                self.pos = ((self.screen.get_width() - self.barWidth) / 2, self.pos[1])
            if self.horizontalAlignment == self.ALIGNMENTRIGHT:
                self.pos = (self.screen.get_width() - self.barWidth - self.dragWidth / 2, self.pos[1])
        if self.verticalAlignment > 0:
            if self.verticalAlignment == self.ALIGNMENTTOP:
                self.pos = (self.pos[0], 0)
            if self.verticalAlignment == self.ALIGNMENTCENTER:
                self.pos = (self.pos[0], (self.screen.get_height() - self.barHeight) / 2)
            if self.verticalAlignment == self.ALIGNMENTBOTTOM:
                self.pos = (self.pos[0], self.screen.get_height() - self.barHeight)

    def _setDragY(self):  # inside use only
        if self.dragShape == Slider.DRAGRECTANGLE:
            return self._getMidY() - self.dragHeight / 2
        else:
            return self._getMidY() - self.dragSize / 2

    def _getMidY(self):  # inside use only
        return self.pos[1] + self.barHeight / 2

    def _setBarBounds(self):  # inside use
        return self.pos[0], self.pos[0] + self.barWidth, self.pos[1], self.pos[1] + self.barHeight

    def _setDragBounds(self):  # inside use
        if self.dragShape == Slider.DRAGRECTANGLE:
            return self.dragPos, self.dragPos + self.dragWidth, self.dragY, self.dragY + self.dragHeight
        else:
            return self.dragPos - self.dragSize, self.dragPos + self.dragSize, self._getMidY() - self.dragSize, self._getMidY() + self.dragSize

    def _setDragPos(self):  # inside use only
        if self.dragShape == Slider.DRAGRECTANGLE:
            return (self.pos[0] + self.value * self.barWidth) - self.dragWidth / 2
        else:
            return (self.pos[0] + self.value * self.barWidth) - self.dragSize / 2

    def setValue(self, mousePos=None):  # outside use,use when clicked, dragged
        if mousePos is None:
            mousePos = pygame.mouse.get_pos()
        self.value = (mousePos[0] - self.pos[0]) / self.barWidth
        if self.value > 1.0:
            self.value = 1.0
        if self.value < 0.0:
            self.value = 0.0
        self.dragPos = self._setDragPos()
        self.dragBounds = self._setDragBounds()

    def setValueInit(self, vol):
        self.value = vol
        self.dragPos = self._setDragPos()
        self.dragBounds = self._setDragBounds()

    def setDragged(self, switch):
        self.beingDragged = switch

    def isHovering(self, mousePos=None):  # used in buttonAssets to check if mouse hovering
        if mousePos is None:
            mousePos = pygame.mouse.get_pos()
        if self.beingDragged:
            return True
        elif (self.dragBounds[Slider.LEFTBOUND] <= mousePos[0] <= self.dragBounds[Slider.RIGHTBOUND]
            and self.dragBounds[Slider.UPPERBOUND] <= mousePos[1] <= self.dragBounds[Slider.LOWERBOUND]) \
                or (self.barBounds[Slider.LEFTBOUND] <= mousePos[0] <= self.barBounds[Slider.RIGHTBOUND]
                    and self.barBounds[Slider.UPPERBOUND] <= mousePos[1] <= self.barBounds[Slider.LOWERBOUND]):
            return True

    def highlightEnlarge(self):
        self.dragWidth += self.enlargeAmount
        self.dragHeight += self.enlargeAmount
        self.dragSize += self.enlargeAmount
        if self.dragShape == Slider.DRAGRECTANGLE:
            self.dragPos = self.dragPos - self.enlargeAmount / 2
            self.dragY = self.dragY - self.enlargeAmount / 2

    def hoverShow(self):
        tempDragPos = self.dragPos
        tempDragY = self.dragY
        tempDragSize = self.dragSize
        tempDragHeight = self.dragHeight
        tempDragWidth = self.dragWidth
        self.highlightEnlarge()
        pygame.draw.rect(self.screen, self.emptyBarColor, [self.pos[0], self.pos[1], self.barWidth, self.barHeight])
        pygame.draw.rect(self.screen, self.barColor,
                         [self.pos[0], self.pos[1], self.barWidth * self.value, self.barHeight])
        if self.hasOutline:
            pygame.draw.rect(self.screen, self.outlineColor, [self.pos[0], self.pos[1], self.barWidth, self.barHeight],
                             self.outLineWidth)
        if self.dragShape == Slider.DRAGRECTANGLE:
            pygame.draw.rect(self.screen, self.dragColor, [self.dragPos, self.dragY, self.dragWidth, self.dragHeight])
        if self.dragShape == Slider.DRAGCIRCLE:
            pygame.draw.circle(self.screen, self.dragColor, (self.dragPos, self._getMidY()), self.dragSize)
        self.dragPos = tempDragPos
        self.dragY = tempDragY
        self.dragSize = tempDragSize
        self.dragHeight = tempDragHeight
        self.dragWidth = tempDragWidth

    def show(self):
        if self.beingDragged:
            self.hoverShow()
        pygame.draw.rect(self.screen, self.emptyBarColor, [self.pos[0], self.pos[1], self.barWidth, self.barHeight])
        pygame.draw.rect(self.screen, self.barColor,
                         [self.pos[0], self.pos[1], int(self.barWidth * self.value), self.barHeight])
        if self.hasOutline:
            pygame.draw.rect(self.screen, self.outlineColor, [self.pos[0], self.pos[1], self.barWidth, self.barHeight],
                             self.outLineWidth)
        if self.dragShape == Slider.DRAGRECTANGLE:
            pygame.draw.rect(self.screen, self.dragColor, [self.dragPos, self.dragY, self.dragWidth, self.dragHeight])
        if self.dragShape == Slider.DRAGCIRCLE:
            pygame.draw.circle(self.screen, self.dragColor, (self.dragPos, self._getMidY()), self.dragSize)

    def toString(self):
        attributes = (self.pos, self.barColor, self.emptyBarColor, self.hasOutline, self.outlineColor,
                      self.barWidth, self.barHeight, self.dragShape, self.dragWidth, self.dragHeight,
                      self.dragSize, self.value, self.dragPos, self.dragY, self.barBounds, self.dragBounds,
                      self.outLineWidth, self.dragColor)
        string = ""
        for i in attributes:
            string += str(i)
        return string
