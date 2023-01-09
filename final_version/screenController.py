from ingame import InGame
from interfaces.menuScreen import MenuScreen
from interfaces.gameoverScreen import GameOverScreen
from interfaces.pauseScreen import PauseScreen
from interfaces.optionsScreen import OptionsScreen
from interfaces.controlsScreen import ControlsScreen
from sound import Sound

class ScreenController:
    def __init__(self):
        self.__ingame = InGame()
        self.__mainmenu = MenuScreen()
        self.__pause = PauseScreen()
        self.__options = OptionsScreen()
        self.__controls = ControlsScreen()
        self.__gameover = GameOverScreen()
        self.__last_screen = None

    def firstScreen(self):
        return self.__mainmenu
    
    def nextScreen(self, key, screen):
        
        if key == 'mainmenu':
            self.__mainmenu = MenuScreen()
            return self.__mainmenu
        elif key == 'start':
            self.__ingame = InGame()
            return self.__ingame
        elif key == 'continue':
            return self.__ingame
        elif key == 'loadgame':
            try:
                self.__ingame.loadgame()
            except:
                self.__ingame = InGame()
            return self.__ingame
        elif key == 'morreu':
            return self.__gameover
        elif key == 'pause':
            return self.__pause 
        elif key == 'restart':
            self.__ingame.getLevel().restart()
            return self.__ingame
        elif key == 'options':
            self.__last_screen = screen
            return self.__options
        elif key == 'controls':
            self.__last_screen = screen
            return self.__controls
        elif key == 'voltar':
            return self.__last_screen
        elif key == 'apply':
            volume = self.__options.getSlider().getValue()
            Sound().setVolume(volume)
            return self.__options