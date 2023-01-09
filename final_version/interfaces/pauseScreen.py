import pygame

from interfaces.abstractScreen import AbstractScreen
from interfaces.button import Button

class PauseScreen(AbstractScreen):
    def __init__(self):
        buttons = pygame.sprite.Group(
            [Button(1030, 250, 'interfaces\Botoes\\botao_restart_hover.png',
                             'interfaces\Botoes\\botao_restart.png', 
                             'interfaces\Botoes\\botao_restart_pressed.png', 'restart')],
            [Button(1030, 350, 'interfaces\Botoes\\botao_continue_hover.png',
                             'interfaces\Botoes\\botao_continue.png', 
                             'interfaces\Botoes\\botao_continue_pressed.png', 'continue')],
            [Button(1030, 450, 'interfaces\Botoes\\botao_options_hover.png',
                             'interfaces\Botoes\\botao_options.png', 
                             'interfaces\Botoes\\botao_options_pressed.png', 'options')],
            [Button(1030, 550, 'interfaces\Botoes\\botao_controls_hover.png',
                             'interfaces\Botoes\\botao_controls.png', 
                             'interfaces\Botoes\\botao_controls_pressed.png', 'controls')],
            [Button(1030, 650, 'interfaces\Botoes\\botao_mainmenu_hover.png',
                             'interfaces\Botoes\\botao_mainmenu.png', 
                             'interfaces\Botoes\\botao_mainmenu_pressed.png', 'mainmenu')])
        
        super().__init__(pygame.display.get_surface(), 'interfaces\\telaPause.png', buttons)

    def update(self):
        self.getButtons().update()
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.getButtons().draw(self.getScreen())
