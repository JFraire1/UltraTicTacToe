import pygame
from musicHandler import musicHandler
from soundHandler import soundHandler
from ColorsFontsImages import ColorsFontsImages as asset
from ButtonAssets import ButtonAssets as Buttons
from colorPickerHandler import colorPickerHandler
from GameBoard import GameBoard
from turnSlot import turnSlot
from gamePiece import gamePiece
from pygame.locals import (
    RLEACCEL,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
musicHandler.musicSwitch()
musicHandler.musicLoop()
clock = pygame.time.Clock()
pygame.init()
screenSize = (500, 475)
screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)
mainBackground = pygame.image.load(asset.mainBackground)
fpsFont = pygame.font.Font(asset.joystix, 20)


def fps():
    fpsNum = clock.get_fps()
    fpsNum = str(round(fpsNum, 2))
    fps = fpsFont.render(fpsNum, True, asset.neonPink)
    screen.blit(fps, (0, 0))


def setVol(vol):
    soundHandler.setVolume(None, vol)
    musicHandler.setVolume(None, vol)


def close():
    pygame.quit()


def checkMusic():
    if musicHandler.musicOn:
        musicHandler.on()
        musicHandler.musicLoop()
    else:
        musicHandler.off()


def checkButtons(Buttons, hoveringButtons):
    for button in Buttons.buttonList:
        if button.toString() in hoveringButtons:
            button.hoverShow()
        else:
            button.show()


def startScreenLoop():
    startScreenButtons = Buttons(screen)
    exitButton = startScreenButtons.exitButton()
    startScreenText = Buttons(screen).startScreenText()
    startButton = startScreenButtons.startButton()
    optionButton = startScreenButtons.optionButton()

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.toString() in hoveringButtons:
                    return False
                elif startButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    preGameLoop()
                    return False
                elif optionButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    optionLoop()
                    return False
        return True

    flashTimer = 0
    while True:
        checkMusic()
        hoveringButtons = startScreenButtons.buttonsHovering()
        running = checkEvents()
        if not running:
            close()
            break
        screen.blit(mainBackground, (0, 25))
        pygame.draw.rect(screen, asset.darkPurple, [0, 0, 500, 25])

        if flashTimer < 350:
            startScreenText.show()
        elif flashTimer > 450:
            flashTimer = 0

        fps()
        checkButtons(startScreenButtons, hoveringButtons)

        flashTimer += 1
        pygame.display.flip()
        clock.tick(120)


