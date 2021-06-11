from textFormat import textFormat
from ColorsFontsImages import ColorsFontsImages as asset

class ButtonAssets:
    def __init__(self, screen):
        self.screen = screen
        self.buttonList = []

    def buttonsHovering(self):
        temp = []
        for i in self.buttonList:
            if i.isHovering():
                temp.append(i.textString)
        return temp

    def startScreenText(self):
        temp = textFormat(self.screen, "Ultra Tic Tac Toe", False, 0, 0, 0,
                          True, asset.black, -1, -1, (asset.joystix, 30), 0, 75,
                          asset.darkPurple, (100, 100, 100), 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def startButton(self):
        temp = textFormat(self.screen, "Start", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 215, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def optionButton(self):
        temp = textFormat(self.screen, "Options", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 275, asset.white, asset.neonPink, 255, 2,
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
                          (asset.joystix, 15), 5, 30, asset.white, asset.neonPink, 255, 2,
                          -1, -1)
        self.buttonList.append(temp)
        return temp

    def pauseButton(self):
        temp = textFormat(self.screen, "||", True, 8, 8, 4, False, asset.black, -1, -1,
                          (asset.joystix, 15), 5, 30, asset.white, asset.neonPink, 255, 2,
                          -1, -1)
        self.buttonList.append(temp)
        return temp

    def continueButton(self):
        temp = textFormat(self.screen, "Continue", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 215, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def mainMenuButton(self):
        temp = textFormat(self.screen, "Main Menu", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 335, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp