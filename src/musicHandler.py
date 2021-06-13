from ColorsFontsImages import ColorsFontsImages as asset
from pygame import mixer

class musicHandler():
    mixer.init()
    trackNum = 0
    trackList = asset.musicList
    musicOn = True
    volume = 1.0

    def setVolume(self, vol):
        musicHandler.volume = vol
        if musicHandler.musicOn:
            mixer.music.set_volume(vol)

    def off(self=None):
        mixer.music.set_volume(0.0)

    def on(self=None):
        mixer.music.set_volume(musicHandler.volume)

    def musicSwitch(self=None):
        musicHandler.musicOn = not musicHandler.musicOn
        return musicHandler.musicOn

    def musicLoop(self=None):
        if mixer.music.get_busy():
            return
        else:
            musicHandler.trackNum %= len(musicHandler.trackList)
            mixer.music.load(musicHandler.trackList[musicHandler.trackNum])
            mixer.music.play(0,0,10)
            musicHandler.trackNum += 1

    def stop(self=None):
        if mixer.music.get_busy():
            mixer.music.stop()
