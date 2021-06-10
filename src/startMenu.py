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

musicHandler.musicLoop(None)
musicOn = True
clock = pygame.time.Clock()
pygame.init()
screenSize = (500, 475)
screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)
buttons = Buttons(screen)
exitButton = buttons.exitButton()
mainBackground = pygame.image.load(asset.mainBackground)

def close():
    pygame.quit()

def startScreenLoop():
    startScreenText = buttons.startScreenText()
    startButton = buttons.startButton()
    optionButton = buttons.optionButton()
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

    running = True
    flashTimer = 0
    while True:
        musicHandler.musicLoop(None)
        hoveringButtons = buttons.buttonsHovering()
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

        for button in buttons.buttonList:
            if button.toString() in hoveringButtons:
                button.hoverShow()
                flashTimer = 100
            elif button.toString() == "Ultra Tic Tac Toe":
                pass
            else:
                button.show()

        flashTimer += 1
        pygame.display.flip()
        clock.tick(120)


def gameLoop():

    def checkEvents():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.isHovering():
                    return False
        return True

    flashTimer = 0
    running = True
    while True:
        musicHandler.musicLoop(None)
        running = checkEvents()
        if not running:
            close()
            break
        screen.fill(asset.darkPurple)
        pygame.draw.rect(screen, asset.black, [0, 0, 500, 25])
        if exitButton.isHovering():
            exitButton.hoverShow()
        else:
            exitButton.show()
        pygame.display.flip()
        clock.tick(120)

def optionLoop():
    while True:
        musicHandler.musicLoop(None)
        screen.fill((255, 255, 255))
        pygame.display.flip()

startScreenLoop()
