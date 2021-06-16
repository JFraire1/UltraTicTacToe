from ColorsFontsImages import ColorsFontsImages as asset
from pygame import mixer


class musicHandler():
    mixer.init()
    isGaming = False
    menuTrackNum = 0
    gameTrackNum = 0
    gameTrackList = asset.gameMusicList
    menuTrackList = asset.musicList
    # todo get gameplay music name from asset
    musicOn = True
    volume = 1.0

    def setVolume(self, vol):
        musicHandler.volume = vol
        if musicHandler.musicOn:
            mixer.music.set_volume(vol)

    def setGameMusic(self=None):
        musicHandler.isGaming = True

    def changeSong(self=None):
        musicHandler.stop()
        musicHandler.musicLoop()

    def setMenuMusic(self=None):
        musicHandler.isGaming = False

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
            if musicHandler.isGaming:
                musicHandler.gameTrackNum %= len(musicHandler.gameTrackList)
                mixer.music.load(musicHandler.gameTrackList[musicHandler.gameTrackNum])
                mixer.music.play(0, 0, 10)
                musicHandler.gameTrackNum += 1
            else:
                musicHandler.menuTrackNum %= len(musicHandler.menuTrackList)
                mixer.music.load(musicHandler.menuTrackList[musicHandler.menuTrackNum])
                mixer.music.play(0, 0, 10)
                musicHandler.menuTrackNum += 1

    def stop(self=None):
        if mixer.music.get_busy():
            mixer.music.stop()
