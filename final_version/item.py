import pygame
from abc import ABC, abstractmethod
from assetController import AssetController


#Deve ser uma classe Abstrata
class Item(ABC, pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.__x = x
        self.__y = y
        self.__sprite = sprite
        self.__image = AssetController().get_asset(self.__sprite)
        self.__rect = self.__image.get_rect(topleft = (self.__x, self.__y))
        self.__hitbox = self.__rect.inflate(0,0)
    
    @abstractmethod
    def use(self, jogador):
        pass
    
    def getHitbox(self):
        return self.__hitbox
    
    def setImage(self, load):
        if not load:
            self.__image = None
        else:
            self.__image = AssetController().get_asset(self.__sprite)

    def getImage(self):
        return self.__image
    
    def getRect(self):
        return self.__rect
    
    def exclui(self):
        self.kill()

    def draw(self, x, y, valor, pos, surface):
        surface.blit(self.__image, (valor*pos+x, y-4))