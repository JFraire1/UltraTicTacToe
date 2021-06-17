from ColorsFontsImages import ColorsFontsImages as asset
from pygame import mixer

class soundHandler:
    mixer.init()
    soundList = []
    for i in asset.soundList:
        soundList.append(mixer.Sound(i))
    for i in soundList:
        i.set_volume(1.0)
    volume = 1.0
    soundOn = True

    @staticmethod
    def soundSwitch():
        soundHandler.soundOn = not soundHandler.soundOn

    @staticmethod
    def playSound(index):
        if 0 <= index < len(soundHandler.soundList) and len(soundHandler.soundList) != 0:
            soundHandler.soundList[index].play()

    @staticmethod
    def setVolume(vol):
        soundHandler.volume = vol
        if soundHandler.soundOn:
            for i in soundHandler.soundList:
                i.set_volume(vol)

    @staticmethod
    def off():
        for i in soundHandler.soundList:
            i.set_volume(0.0)

    @staticmethod
    def on():
        for i in soundHandler.soundList:
            i.set_volume(soundHandler.volume)
