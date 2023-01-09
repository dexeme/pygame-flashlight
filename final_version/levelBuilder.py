from settings import *
from tile import Tile, Chao
from jogador import Jogador
from item import *
from key import Key
from door import Door
from pilha import Pilha
from hud import Hud
from enemyLowDMG import EnemyLowDMG
from enemyHighDMG import EnemyHighDMG
from ySortCameraGroup import YSortCameraGroup
from damageController import DamageController
from projectileWeapon import ProjectileWeapon
from meleeWeapon import MeleeWeapon
from assetController import AssetController


class LevelBuilder:

    def __init__(self):
        self.rooms = ROOMS

    def selected_floor(self, sala):
        if sala == 1:
            self.chao = pygame.image.load('tiles/chao.png').convert_alpha()
        if sala == 2:
            self.chao = pygame.image.load('tiles/chao1.png').convert_alpha()
        return self.chao
    

    def create_map(self, selected_room):
        self.__dmg_ctrl = DamageController()
        self.__hud = Hud()
        self.__key = ''
        self.__door = ''
        __chao = Chao((0, 0), f'tiles/chao{selected_room}.png')
        __visible_sprites = YSortCameraGroup()
        __obstacle_sprites = pygame.sprite.Group()
        __item_sprites = []
        __enemy_sprites = pygame.sprite.Group()
        __projectile_sprites = pygame.sprite.Group()
        __visible_sprites.add(__chao)
        for row_index, row in enumerate(self.rooms[selected_room]):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    tile = Tile((x, y), AssetController().get_asset('parede_vertical_esquerda'))
                    
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'm':
                    tile = Tile((x, y), AssetController().get_asset('parede_quina_direita_cima'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'n':
                    tile = Tile((x, y), AssetController().get_asset('parede_quina_esquerda_baixo'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'o':
                    tile = Tile((x, y), AssetController().get_asset('parede_quina_direita_baixo'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'j':
                    tile = Tile((x, y), AssetController().get_asset('parede_quina_esquerda_cima'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'a':
                    tile = Tile((x, y), AssetController().get_asset('parede'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'z':
                    tile = Tile((x, y), AssetController().get_asset('parede_com_corrente'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'i':
                    tile = Tile((x, y), AssetController().get_asset('parede_com_vaso'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                if col == 'q':
                    tile = Tile((x, y), AssetController().get_asset('parede_vertical_direita'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'h':
                    tile = Tile((x, y), AssetController().get_asset('parede_horizontal_baixo'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                if col == 'y':
                    tile = Tile((x, y), AssetController().get_asset('parede_horizontal_cima'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'p':
                    __player = Jogador((x, y))
                    __visible_sprites.add(__player)
                elif col == 'b':
                    battery = Pilha(x, y, 'pilha', 50)
                    __item_sprites.append(battery)
                    __visible_sprites.add(battery)
                elif col == 'l':
                    door = Door(x, y)
                    __visible_sprites.add(door)
                    __obstacle_sprites.add(door)
                    self.__door = door
                    __item_sprites.append(door)
                elif col == 'v':
                    tile = Tile((x, y), AssetController().get_asset('barril'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'c':
                    tile = Tile((x, y), AssetController().get_asset('porta_cima'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'k':
                    key = Key(x, y)
                    __visible_sprites.add(key)
                    __item_sprites.append(key)
                    self.__key = key
                elif col == 'f':
                    tile = Tile((x, y), AssetController().get_asset('porta_aberta_cima'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'w':
                    tile = Tile((x, y), AssetController().get_asset('porta_aberta'))
                    __visible_sprites.add(tile)
                    __obstacle_sprites.add(tile)
                elif col == 'el':
                    enemy = EnemyLowDMG((x, y))
                    __visible_sprites.add(enemy)
                    __enemy_sprites.add(enemy)
                elif col == 'eh':
                    enemy = EnemyHighDMG((x, y))
                    __visible_sprites.add(enemy)
                    __enemy_sprites.add(enemy)
                elif col.endswith('-lrwpn'):
                    name, damage, shot_speed, cooldown, type = col.split('-')
                    damage, shot_speed, cooldown = int(damage), int(shot_speed), int(cooldown)
                    weapon = ProjectileWeapon(x, y, name, damage, shot_speed, cooldown)
                    __visible_sprites.add(weapon)
                    __item_sprites.append(weapon)
                elif col.endswith('-mlwpn'):
                    name, dmg, _range, cooldown, type = col.split('-')
                    dmg, _range, cooldown = int(dmg), int(_range), int(cooldown)
                    weapon = MeleeWeapon(x, y, name, dmg, _range, cooldown)
                    __visible_sprites.add(weapon)
                    __item_sprites.append(weapon)
        self.__dmg_ctrl.update_characters(__enemy_sprites, __player)
        return __visible_sprites, __obstacle_sprites, __item_sprites, __enemy_sprites, __projectile_sprites, __player

    def getKey(self):
        return self.__key

    def getDoor(self):
        return self.__door

    def getHud(self):
        return self.__hud