def preGameLoop():
    preGameButtons = Buttons(screen)
    exitButton = preGameButtons.exitButton()
    backButton = preGameButtons.backButton()
    startGameButton = preGameButtons.startGameButton()
    colorPickersP1 = colorPickerHandler(screen)
    colorPickerP1Red = colorPickersP1.colorPickerP1Red()
    colorPickersP1.colorPickerP1Blue()
    colorPickersP1.colorPickerP1Green()
    colorPickersP1.colorPickerP1Orange()
    colorPickersP2 = colorPickerHandler(screen)
    colorPickersP2.colorPickerP2Red()
    colorPickerP2Blue = colorPickersP2.colorPickerP2Blue()
    colorPickersP2.colorPickerP2Green()
    colorPickersP2.colorPickerP2Orange()
    colorPickersP2.selectColor(colorPickerP2Blue.color)
    colorPickersP1.banColor(colorPickerP2Blue.color)
    colorPickersP1.selectColor(colorPickerP1Red.color)
    colorPickersP2.banColor(colorPickerP1Red.color)
    P1Display = preGameButtons.gamePiece(gamePiece.XFACE, colorPickersP1.selectedColor, gamePiece.SIZELARGE, 95, 220)
    P2Display = preGameButtons.gamePiece(gamePiece.OFACE, colorPickersP2.selectedColor, gamePiece.SIZELARGE, 405, 220)
    preGameButtons.player1Text()
    preGameButtons.player2Text()
    xCheckP1 = preGameButtons.XCheckP1()
    xCheckP2 = preGameButtons.XCheckP2()
    xCheckP2.check(False)
    preGameButtons.selectScreenText()
    slot = preGameButtons.turnSlot()
    spinButton = preGameButtons.spinButton()
    preGameButtons.firstText()

    def checkEvents():
        if slot.doneSpinning:
            if slot.result == turnSlot.P1SELECT:
                soundHandler.playSound(None, asset.GLITCHSOUND)
            else:
                soundHandler.playSound(None, asset.GLITCHSOUND)
            slot.valueUpdated()
            return True
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.toString() in hoveringButtons:
                    return False
                if startGameButton.toString() in hoveringButtons:
                    musicHandler.setGameMusic()
                    musicHandler.changeSong()
                    soundHandler.playSound(None, asset.GAMEOVERSOUND)
                    if xCheckP1.checked:
                        XPlayer = 1
                    else:
                        XPlayer = 2
                    if slot.result == turnSlot.P1SELECT:
                        first = 0
                    else:
                        first = 1
                    gameLoop(colorPickersP1.selectedColor, colorPickersP2.selectedColor, XPlayer, first)
                    return False
                if backButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICKSOUND)
                    startScreenLoop()
                    return False
                if xCheckP1.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.GLITCHSOUND)
                    xCheckP1.check(not xCheckP1.checked)
                    xCheckP2.check(not xCheckP2.checked)
                    if xCheckP1.checked:
                        P1Display.setFace(gamePiece.XFACE)
                        P2Display.setFace(gamePiece.OFACE)
                    else:
                        P2Display.setFace(gamePiece.XFACE)
                        P1Display.setFace(gamePiece.OFACE)
                    return True
                if xCheckP2.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.GLITCHSOUND)
                    xCheckP2.check(not xCheckP2.checked)
                    xCheckP1.check(not xCheckP1.checked)
                    if xCheckP2.checked:
                        P2Display.setFace(gamePiece.XFACE)
                        P1Display.setFace(gamePiece.OFACE)
                    else:
                        P1Display.setFace(gamePiece.XFACE)
                        P2Display.setFace(gamePiece.OFACE)
                    return True
                if P1Display.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.GLITCHSOUND)
                    P1Display.cycleSize()
                    return True
                if P2Display.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.GLITCHSOUND)
                    P2Display.cycleSize()
                    return True
                if spinButton.toString() in hoveringButtons:
                    if not slot.isSpinning:
                        soundHandler.playSound(None, asset.SLOTWHEELSOUND)
                        soundHandler.playSound(None, asset.SPINCLICK)
                        slot.spin()
                    return True
                if hoveringColorsP1:
                    soundHandler.playSound(None, asset.GLITCHSOUND)
                    color = hoveringColorsP1[0].split("-")[0]
                    if colorPickersP1.selectColor(color):
                        P1Display.setColor(colorPickersP1.selectedColor)
                        colorPickersP2.banColor(color)
                    return True
                if hoveringColorsP2:
                    soundHandler.playSound(None, asset.GLITCHSOUND)
                    color = hoveringColorsP2[0].split("-")[0]
                    if colorPickersP2.selectColor(color):
                        P2Display.setColor(colorPickersP2.selectedColor)
                        colorPickersP1.banColor(color)
                    return True
        return True

    while True:
        checkMusic()
        hoveringColorsP1 = colorPickersP1.colorsHovering()
        hoveringColorsP2 = colorPickersP2.colorsHovering()
        hoveringButtons = preGameButtons.buttonsHovering()
        running = checkEvents()
        if not running:
            close()
            break

        screen.blit(mainBackground, (0, 25))
        pygame.draw.rect(screen, asset.black, [0, 0, 500, 25])

        checkButtons(colorPickersP1, hoveringColorsP1)
        checkButtons(colorPickersP2, hoveringColorsP2)
        checkButtons(preGameButtons, hoveringButtons)
        fps()

        pygame.display.flip()
        clock.tick(120)


