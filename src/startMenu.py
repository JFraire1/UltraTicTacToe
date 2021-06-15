import pygame
from musicHandler import musicHandler
from soundHandler import soundHandler
from ColorsFontsImages import ColorsFontsImages as asset
from ButtonAssets import ButtonAssets as Buttons
from colorPickerHandler import colorPickerHandler
from gamePiece import gamePiece
from pygame.locals import (
    RLEACCEL,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

musicHandler.musicLoop()
clock = pygame.time.Clock()
pygame.init()
screenSize = (500, 475)
screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)
mainBackground = pygame.image.load(asset.mainBackground)

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
    colorPickerP1Blue = colorPickersP1.colorPickerP1Blue()
    colorPickerP1Green = colorPickersP1.colorPickerP1Green()
    colorPickerP1Orange = colorPickersP1.colorPickerP1Orange()
    colorPickersP2 = colorPickerHandler(screen)
    colorPickerP2Red = colorPickersP2.colorPickerP2Red()
    colorPickerP2Blue = colorPickersP2.colorPickerP2Blue()
    colorPickerP2Green = colorPickersP2.colorPickerP2Green()
    colorPickerP2Orange = colorPickersP2.colorPickerP2Orange()
    colorPickersP2.selectColor(colorPickerP2Blue.color)
    colorPickersP1.banColor(colorPickerP2Blue.color)
    colorPickersP1.selectColor(colorPickerP1Red.color)
    colorPickersP2.banColor(colorPickerP1Red.color)
    P1Display = preGameButtons.gamePiece(gamePiece.XFACE, colorPickersP1.selectedColor, gamePiece.SIZELARGE, 95, 200)
    P2Display = preGameButtons.gamePiece(gamePiece.OFACE, colorPickersP2.selectedColor, gamePiece.SIZELARGE, 405, 200)
    player1Text = preGameButtons.player1Text()
    player2Text = preGameButtons.player2Text()
    xCheckP1 = preGameButtons.XCheckP1()
    xTextP1 = preGameButtons.XTextP1()
    xCheckP2 = preGameButtons.XCheckP2()
    xTextP2 = preGameButtons.XTextP2()
    xCheckP2.check(False)
    selectScreenText = preGameButtons.selectScreenText()


    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.toString() in hoveringButtons:
                    return False
                if startGameButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    gameLoop()
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
                if hoveringColorsP1:
                    soundHandler.playSound(None, asset.GLITCHSOUND)
                    color = hoveringColorsP1[0].split("-")[0]
                    if colorPickersP1.selectColor(color):
                        P1Display.setColor(colorPickersP1.selectedColor) # replace with piece color change
                        colorPickersP2.banColor(color)
                    return True
                if hoveringColorsP2:
                    soundHandler.playSound(None, asset.GLITCHSOUND)
                    color = hoveringColorsP2[0].split("-")[0]
                    if colorPickersP2.selectColor(color):
                        P2Display.setColor(colorPickersP2.selectedColor) # replace with piece color change
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

        pygame.display.flip()
        clock.tick(120)



def gameLoop():
    gameButtons = Buttons(screen)
    exitButton = gameButtons.exitButton()
    pauseButton = gameButtons.pauseButton()
    inProgressButton = gameButtons.inProgressButton()

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    soundHandler.playSound(None, asset.CLICKSOUND)
                    return pauseLoop(gameButtons)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.toString() in hoveringButtons:
                    return False
                if pauseButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICKSOUND)
                    return pauseLoop(gameButtons)
        return True

    while True:
        checkMusic()
        hoveringButtons = gameButtons.buttonsHovering()
        running = checkEvents()
        if not running:
            close()
            break
        screen.fill(asset.darkPurple)
        pygame.draw.rect(screen, asset.black, [0, 0, 500, 25])

        checkButtons(gameButtons, hoveringButtons)

        pygame.display.flip()
        clock.tick(120)

def pauseLoop(gameButtons):
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
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pauseButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    return True
                if continueButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICK2SOUND)
                    return True
                if exitButton.toString() in hoveringButtons:
                    return False
                if mainMenuButton.toString() in hoveringButtons:
                    soundHandler.playSound(None, asset.CLICKSOUND)
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
        s.fill((asset.darkPurple[0], asset.darkPurple[1], asset.darkPurple[2], 190))
        screen.blit(s, (0, 25))
        checkButtons(pauseButtons, hoveringButtons)
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

        pygame.display.flip()
        clock.tick(120)


startScreenLoop()
