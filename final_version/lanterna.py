import pygame
from assetController import AssetController
from pilha import Pilha
from settings import WIDTH, HEIGTH
from sound import Sound


class Lanterna(pygame.sprite.Sprite):
    def __init__(self, pos, status=False):
        super().__init__(pygame.sprite.Group())
        self.__status = status
        self.__pilha = Pilha(pos[0], pos[1], 'pilha', 50)

        self.__Onimage = pygame.image.load('tiles/lightOn.png').convert_alpha()
        self.__Offimage = pygame.image.load('tiles/lightOff.png').convert_alpha()
        rect = self.__Onimage.get_rect()

        self.__x = (WIDTH - rect[2]) / 2
        self.__y = (HEIGTH - rect[3]) / 2

        self.__toggle_timer = 0  # timer para impedir que a pilha fique ligando ou desligando se o jogador segurar CTRL
        self.__toggle_cooldown = 2

    def cooldown(self):
        if self.__toggle_timer > 0:
            self.__toggle_timer -= 1

    def update(self):
        self.cooldown()
        self.__pilha.contador()

    def getPilha(self):
        return self.__pilha
    
    def setPilha(self, pilha: Pilha):
        self.__pilha = pilha
        self.__pilha.setUsando(self.__status)

    def getStatus(self):
        return self.__status

    def setStatus(self):
        if self.__toggle_timer <= 0:
            self.__status = not self.__status
            Sound().playSound('lanterna')
            self.__pilha.setUsando(self.__status)

        self.__toggle_timer = self.__toggle_cooldown

    def draw(self, tela):
        if self.__status and self.__pilha.getUsando() and self.__pilha.getStatus():
            tela.blit(self.__Onimage, (self.__x, self.__y))
        else:
            tela.blit(self.__Offimage, (self.__x, self.__y))