def gameLoop(colorP1, colorP2, XPlayer, first):
    s = pygame.Surface((420, 100), pygame.SRCALPHA)
    s.fill((asset.neonPink[0], asset.neonPink[1], asset.neonPink[2], 70))
    gameButtons = Buttons(screen)
    grabbableGamePieces = Buttons(screen)
    exitButton = gameButtons.exitButton()
    pauseButton = gameButtons.pauseButton()
    turnDisplay = gameButtons.turnDisplay()
    if XPlayer == 1:
        player1X = 0
        gameBoard = GameBoard(screen, colorP1, colorP2)
    else:
        player1X = 1
        gameBoard = GameBoard(screen, colorP2, colorP1)
    grabbableGamePieces.gamePiece(0, gameBoard.colorX, gamePiece.SIZELARGE, 210, 62)
    grabbableGamePieces.gamePiece(0, gameBoard.colorX, gamePiece.SIZEMEDIUM, 330, 62)
    grabbableGamePieces.gamePiece(0, gameBoard.colorX, gamePiece.SIZESMALL, 430, 62)
    gameBoard.turn = first + XPlayer % 2
    playerTurn = gameButtons.playerDisplayText()
    numTexts = {gamePiece.SIZELARGE: gameButtons.num1Text(),
                gamePiece.SIZEMEDIUM: gameButtons.num2Text(),
                gamePiece.SIZESMALL: gameButtons.num3Text()}
    piecesAmountX = {gamePiece.SIZELARGE: 2, gamePiece.SIZEMEDIUM: 4, gamePiece.SIZESMALL: 8}
    piecesAmountO = {gamePiece.SIZELARGE: 2, gamePiece.SIZEMEDIUM: 4, gamePiece.SIZESMALL: 8}
    draggedPiece = gamePiece(screen, 0, gameBoard.colorX, gamePiece.SIZESMALL, 0, 0)

    def updateTurnDisplay(turn):
        if turn == 0:
            for i in turnDisplay:
                i.setText("X Turn")
        else:
            for i in turnDisplay:
                i.setText("O Turn")

    def iterateTurn(turn):
        turn += 1
        tempTurn = turn % 2
        if tempTurn == player1X:
            for i in playerTurn:
                i.setText("P1")
        else:
            for i in playerTurn:
                i.setText("P2")
        for i in grabbableGamePieces.buttonList:
            i.setFace(tempTurn)
            i.setBeingDragged(False)
            if tempTurn == 0:
                for j in numTexts[i.size]:
                    j.setText("x" + str(piecesAmountX[i.size]))
                i.setColor(gameBoard.colorX)
            else:
                for j in numTexts[i.size]:
                    j.setText("x" + str(piecesAmountO[i.size]))
                i.setColor(gameBoard.colorO)
        updateTurnDisplay(tempTurn)
        return turn

    def handleGamePieceAmounts(turn):
        XTurn = turn % 2 == 0
        piece = None

        for i in grabbableGamePieces.buttonList:
            if i.toString() in hoveringPieces:
                piece = i
            elif i.isBeingDragged:
                i.setBeingDragged(False)
                if XTurn:
                    piecesAmountX[i.size] += 1
                    for j in numTexts[i.size]:
                        j.setText("x" + str(piecesAmountX[i.size]))
                else:
                    piecesAmountO[i.size] += 1
                    for j in numTexts[i.size]:
                        j.setText("x" + str(piecesAmountO[i.size]))

        if piece is None:
            return True

        if piece.isBeingDragged:
            if XTurn:
                piecesAmountX[piece.size] += 1
                for j in numTexts[piece.size]:
                    j.setText("x" + str(piecesAmountX[piece.size]))
            else:
                piecesAmountO[piece.size] += 1
                for j in numTexts[piece.size]:
                    j.setText("x" + str(piecesAmountO[piece.size]))
            piece.setBeingDragged(False)
            draggedPiece.setBeingDragged(False)
        else:
            if XTurn:
                if piecesAmountX[piece.size] == 0:
                    return
                piecesAmountX[piece.size] -= 1
                for j in numTexts[piece.size]:
                    j.setText("x" + str(piecesAmountX[piece.size]))
            else:
                if piecesAmountO[piece.size] == 0:
                    return
                piecesAmountO[piece.size] -= 1
                for j in numTexts[piece.size]:
                    j.setText("x" + str(piecesAmountO[piece.size]))
            draggedPiece.setBeingDragged(True)
            draggedPiece.setColor(piece.color)
            draggedPiece.setFace(piece.face)
            draggedPiece.setSize(piece.size)
            draggedPiece.setPos(piece.pos)
            piece.setBeingDragged(True)

    def checkDraggedPiece():
        if draggedPiece.isBeingDragged:
            draggedPiece.show()
            draggedPiece.setPos(pygame.mouse.get_pos())

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    soundHandler.playSound(None, asset.CLICKSOUND)
                    return pauseLoop(gameButtons, gameBoard, grabbableGamePieces)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.toString() in hoveringButtons:
                    return False
                if pauseButton.toString() in hoveringButtons:
                    musicHandler.setVolume(None, musicHandler.volume / 4)
                    soundHandler.playSound(None, asset.CLICKSOUND)
                    return pauseLoop(gameButtons, gameBoard, grabbableGamePieces)
                if hoveringPieces:
                    handleGamePieceAmounts(gameBoard.turn)
                    return True
        return True

    gameBoard.turn = iterateTurn(gameBoard.turn)
    while True:
        checkMusic()
        hoveringPieces = grabbableGamePieces.buttonsHovering()
        hoveringButtons = gameButtons.buttonsHovering()
        running = checkEvents()
        if not running:
            close()
            break
        screen.fill(asset.darkPurple)
        screen.blit(s, (80, 0))
        pygame.draw.rect(screen, asset.black, [0, 0, 500, 25])

        checkButtons(grabbableGamePieces, hoveringPieces)
        checkButtons(gameButtons, hoveringButtons)
        gameBoard.show()
        fps()
        checkDraggedPiece()

        pygame.display.flip()
        clock.tick(120)


