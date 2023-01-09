#Classe para printar informações de debug na tela
#
import pygame
import pygame.freetype 

class Debug:
    def __init__(self):
        self.__font = pygame.font.Font('fonte/fonte_debug.ttf', 14)


    def debug(self, titulo, info, y, x, corTitulo, corInfo):
        display_surface = pygame.display.get_surface()
        debug_first_content = self.__font.render(str(info), True, corInfo)
        debug_second_content = self.__font.render(str(titulo), True, corTitulo)
        debug_rect = debug_first_content.get_rect(topleft=(x, y))
        
        pygame.draw.rect(display_surface, 'Black', debug_rect)
        display_surface.blit(debug_first_content, debug_rect)
        display_surface.blit(debug_second_content, (x, y-20))



