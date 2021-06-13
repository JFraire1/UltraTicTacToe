import pygame
from musicHandler import musicHandler
from soundHandler import soundHandler
from ColorsFontsImages import ColorsFontsImages as asset
from ButtonAssets import ButtonAssets as Buttons
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
                    gameLoop()
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
    canDragSound = False
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
        global canDragSound
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if soundSlider.toString() in hoveringButtons:
                    canDragSound = True
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
                if canDragSound:
                    soundSlider.setDragged(True)
                    soundSlider.setDragged(True)
                    soundSlider.setValue()
                    soundHandler.setVolume(None, soundSlider.value)
                    musicHandler.setVolume(None, soundSlider.value)
            if event.type == pygame.MOUSEBUTTONUP:
                canDragSound = False
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
