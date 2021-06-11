from textFormat import textFormat
import pygame
from ColorsFontsImages import ColorsFontsImages as asset

class checkBox(textFormat):
    def __init__(self, screen, isCheckedByDefault=False, text="X", hasSurroundRect=True, verticalPadding=-1,
                 horizontalPadding=-1, rectLineWidth=1, useBackColor=True, backColor=asset.white, rectHeight=20,
                 rectWidth=20, font=("Corbel", 15), x=0, y=0, color=asset.black, rectColor=asset.black,
                 hoverBrightness=-20, enlargeAmount=3, horizontalAlignment=-1, verticalAlignment=-1):
        super().__init__(screen, text, hasSurroundRect, verticalPadding, horizontalPadding, rectLineWidth,
                         useBackColor, backColor, rectHeight, rectWidth, font, x, y, color, rectColor, hoverBrightness,
                         enlargeAmount, horizontalAlignment, verticalAlignment)
        self.checked = isCheckedByDefault

    def show(self):
        if self.hasSurroundRect:
            if self.useBackColor:
                pygame.draw.rect(self.screen, self.backColor,
                                 [self.rectPos[0], self.rectPos[1], self.rectWidth, self.rectHeight])
            pygame.draw.rect(self.screen, self.rectColor,
                             [self.rectPos[0], self.rectPos[1], self.rectWidth, self.rectHeight], self.rectLineWidth)
        if self.checked:
            self.screen.blit(self.outText, self.textPos)

    def hoverShow(self):
        tempFont = self.font
        tempRectHeight = self.rectHeight
        tempRectWidth = self.rectWidth
        tempTextPos = self.textPos
        if self.enlargeAmount != 0:
            self.highlightEnlarge()
        if self.hasSurroundRect:
            self.checkBackColor()
            tempColor = self.highlightColor()
            pygame.draw.rect(self.screen, (tempColor[0], tempColor[1], tempColor[2]),
                             [self.rectPos[0], self.rectPos[1], self.rectWidth, self.rectHeight], self.rectLineWidth)
        if self.checked:
            self.screen.blit(self.outText, self.textPos)
        self.font = tempFont
        self.outText = self.textSize()
        self.rectWidth = tempRectWidth
        self.rectHeight = tempRectHeight
        self.textPos = tempTextPos
        self.rectPos = self.reposition()

    def check(self, check):
        self.checked = check




