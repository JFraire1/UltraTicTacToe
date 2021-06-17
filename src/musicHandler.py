from ColorsFontsImages import ColorsFontsImages as asset
from pygame import mixer


class musicHandler():
    mixer.init()
    isGaming = False
    menuTrackNum = 0
    gameTrackNum = 0
    gameTrackList = asset.gameMusicList
    menuTrackList = asset.musicList
    musicOn = True
    volume = 1.0

    @staticmethod
    def setVolume(vol):
        musicHandler.volume = vol
        if musicHandler.musicOn:
            mixer.music.set_volume(vol)

    @staticmethod
    def setGameMusic():
        musicHandler.isGaming = True

    @staticmethod
    def changeSong():
        musicHandler.stop()
        musicHandler.musicLoop()

    @staticmethod
    def setMenuMusic():
        musicHandler.isGaming = False

    @staticmethod
    def off():
        mixer.music.set_volume(0.0)

    @staticmethod
    def on():
        mixer.music.set_volume(musicHandler.volume)

    @staticmethod
    def musicSwitch():
        musicHandler.musicOn = not musicHandler.musicOn
        return musicHandler.musicOn

    @staticmethod
    def musicLoop():
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

    @staticmethod
    def stop():
        if mixer.music.get_busy():
            mixer.music.stop()
