from ColorsFontsImages import ColorsFontsImages as asset
from pygame import mixer

class musicHandler():
    mixer.init()
    trackNum = 0
    trackList = asset.musicList

    def musicLoop(self):
        if mixer.music.get_busy():
            return
        else:
            musicHandler.trackNum %= len(musicHandler.trackList)
            mixer.music.load(musicHandler.trackList[musicHandler.trackNum])
            mixer.music.play(0,0,10)
            musicHandler.trackNum += 1
