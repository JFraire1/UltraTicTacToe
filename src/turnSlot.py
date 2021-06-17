import pygame
from ColorsFontsImages import ColorsFontsImages as asset
import random


class turnSlot:
    ALIGNMENTCENTER = 1

    P2SELECT = 0
    P1SELECT = 7

    def __init__(self, screen, x, y, hasOutline=False, outLineWidth=4, outLineColor=asset.neonPink):
        self.screen = screen
        self.pos = x, y
        self.index = 7
        self.result = self.index
        self.lastChanged = 0
        self.isSpinning = False
        self.animation = []
        for i in asset.slotAnimationList:
            self.animation.append(pygame.image.load(i))
        self.rollCounter = 0
        self.doneSpinning = False
        self.hasOutline = hasOutline
        self.outLineWidth = outLineWidth
        self.outLineColor = outLineColor
        self.flash = 0

    def valueUpdated(self):
        self.doneSpinning = False

    def spin(self):
        self.isSpinning = True
        self._setResult()

    def _setResult(self):
        self.result = random.choice((turnSlot.P1SELECT, turnSlot.P2SELECT))

    def isHovering(self):
        return False

    def show(self):
        if self.isSpinning:
            if self.result == self.index:
                if self.rollCounter <= 230:
                    self._spinShow()
                    self.rollCounter += 1
                else:
                    self.rollCounter = 0
                    self.isSpinning = False
                    self.doneSpinning = True
            else:
                if self.rollCounter <= 420:
                    self._spinShow()
                    self.rollCounter += 1
                else:
                    self.rollCounter = 0
                    self.isSpinning = False
                    self.doneSpinning = True
            return
        self.screen.blit(self.animation[self.index], self.pos)
        if self.hasOutline:
            pygame.draw.rect(self.screen, self.outLineColor, [self.pos[0] - 6, self.pos[1] - 6, 62, 62],
                             self.outLineWidth)

    def _spinShow(self):
        self.index += 1
        self.index %= len(self.animation)
        self.screen.blit(self.animation[self.index], self.pos)
        if self.hasOutline:
            pygame.draw.rect(self.screen, asset.neonPink, [self.pos[0] - 5, self.pos[1] - 5, 60, 60],
                             self.outLineWidth)

    def toString(self):
        return "Only here to work with buttonAssets class"
