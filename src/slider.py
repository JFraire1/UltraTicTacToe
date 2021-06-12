import pygame
from ColorsFontsImages import ColorsFontsImages as asset


class Slider:
    DRAGCIRCLE = 1
    DRAGRECTANGLE = 2
    DRAGSQUARE = 3
    DRAGPOLYGON = -1

    def __init__(self, screen, x=0, y=0, barColor=asset.white, emptyBarColor=asset.black, hasOutline=True,
                 outlineColor=asset.gray, barWidth=360, barHeight=5, dragShape=DRAGRECTANGLE, dragWidth=10,
                 dragHeight=7, dragSize=8, dragPoints=3, defaultValue = 1.0):
        self.screen = screen
        self.pos = (x, y)
        self.barColor = barColor
        self.emptyBarColor = emptyBarColor
        self.hasOutline = hasOutline
        self.outlineColor = outlineColor
        self.barWidth = barWidth
        self.barHeight = barHeight
        self.dragShape = dragShape
        self.dragWidth = dragWidth
        self.dragHeight = dragHeight
        self.dragSize = dragSize
        self.dragPoints = dragPoints
        self.value = defaultValue
        self.dragPos = self.setDragPos()

    def setDragPos(self):
        if self.dragShape == Slider.DRAGRECTANGLE:
            return (self.pos[0] + self.value * self.barWidth) - self.dragWidth / 2
        else:
            return (self.pos[0] + self.value * self.barWidth) - self.dragSize / 2

    def setValue(self):
        #todo
        #sets Value and updates dragPos
        pass

    def isHovering(self, mouse=None):
        #checks if mouse is hovering over any part of the slider
        pass

    def hoverShow(self):
        #show but makes dragShape big
        pass

    def show(self):
        #show normally
        pass


