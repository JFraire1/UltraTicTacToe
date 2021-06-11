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

    def soundSwitch(self=None):
        soundHandler.soundOn = not soundHandler.soundOn

    def playSound(self, index):
        if 0 <= index < len(soundHandler.soundList) and len(soundHandler.soundList) != 0:
            soundHandler.soundList[index].play()

    def setVolume(self, vol):
        if vol >= 0:
            soundHandler.volume = vol
            for i in soundHandler.soundList:
                i.set_volume(vol)

    def off(self = None):
        for i in soundHandler.soundList:
            i.set_volume(0.0)

    def on(self = None):
        for i in soundHandler.soundList:
            i.set_volume(soundHandler.volume)
