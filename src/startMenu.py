import pygame
from musicHandler import musicHandler
from ColorsFontsImages import ColorsFontsImages as asset
from ButtonAssets import ButtonAssets as Buttons
from pygame.locals import (
    RLEACCEL,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

musicOn = True
musicHandler.musicLoop(None)
clock = pygame.time.Clock()
pygame.init()
screenSize = (500, 475)
screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)
mainBackground = pygame.image.load(asset.mainBackground)


def close():
    pygame.quit()

def checkMusic():
    if musicOn:
        musicHandler.musicLoop(None)
    else:
        musicHandler.stop(None)

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
                    gameLoop()
                    return False
                elif optionButton.toString() in hoveringButtons:
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

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.toString() in hoveringButtons:
                    return False
                if pauseButton.toString() in hoveringButtons:
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
    optionButton = pauseButtons.optionButton()
    continueButton = pauseButtons.continueButton()
    mainMenuButton = pauseButtons.mainMenuButton()

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pauseButton.toString() in hoveringButtons:
                    return True
                if continueButton.toString() in hoveringButtons:
                    return True
                if exitButton.toString() in hoveringButtons:
                    return False
                if optionButton.toString() in hoveringButtons:
                    optionLoop()
                    return False
                if mainMenuButton.toString() in hoveringButtons:
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
        for button in gameButtons.buttonList:
            if button.toString() != "||":
                button.show()
        s.fill((asset.darkPurple[0], asset.darkPurple[1], asset.darkPurple[2], 90))
        screen.blit(s, (0, 25))
        checkButtons(pauseButtons, hoveringButtons)
        pygame.display.flip()
        clock.tick(120)
    return out


def optionLoop():
    optionButtons = Buttons(screen)
    exitButton = optionButtons.exitButton()
    backButton = optionButtons.backButton()

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.toString() in hoveringButtons:
                    return False
                if backButton.toString() in hoveringButtons:
                    startScreenLoop()
                    return False
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
