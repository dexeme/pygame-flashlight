import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, sprite):
        super().__init__()
        self.__image = sprite
        self.__rect = self.__image.get_rect(topleft = pos)
        # Função inflate para mudar o tamanho do retângulo
        self.__hitbox = self.__rect.inflate(0,-10)

    def getHitbox(self):
        return self.__hitbox

    def getRect(self):
        return self.__rect

    def getImage(self):
        return self.__image


class Chao(pygame.sprite.Sprite):
    def __init__(self, pos, filepath):
        super().__init__()

        self.__image = pygame.image.load(filepath).convert_alpha()
        self.__rect = self.__image.get_rect(topleft = pos)

    def getRect(self):
        return self.__rect

    def getImage(self):
        return self.__image

    def setImage(self, image):
        self.__image = image
    