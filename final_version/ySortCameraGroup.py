import pygame


class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        # Setup
        super().__init__()
        self.__display_surface = pygame.display.get_surface()
        self.__half_width = self.__display_surface.get_size()[0] / 2
        self.__half_height = self.__display_surface.get_size()[1] / 2
        self.__offset = pygame.math.Vector2()

    

    def custom_draw(self, jogador):
        # Pegando offset
        self.__offset.x = jogador.getRect().centerx - self.__half_width
        self.__offset.y = jogador.getRect().centery - self.__half_height
        # Desenhando sprites
        for sprite in self.sprites():
            offset_pos = sprite.getRect().topleft - self.__offset
            self.__display_surface.blit(sprite.getImage(), offset_pos)
