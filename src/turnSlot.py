import pygame
from ColorsFontsImages import ColorsFontsImages as asset
import random


class turnSlot:
    ALIGNMENTCENTER = 1

    P2SELECT = 7
    P1SELECT = 0

    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = x, y
        self.index = 0
        self.result = self.index
        self.lastChanged = 0
        self.isSpinning = False
        self.animation = []
        for i in asset.slotAnimationList:
            self.animation.append(pygame.image.load(i))
        self.rollCounter = 0
        self.doneSpinning = False

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

    def _spinShow(self):
        self.index += 1
        self.index %= len(self.animation)
        self.screen.blit(self.animation[self.index], self.pos)

    def toString(self):
        return "None rn lol"
