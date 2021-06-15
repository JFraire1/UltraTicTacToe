import pygame
from ColorsFontsImages import ColorsFontsImages as asset
from colorPicker import colorPicker

class colorPickerHandler:
    def __init__(self, screen):
        self.screen = screen
        self.buttonList = []
        self.selectedColor = None

    def colorsHovering(self):
        temp = []
        for i in self.buttonList:
            if i.isHovering() and i.selectable:
                temp.append(i.toString())
        return temp

    def _findSelectedColor(self, color):
        for i in self.buttonList:
            if str(i.color) == str(color):
                return i

    def selectColor(self, color):
        selectedColorPicker = self._findSelectedColor(color)
        if selectedColorPicker is not None:
            if not selectedColorPicker.selectable:
                return
            for i in self.buttonList:
                i.setSelected(False)
            selectedColorPicker.setSelected(True)
            self.selectedColor = selectedColorPicker.color
            return True
        return False

    def banColor(self, color):
        for i in self.buttonList:
            if str(i.color) == str(color):
                i.setSelectable(False)
            else:
                i.setSelectable(True)

    def colorPickerP1Red(self):
        temp = colorPicker(self.screen, asset.red, 35, 300, 15, True, 3, asset.white, 2, asset.yellow)
        self.buttonList.append(temp)
        return temp

    def colorPickerP1Blue(self):
        temp = colorPicker(self.screen, asset.blue, 75, 300, 15, True, 3, asset.white, 2, asset.yellow)
        self.buttonList.append(temp)
        return temp

    def colorPickerP1Green(self):
        temp = colorPicker(self.screen, asset.green, 115, 300, 15, True, 3, asset.white, 2, asset.yellow)
        self.buttonList.append(temp)
        return temp

    def colorPickerP1Orange(self):
        temp = colorPicker(self.screen, asset.orange, 155, 300, 15, True, 3, asset.white, 2, asset.yellow)
        self.buttonList.append(temp)
        return temp

    def colorPickerP2Red(self):
        temp = colorPicker(self.screen, asset.red, 345, 300, 15, True, 3, asset.white, 2, asset.yellow)
        self.buttonList.append(temp)
        return temp

    def colorPickerP2Blue(self):
        temp = colorPicker(self.screen, asset.blue, 385, 300, 15, True, 3, asset.white, 2, asset.yellow)
        self.buttonList.append(temp)
        return temp

    def colorPickerP2Green(self):
        temp = colorPicker(self.screen, asset.green, 425, 300, 15, True, 3, asset.white, 2, asset.yellow)
        self.buttonList.append(temp)
        return temp

    def colorPickerP2Orange(self):
        temp = colorPicker(self.screen, asset.orange, 465, 300, 15, True, 3, asset.white, 2, asset.yellow)
        self.buttonList.append(temp)
        return temp