import pygame
from settings import *
from level import Level



class InGame:
    def __init__(self):
        # Configuração inicial
        self.__screen = pygame.display.get_surface()
        self.__level = Level()
        
    def loadgame(self):
        self.__level.load()
        
    def getLevel(self):
        return self.__level

    def run(self):
        self.__screen.fill((0, 0, 0))
        self.__level.run()
        
        if self.__level.getPlayerDead():
            return 'morreu'
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return 'pause'
