from ColorsFontsImages import ColorsFontsImages as asset
from textFormat import textFormat
from gamePiece import gamePiece
from turnSlot import turnSlot
from checkBox import checkBox
from slider import Slider


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
        temp = textFormat(self.screen, "Ultra Tic Tac Toe", False, 0, 0, 0, True, asset.black,
                          -1, -1, (asset.joystix, 30), 0, 75, asset.darkPurple, (100, 100, 100),
                          50, 0, textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def startButton(self):
        temp = textFormat(self.screen, "Start", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 240, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def optionButton(self):
        temp = textFormat(self.screen, "Options", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 300, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def exitButton(self):
        temp = textFormat(self.screen, "X", True, 1, 10, 0, False, asset.black, -1, -1, (asset.joystix, 20),
                          478, 1, asset.white, asset.red, 50, 2, -1, -1, textFormat.ENLARGELEFT)
        self.buttonList.append(temp)
        return temp

    def backButton(self):
        temp = textFormat(self.screen, "Back", True, 8, 8, 4, False, asset.black, -1, -1,
                          (asset.joystix, 15), 5, 30, asset.white, asset.neonPink, 255, 2,
                          -1, -1, textFormat.ENLARGERIGHT)
        self.buttonList.append(temp)
        return temp

    def pauseButton(self):
        temp = textFormat(self.screen, "||", True, 8, 8, 4, False, asset.black, -1, -1,
                          (asset.joystix, 15), 5, 30, asset.white, asset.neonPink, 255, 2,
                          -1, -1, textFormat.ENLARGERIGHT)
        self.buttonList.append(temp)
        return temp

    def continueButton(self):
        temp = textFormat(self.screen, "Continue", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 240, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def mainMenuButton(self):
        temp = textFormat(self.screen, "Main Menu", True, 8, -1, 4, False, asset.black, -1, 120,
                          (asset.joystix, 15), 0, 300, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def pauseText(self):
        temp = textFormat(self.screen, "Pause", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 50), 0, 100, asset.neonPink, (100, 100, 100), 50,
                          0, textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def musicText(self):
        temp = textFormat(self.screen, "Music: ", False, 0, 0, 0, False, asset.black, -1, -1,
                          (asset.joystix, 20), 167, 160, asset.neonPink, (100, 100, 100), 50,
                          0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def musicCheckBox(self):
        temp = checkBox(self.screen, True, "X", True, -1, -1, 4, False, asset.white, 20,
                        20, (asset.joystix, 40), 296, 149.6, asset.white, asset.neonPink, -20, 3,
                        -1, -1)
        self.buttonList.append(temp)
        return temp

    def soundText(self):
        temp = textFormat(self.screen, "Effects: ", False, 0, 0, 0, False, asset.black,
                          -1, -1, (asset.joystix, 20), 156, 230, asset.neonPink, (100, 100, 100),
                          50, 0, -1, -1, textFormat.ENLARGENOMOVEMENT)
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

    def startGameButton(self):
        temp = textFormat(self.screen, "Start Game", True, 8, 20, 4, False, asset.black, -1, -1,
                          (asset.joystix, 15), 0, 360, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def gamePiece(self, face, color, size, x, y):
        temp = gamePiece(self.screen, face, color, size, x, y)
        self.buttonList.append(temp)
        return temp

    def player1Text(self):
        temp = textFormat(self.screen, "Player 1:", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 23), 15, 135, asset.neonPink, (100, 100, 100), 50,
                          0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def player2Text(self):
        temp = textFormat(self.screen, "Player 2:", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 23), 325, 135, asset.neonPink, (100, 100, 100), 50,
                          0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def XCheckP1(self):
        temp = checkBox(self.screen, True, "X", True, -1, -1, 4, False, asset.white, 15,
                        15, (asset.joystix, 35), 15, 200, asset.white, asset.neonPink,
                        -20, 3, -1, -1)
        self.buttonList.append(temp)
        return temp

    def XCheckP2(self):
        temp = checkBox(self.screen, True, "X", True, -1, -1, 4, False, asset.white, 15,
                        15, (asset.joystix, 35), 460, 200, asset.white, asset.neonPink,
                        -20, 3, -1, -1)
        self.buttonList.append(temp)
        return temp

    def selectScreenText(self):
        temp = textFormat(self.screen, "Choose Color", False, 0, 0, 0, True, asset.black,
                          -1, -1, (asset.joystix, 30), 0, 75, asset.darkPurple, (100, 100, 100),
                          50, 0, textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def slotTest(self):
        temp = textFormat(self.screen, "", True, -1, -1, 0,
                          False, asset.white, 50, 50, (asset.joystix, 35), 245, 200,
                          asset.black, asset.white, 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def turnSlot(self):
        temp = turnSlot(self.screen, 225, 195, True, 4)
        self.buttonList.append(temp)
        return temp

    def spinButton(self):
        temp = textFormat(self.screen, "Spin", True, 8, 20, 4, False, asset.black, -1, -1,
                          (asset.joystix, 12), 0, 270, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp

    def turnDisplay(self):
        temp = textFormat(self.screen, "X Turn:", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 16), 85, 30, asset.white, (100, 100, 100), 50,
                          0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        temp2 = textFormat(self.screen, "X Turn:", False, 0, 0, 0, True, asset.black, -1, -1,
                           (asset.joystix, 16), 88, 33, asset.black, (100, 100, 100), 50,
                           0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp2)
        self.buttonList.append(temp)
        return temp, temp2

    def firstText(self):
        temp = textFormat(self.screen, "First Move:", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 14), 325, 165, asset.white, (100, 100, 100), 50,
                          0, textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        temp2 = textFormat(self.screen, "First Move:", False, 0, 0, 0, True, asset.black, -1, -1,
                           (asset.joystix, 14), 328, 168, asset.black, (100, 100, 100), 50,
                           0, textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp2)
        self.buttonList.append(temp)

    def num1Text(self):
        temp = textFormat(self.screen, "x2", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 20), 255, 50, asset.white, (100, 100, 100), 50,
                          0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        temp2 = textFormat(self.screen, "x2", False, 0, 0, 0, True, asset.black, -1, -1,
                           (asset.joystix, 20), 258, 53, asset.black, (100, 100, 100), 50,
                           0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp2)
        self.buttonList.append(temp)
        return temp, temp2

    def num2Text(self):
        temp = textFormat(self.screen, "x4", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 20), 367, 50, asset.white, (100, 100, 100), 50,
                          0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        temp2 = textFormat(self.screen, "x4", False, 0, 0, 0, True, asset.black, -1, -1,
                           (asset.joystix, 20), 370, 53, asset.black, (100, 100, 100), 50,
                           0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp2)
        self.buttonList.append(temp)
        return temp, temp2

    def num3Text(self):
        temp = textFormat(self.screen, "x8", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 20), 454, 50, asset.white, (100, 100, 100), 50,
                          0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        temp2 = textFormat(self.screen, "x8", False, 0, 0, 0, True, asset.black, -1, -1,
                           (asset.joystix, 20), 457, 53, asset.black, (100, 100, 100), 50,
                           0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp2)
        self.buttonList.append(temp)
        return temp, temp2

    def playerDisplayText(self):
        temp = textFormat(self.screen, "P1", False, 0, 0, 0, True, asset.black, -1, -1,
                          (asset.joystix, 40), 85, 45, asset.white, (100, 100, 100), 50,
                          0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        temp2 = textFormat(self.screen, "P1", False, 0, 0, 0, True, asset.black, -1, -1,
                           (asset.joystix, 40), 90, 50, asset.black, (100, 100, 100), 50,
                           0, -1, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp2)
        self.buttonList.append(temp)
        return temp, temp2

    def hitBox(self):
        temp = textFormat(self.screen, "", True, 8, -1, 4, False, asset.black, 120, 120,
                          (asset.joystix, 15), 0, 240, asset.white, asset.neonPink, 255, 2,
                          textFormat.ALIGNMENTCENTER, -1, textFormat.ENLARGENOMOVEMENT)
        self.buttonList.append(temp)
        return temp


    def alignmentCheck(self):
        temp = textFormat(self.screen, "", True, -1, -1, 0,
                          False, asset.neonPink, 5, 400, (asset.joystix, 35), 0, 200,
                          asset.neonPink, asset.neonPink, 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp

    def alignmentCheck2(self):
        temp = textFormat(self.screen, "", True, -1, -1, 0,
                          False, asset.neonPink, 400, 5, (asset.joystix, 35), 0, 200,
                          asset.neonPink, asset.neonPink, 50, 0, textFormat.ALIGNMENTCENTER, -1)
        self.buttonList.append(temp)
        return temp
