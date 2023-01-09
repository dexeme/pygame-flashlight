import pygame
import pygame_widgets

from pygame_widgets.slider import Slider
from interfaces.abstractScreen import AbstractScreen
from interfaces.button import Button
from sound import Sound

class OptionsScreen(AbstractScreen):
    def __init__(self):
        buttons = pygame.sprite.Group([Button(150, 75, 'interfaces\Botoes\\botao_voltar_hover.png', 
                                                       'interfaces\Botoes\\botao_voltar.png',
                                                       'interfaces\Botoes\\botao_voltar_pressed.png', 'voltar')],
                                      [Button(375, 600, 'interfaces\Botoes\\botao_apply_hover.png', 
                                                       'interfaces\Botoes\\botao_apply.png',
                                                       'interfaces\Botoes\\botao_apply_pressed.png', 'apply')])
        super().__init__(pygame.display.get_surface(), 'interfaces\\telaOptions.png', buttons)
        
        self.__slider = Slider(self.getScreen(), 175, 300, 400, 30, colour = (225, 215, 208), handleColour = (132, 116, 110))

    def update(self):
        self.getButtons().update()
        pygame_widgets.update(pygame.event.get())
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.getButtons().draw(self.getScreen())
        self.__slider.draw()

    def getSlider(self):
        return self.__slider