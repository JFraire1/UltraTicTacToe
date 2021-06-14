import pygame


class textFormat:
    ALIGNMENTLEFT = 1
    ALIGNMENTCENTER = 2
    ALIGNMENTRIGHT = 3

    ALIGNMENTTOP = 1
    ALIGNMENTBOTTOM = 3

    ALIGNMENTNONE = -1

    ENLARGENOMOVEMENT = 0
    ENLARGELEFT = 1
    ENLARGERIGHT = 2

    def __init__(self, screen, text="Hello", hasSurroundRect=False, verticalPadding=0, horizontalPadding=0,
                 rectLineWidth=0, useBackColor=False, backColor=(0, 0, 0), rectHeight=-1, rectWidth=-1,
                 font=("Corbel", 35), x=0, y=0,
                 color=(255, 255, 255), rectColor=(100, 100, 100), hoverBrightness=50, enlargeAmount=0,
                 horizontalAlignment=-1, verticalAlignment=-1, directionEnlarge=ENLARGENOMOVEMENT):
        self.screen = screen
        self.textString = text
        self.rectHeight = rectHeight
        self.rectLineWidth = rectLineWidth
        self.hasSurroundRect = hasSurroundRect
        self.verticalPadding = verticalPadding
        self.horizontalPadding = horizontalPadding
        self.rectHeight = rectHeight
        self.rectWidth = rectWidth
        self.textPos = (x, y)
        self.textColor = color
        self.rectColor = rectColor
        self.useBackColor = useBackColor
        self.backColor = backColor
        self.hoverBrightness = hoverBrightness
        self.font = font
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.outText = self.rectTextSize()
        self.rectPos = self.reposition()
        self.rectLeftBound = self.rectPos[0]
        self.rectRightBound = self.rectPos[0] + self.rectWidth
        self.rectUpperBound = self.rectPos[1]
        self.rectLowerBound = self.rectPos[1] + self.rectHeight
        self.enlargeAmount = enlargeAmount
        self.directionEnlarge = directionEnlarge

    def setBounds(self, rectPos):
        self.rectLeftBound = rectPos[0]
        self.rectRightBound = rectPos[0] + self.rectWidth
        self.rectUpperBound = rectPos[1]
        self.rectLowerBound = rectPos[1] + self.rectHeight

    def reposition(self):
        if self.horizontalAlignment > 0:
            if self.horizontalAlignment == self.ALIGNMENTLEFT:
                self.textPos = (0, self.textPos[1])
            if self.horizontalAlignment == self.ALIGNMENTCENTER:
                self.textPos = ((self.screen.get_width() - self.outText.get_width()) / 2, self.textPos[1])
            if self.horizontalAlignment == self.ALIGNMENTRIGHT:
                self.textPos = (self.screen.get_width() - self.outText.get_width(), self.textPos[1])
        if self.verticalAlignment > 0:
            if self.verticalAlignment == self.ALIGNMENTTOP:
                self.textPos = (self.textPos[0], 0)
            if self.verticalAlignment == self.ALIGNMENTCENTER:
                self.textPos = (self.textPos[0], (self.screen.get_height() - self.outText.get_height()) / 2)
            if self.verticalAlignment == self.ALIGNMENTBOTTOM:
                self.textPos = (self.textPos[0], self.screen.get_height() - self.outText.get_height())
        rectPos = self.textPos
        rectPos = (rectPos[0] + self.outText.get_width() / 2 - self.rectWidth / 2,
                   rectPos[1] + self.outText.get_height() / 2 - self.rectHeight / 2)
        self.setBounds(rectPos)
        return rectPos

    def rectTextSize(self):
        if "\\" in self.font[0]:
            outText = pygame.font.Font(self.font[0], self.font[1]).render(self.textString, True, self.textColor)
        else:
            outText = pygame.font.SysFont(self.font[0], self.font[1]).render(self.textString, True, self.textColor)
        if self.rectHeight < 0:
            if self.verticalPadding > 0:
                self.rectHeight = outText.get_height() + self.verticalPadding
            else:
                self.rectHeight = outText.get_height()
        if self.rectWidth < 0:
            if self.horizontalPadding > 0:
                self.rectWidth = outText.get_width() + self.horizontalPadding
            else:
                self.rectWidth = outText.get_width()
        return outText

    def textSize(self):
        if "\\" in self.font[0]:
            outText = pygame.font.Font(self.font[0], self.font[1]).render(self.textString, True, self.textColor)
        else:
            outText = pygame.font.SysFont(self.font[0], self.font[1]).render(self.textString, True, self.textColor)
        return outText

    def rectSize(self):
        if self.verticalPadding >= 0:
            self.rectHeight = self.outText.get_height() + self.verticalPadding
        elif self.rectHeight < 0:
            self.rectHeight = self.outText.get_height()
        if self.horizontalPadding >= 0:
            self.rectWidth = self.outText.get_width() + self.horizontalPadding
        elif self.rectWidth < 0:
            self.rectWidth = self.outText.get_width()

    def setHasSurroundRect(self, switch):
        self.hasSurroundRect = switch

    def setUseBackColor(self, switch):
        self.useBackColor = switch

    def setText(self, textString):
        self.textString = textString
        self.outText = self.textSize()
        self.rectSize()
        self.rectPos = self.reposition()

    def setFontHeight(self, fontHeight):
        self.font = (self.font[0], fontHeight)
        self.outText = self.textSize()
        self.rectSize()
        self.rectPos = self.reposition()

    def setFont(self, fontName):
        self.font = (fontName, self.font[1])
        self.outText = self.textSize()
        self.rectSize()
        self.rectPos = self.reposition()

    def setRectHeight(self, rectHeight):
        self.verticalPadding = -1
        self.rectHeight = rectHeight
        self.rectPos = self.reposition()

    def setRectWidth(self, rectWidth):
        self.horizontalPadding = -1
        self.rectWidth = rectWidth
        self.rectPos = self.reposition()

    def setRectLineWidth(self, lineWidth):
        self.rectLineWidth = lineWidth

    def setHorizontalPadding(self, horizontalPadding):
        self.horizontalPadding = horizontalPadding
        self.rectSize()
        self.rectPos = self.reposition()

    def setVerticalPadding(self, verticalPadding):
        self.verticalPadding = verticalPadding
        self.rectSize()
        self.rectPos = self.reposition()

    def setX(self, x):
        self.textPos = (x, self.textPos[1])
        self.rectPos = self.reposition()

    def setY(self, y):
        self.textPos = (self.textPos[0], y)
        self.rectPos = self.reposition()

    def setPos(self, x, y):
        self.textX = x
        self.textY = y
        self.rectPos = self.reposition()

    def setHorizontalAlignment(self, alignment):
        self.horizontalAlignment = alignment
        self.rectPos = self.reposition()

    def setVerticalAlignment(self, alignment):
        self.verticalAlignment = alignment
        self.rectPos = self.reposition()

    def setTextColor(self, color):
        self.textColor = color
        self.outText = self.rectTextSize()

    def setBackColor(self, color):
        self.backColor = color

    def setRectColor(self, color):
        self.rectColor = color

    def setHoverBrightness(self, amount):
        self.hoverBrightness = amount

    def setEnlargeAmount(self, amount):
        self.enlargeAmount = amount

    def show(self):
        if self.hasSurroundRect:
            if self.useBackColor:
                pygame.draw.rect(self.screen, self.backColor,
                                 [self.rectPos[0], self.rectPos[1], self.rectWidth, self.rectHeight])
            pygame.draw.rect(self.screen, self.rectColor,
                             [self.rectPos[0], self.rectPos[1], self.rectWidth, self.rectHeight], self.rectLineWidth)
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
        self.screen.blit(self.outText, self.textPos)
        self.font = tempFont
        self.outText = self.textSize()
        self.rectWidth = tempRectWidth
        self.rectHeight = tempRectHeight
        self.textPos = tempTextPos
        self.rectPos = self.reposition()

    def isHovering(self, mousePos=None):
        if mousePos is None:
            mousePos = pygame.mouse.get_pos()
        if self.rectLeftBound <= mousePos[0] <= self.rectRightBound and self.rectUpperBound <= mousePos[1] <= self.rectLowerBound:
            return True

    def checkBackColor(self):
        if self.useBackColor:
            pygame.draw.rect(self.screen, self.backColor,
                             [self.rectPos[0], self.rectPos[1], self.rectWidth, self.rectHeight])

    def highlightColor(self):
        tempColor = []
        for i in range(3):
            if self.hoverBrightness > 0:
                if self.rectColor[i] + self.hoverBrightness >= 255:
                    tempColor.append(255)
                else:
                    tempColor.append(self.rectColor[i] + self.hoverBrightness)
            elif self.rectColor[i] + self.hoverBrightness <= 0:
                tempColor.append(0)
            else:
                tempColor.append(self.rectColor[i] + self.hoverBrightness)
        return tempColor

    def highlightEnlarge(self):
        self.font = (self.font[0], self.font[1] + self.enlargeAmount)
        oldTextWidth = self.outText.get_width()
        oldTextHeight = self.outText.get_height()
        self.outText = self.textSize()
        diffWidth = self.outText.get_width() - oldTextWidth
        diffHeight = self.outText.get_height() - oldTextHeight
        self.rectWidth += diffWidth
        self.rectHeight += diffHeight
        if self.directionEnlarge == textFormat.ENLARGENOMOVEMENT:
            self.textPos = (self.textPos[0] - diffWidth / 2, self.textPos[1] - diffHeight / 2)
        elif self.directionEnlarge == textFormat.ENLARGELEFT:
            self.textPos = (self.textPos[0] - diffWidth , self.textPos[1])
        self.rectPos = self.reposition()

    def toString(self):
        attributes = (self.textString, self.rectHeight, self.rectLineWidth, self.hasSurroundRect, self.rectWidth, self.textPos, self.textColor,
                      self.rectColor, self.useBackColor, self.backColor, self.hoverBrightness, self.font, self.horizontalAlignment,
                      self.verticalAlignment, self.outText, self.rectPos)
        string = ""
        for i in attributes:
            string += str(i)
        return string
