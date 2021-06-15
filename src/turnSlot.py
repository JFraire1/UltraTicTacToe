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

    def spin(self):
        self.isSpinning = True

    def _setResult(self):
        self.result = random.choice((turnSlot.P1SELECT, turnSlot.P2SELECT))

    def isHovering(self):
        return False

    def show(self):
        if self.isSpinning:
            self.animateSpin()
            return
        self.screen.blit(self.animation[self.index], self.pos)

    def animateSpin(self):
        self._setResult()
        if self.result == self.index:
            for i in range(280):
                self._spinShow()
        else:
            for i in range(140):
                self._spinShow()
        self.isSpinning = False

    def _spinShow(self):
        if self.lastChanged >= 10:
            self.index %= len(self.animation)
            self.screen.blit(self.animation[self.index], self.pos)
            self.lastChanged = -1
        self.lastChanged += 1