def pauseLoop(gameButtons, gameBoard, grabbableGamePieces):
    s = pygame.Surface((500, 475), pygame.SRCALPHA)
    pauseButtons = Buttons(screen)
    pauseButton = pauseButtons.pauseButton()
    exitButton = pauseButtons.exitButton()
    continueButton = pauseButtons.continueButton()
    mainMenuButton = pauseButtons.mainMenuButton()
    pauseText = pauseButtons.pauseText()

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    musicHandler.setVolume(None, 4 * musicHandler.volume)
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pauseButton.toString() in hoveringButtons:
                    musicHandler.setVolume(None, 4 * musicHandler.volume)
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    return True
                if continueButton.toString() in hoveringButtons:
                    musicHandler.setVolume(None, 4 * musicHandler.volume)
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    return True
                if exitButton.toString() in hoveringButtons:
                    return False
                if mainMenuButton.toString() in hoveringButtons:
                    musicHandler.setVolume(None, 4 * musicHandler.volume)
                    soundHandler.playSound(None, asset.CLICKSOUND)
                    musicHandler.setMenuMusic()
                    musicHandler.changeSong()
                    startScreenLoop()
                    return False

    while True:
        hoveringButtons = pauseButtons.buttonsHovering()
        checkMusic()
        out = checkEvents()
        if out != None:
            break
        s.fill(asset.darkPurple)
        screen.blit(s, (0, 25))
        pygame.draw.rect(screen, asset.black, [0, 0, 500, 25])
        for button in gameButtons.buttonList:
            if button.toString() != pauseButton.toString():
                button.show()
        for button in grabbableGamePieces.buttonList:
            if button.toString() != pauseButton.toString():
                button.show()
        gameBoard.show()
        s.fill((asset.darkPurple[0], asset.darkPurple[1], asset.darkPurple[2], 190))
        screen.blit(s, (0, 25))
        checkButtons(pauseButtons, hoveringButtons)
        fps()
        pygame.display.flip()
        clock.tick(120)
    return out


def optionLoop():
    optionButtons = Buttons(screen)
    exitButton = optionButtons.exitButton()
    backButton = optionButtons.backButton()
    musicText = optionButtons.musicText()
    soundText = optionButtons.soundText()
    soundCheckBox = optionButtons.soundCheckBox()
    musicCheckBox = optionButtons.musicCheckBox()
    soundSlider = optionButtons.soundSlider()
    soundCheckBox.check(soundHandler.soundOn)
    musicCheckBox.check(musicHandler.musicOn)
    soundSlider.setValueInit(soundHandler.volume)

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if soundSlider.toString() in hoveringButtons:
                    soundSlider.setDragged(True)
                    soundSlider.setValue()
                    soundHandler.setVolume(None, soundSlider.value)
                    musicHandler.setVolume(None, soundSlider.value)
                if exitButton.toString() in hoveringButtons:
                    return False
                if backButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICKSOUND)
                    startScreenLoop()
                    return False
                if musicCheckBox.toString() in hoveringButtons or musicText.toString() in hoveringButtons:
                    musicHandler.musicSwitch()
                    if musicHandler.musicOn:
                        soundHandler.playSound(None, asset.CLICK2SOUND)
                    else:
                        soundHandler.playSound(None, asset.CLICKSOUND)
                    musicCheckBox.check(musicHandler.musicOn)
                    return True
                if soundCheckBox.toString() in hoveringButtons or soundText.toString() in hoveringButtons:
                    soundHandler.soundSwitch()
                    if soundHandler.soundOn:
                        soundHandler.on()
                        soundHandler.playSound(None, asset.CLICK2SOUND)
                    else:
                        soundHandler.off()
                        soundHandler.playSound(None, asset.CLICKSOUND)
                    soundCheckBox.check(soundHandler.soundOn)
                    return True
            if event.type == pygame.MOUSEMOTION:
                if soundSlider.beingDragged:
                    soundSlider.setDragged(True)
                    soundSlider.setValue()
                    soundHandler.setVolume(None, soundSlider.value)
                    musicHandler.setVolume(None, soundSlider.value)
            if event.type == pygame.MOUSEBUTTONUP:
                soundSlider.setDragged(False)
        return True

    while True:
        checkMusic()
        hoveringButtons = optionButtons.buttonsHovering()
        running = checkEvents()
        if not running:
            close()
            break

        screen.fill(asset.darkPurple)
        pygame.draw.rect(screen, asset.black, [0, 0, 500, 25])

        checkButtons(optionButtons, hoveringButtons)
        fps()

        pygame.display.flip()
        clock.tick(120)


startScreenLoop()
