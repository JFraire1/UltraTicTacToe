from textFormat import textFormat
from checkBox import checkBox
from slider import Slider
from ColorsFontsImages import ColorsFontsImages as asset

class ButtonAssets:
    def __init__(self, screen):
        self.screen = screen
        self.buttonList = []

    def buttonsHovering(self):
        temp = []
        for i in self.buttonList:
            if i.isHovering():
                temp.append(i.toString())
        return temp

    def startScreenText(self):
        temp = textFormat(self.screen, "Ultra Tic Tac Toe", False, 0, 0, 0,
                          True, asset.black, -1, -1, (asset.joystix, 30), 0, 75,
                          asset.darkPurple, (100, 100, 100), 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def startButton(self):
        temp = textFormat(self.screen, "Start", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 240, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def optionButton(self):
        temp = textFormat(self.screen, "Options", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 300, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def exitButton(self):
        temp = textFormat(self.screen, "X", True, 7, 6, 0, False, asset.black, -1, -1, ("Calibri Bold", 27),
                          485, 4, asset.white, asset.red, 50, -2, -1, -1)
        self.buttonList.append(temp)
        return temp

    def backButton(self):
        temp = textFormat(self.screen, "Back", True, 8, 8, 4, False, asset.black, -1, -1,
                          (asset.joystix, 15), 10, 30, asset.white, asset.neonPink, 255, 2,
                          -1, -1)
        self.buttonList.append(temp)
        return temp

    def pauseButton(self):
        temp = textFormat(self.screen, "||", True, 8, 8, 4, False, asset.black, -1, -1,
                          (asset.joystix, 15), 8, 30, asset.white, asset.neonPink, 255, 2,
                          -1, -1)
        self.buttonList.append(temp)
        return temp

    def continueButton(self):
        temp = textFormat(self.screen, "Continue", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 240, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def mainMenuButton(self):
        temp = textFormat(self.screen, "Main Menu", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 300, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def inProgressButton(self):
        temp = textFormat(self.screen, "In Progress :|", False, 0, 0, 0,
                          True, asset.black, -1, -1, (asset.joystix, 35), 0, 200,
                          asset.neonPink, (100, 100, 100), 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def pauseText(self):
        temp = textFormat(self.screen, "Pause", False, 0, 0, 0,
                          True, asset.black, -1, -1, (asset.joystix, 50), 0, 100,
                          asset.neonPink, (100, 100, 100), 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def musicText(self):
        temp = textFormat(self.screen, "Music: ", False, 0, 0, 0,
                          False, asset.black, -1, -1, (asset.joystix, 20), 167, 160,
                          asset.neonPink, (100, 100, 100), 50, 0, -1, -1)
        self.buttonList.append(temp)
        return temp

    def musicCheckBox(self):
        temp = checkBox(self.screen, True, "X", True, -1, -1, 4, False, asset.white, 20,
                 20, (asset.joystix, 40), 296, 149.6, asset.white, asset.neonPink,-20, 3,-1,-1)
        self.buttonList.append(temp)
        return temp

    def soundText(self):
        temp = textFormat(self.screen, "Effects: ", False, 0, 0, 0,
                          False, asset.black, -1, -1, (asset.joystix, 20), 156, 230,
                          asset.neonPink, (100, 100, 100), 50, 0, -1, -1)
        self.buttonList.append(temp)
        return temp

    def soundCheckBox(self):
        temp = checkBox(self.screen, True, "X", True, -1, -1, 4, False, asset.white, 20,
                        20, (asset.joystix, 40), 303, 219.6, asset.white, asset.neonPink, -20, 3, -1, -1)
        self.buttonList.append(temp)
        return temp

    def soundSlider(self):
        temp = Slider(self.screen, 0, 300, Slider.ALIGNMENTCENTER, -1, asset.neonPink, asset.black, True, asset.white,
                      300, 12, Slider.DRAGRECTANGLE, asset.white, 30, 22, 14, 1.0, 3, 2)
        self.buttonList.append(temp)
        return temp

    def alignmentCheck(self):
        temp = textFormat(self.screen, "", True, -1, -1, 0,
                          False, asset.neonPink, 10, 200, (asset.joystix, 35), 0, 200,
                          asset.neonPink, asset.neonPink, 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def alignmentCheck2(self):
        temp = textFormat(self.screen, "", True, -1, -1, 0,
                          False, asset.neonPink, 200, 1, (asset.joystix, 35), 0, 200,
                          asset.neonPink, asset.neonPink, 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp
