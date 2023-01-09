import pygame
from debug import Debug
from settings import HEIGTH, WIDTH
from item import Item
from assetController import AssetController
from projectileWeapon import ProjectileWeapon
from meleeWeapon import MeleeWeapon

class Hud():
    def __init__(self):
        self.__hud_pilha = AssetController().get_asset('hud_pilha')
        self.__hud_vida = AssetController().get_asset('hud_vida')
        self.__key = AssetController().get_asset('key')
        self.__key_indisponivel = AssetController().get_asset('key_indisponivel')
        self.__luva = AssetController().get_asset('luva')
        self.__luva_indisponivel = AssetController().get_asset('luva_indisponivel')
        self.__faca = AssetController().get_asset('faca')
        self.__faca_indisponivel = AssetController().get_asset('faca_indisponivel')
        self.__seletor = AssetController().get_asset('seletor')
        self.__inventario = AssetController().get_asset('inventario')
        self.__display = pygame.display.get_surface()
        self.__debug = Debug()


    def draw(self, player, sala_atual):
        self.draw_timer_pilha(player.getLight().getPilha())
        self.draw_health(player.getHealth())
        self.draw_sala_atual(sala_atual)
        self.draw_se_tiver_chave(player.getKey())
        self.draw_inventario(self.__display, player.getInventory())
        self.draw_se_tiver_arma(player.get_weapon())

    def draw_se_tiver_arma(self, arma):
       # if isinstance(arma, ProjectileWeapon):
           # self.__display.blit(arma.getSprite(), (WIDTH - 100, HEIGTH - 100))
        # Desenha a luva
        self.__display.blit(self.__luva_indisponivel, (WIDTH - 100, HEIGTH - 100))
        self.__display.blit(self.__faca_indisponivel, (WIDTH - 100, HEIGTH - 200))
        if arma is not None and isinstance(arma, ProjectileWeapon):
            self.__display.blit(self.__luva, (WIDTH - 100, HEIGTH - 100))
            self.__display.blit(self.__seletor, (WIDTH - 100, HEIGTH - 100))
        elif arma is not None and isinstance(arma, MeleeWeapon):
            self.__display.blit(self.__faca, (WIDTH - 100, HEIGTH - 200))
            self.__display.blit(self.__seletor, (WIDTH - 100, HEIGTH - 200))





    def draw_inventario(self, surface, inventario):
        self.__rect = self.__inventario.get_rect()
        x = (WIDTH - self.__rect[2])/2
        y = HEIGTH - 70
        surface.blit(self.__inventario, (x, y))
        valor = self.__rect[2]/9
        for pos,item in enumerate(inventario.getItemList()):
            if isinstance(item, Item):
                item.draw(x, 650, valor, pos, surface)


    def draw_timer_pilha(self, pilha):
        if pilha.getStatus():
            pygame.draw.rect(self.__display, (0, 0, 255), (2, 15, pilha.getTamanho()[0] - 10, pilha.getTamanho()[1]))
            pygame.draw.rect(self.__display, (0, 255, 0), (2, 15, pilha.getTempoRestante()/6 - 10, pilha.getTamanho()[1]))
        else:
            pygame.draw.rect(self.__display, (255, 0, 0), (2, 15, pilha.getTamanho()[0] - 10, pilha.getTamanho()[1]))
        
        x_pilha = 0
        y_pilha = 0
        self.__display.blit(self.__hud_pilha, (x_pilha, y_pilha))
            
    def draw_health(self, vida):
        x = 690
        y = 0

        x_barra = x+15
        y_barra = y+15
        width_barra = self.__hud_vida.get_width() - 20

        gordura_da_barra = 15
        vida_maxima = 100
        pygame.draw.rect(self.__display, (255, 0, 0), (x_barra, y_barra, width_barra, gordura_da_barra))
        pygame.draw.rect(self.__display, (0, 255, 0), (x_barra, y_barra, (width_barra / vida_maxima) * vida, gordura_da_barra))
        self.__display.blit(self.__hud_vida, (x, y))

    def draw_sala_atual(self, sala_atual):
        x = 40
        y = 100
        self.__debug.debug('Sala', sala_atual , y, x, (255, 255, 255), (255, 255, 255))


    def draw_se_tiver_chave(self, chave):
        x = 40
        y = 160
        self.__debug.debug('Chave', '', y, x, (255, 255, 255), (255, 255, 255))
        if chave:
            self.__display.blit(self.__key, (x-8, y-15))
        else:
            self.__display.blit(self.__key_indisponivel, (x-8, y-15))


    def update(self, pilha, vida, sala_atual, player):
        self.draw(pilha, vida)
        self.draw_health(vida)
        self.draw_sala_atual(sala_atual)
        self.draw_se_tiver_chave(player.getKey())

