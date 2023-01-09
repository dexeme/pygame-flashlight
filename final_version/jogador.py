import pygame
from inventory import Inventory
from lanterna import Lanterna
from character import Character
from damageController import DamageController
from meleeWeapon import MeleeWeapon
from projectileWeapon import ProjectileWeapon
from support import import_folder
from weapon import Weapon
from playerPickable import PlayerPickable


class Jogador(Character):
    def __init__(self, pos):
        super().__init__(health=100, pos=pos, speed=5, sprite='player', damage=100, _range=100)
        self.import_player_assets()
        self.__inventory = Inventory()
        self.__weapon = None
        self.__dead = False
        self.__light = Lanterna((self.getHitbox().x, self.getHitbox().y))

    def attack(self):
        dmg_ctrl = DamageController()
        if not self.getAttackingStatus():
            self.setAttackTimer()
            if self.__weapon is None:
                    dmg_ctrl.melee_attack(self.getDamage(), self.getRange(), self.get_status())
            else:
                projectile = self.__weapon.attack(self.getStatus())
                if projectile is not None:
                    projectile.setPos(self.getPos())
                return projectile

    def setWeapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.__weapon = weapon

    def import_player_assets(self):
        character_path = 'graphics/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
            'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
            'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[],
            'right_attack_pistol':[],'left_attack_pistol':[],'up_attack_pistol':[],'down_attack_pistol':[],
            'right_attack_knife':[],'left_attack_knife':[],'up_attack_knife':[],'down_attack_knife':[]}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
        
    def getInventory(self):
        return self.__inventory
    

    #Se for tomar dano passar vida como parametro negativo
    def tomar_Dano_ou_curar_vida(self, vida):
        if self.getHealth() + vida > 100:
            self.setHealth(100)
        else:
            self.setHealth(self.getHealth() + vida)
        if self.getHealth() <= 0:
            self.die()
        elif self.getHealth() > 100:
            self.setHealth(100)
            #attack_pistol_left.png
    
    def get_status(self):
        #Idle status
        if self.getDirectionX() == 0 and self.getDirectionY() == 0:
            if not 'idle' in self.getStatus() and not 'attack' in self.getStatus():
                self.setStatus(self.getStatus() + '_idle')
        #Attack status
        if self.getAttackingStatus():
            self.setDirectionX(0)
            self.setDirectionY(0)
            if not 'attack' in self.getStatus():
                if 'idle' in self.getStatus():
                    if self.__weapon is not None and isinstance(self.__weapon, ProjectileWeapon):
                        self.setStatus(self.getStatus().replace('_idle','_attack_pistol'))
                    elif self.__weapon is not None and isinstance(self.__weapon, MeleeWeapon):
                        self.setStatus(self.getStatus().replace('_idle','_attack_knife'))
                    elif self.__weapon is None:
                        self.setStatus(self.getStatus().replace('_idle','_attack'))
                else:
                    if self.__weapon is not None and isinstance(self.__weapon, ProjectileWeapon):
                        self.setStatus(self.getStatus() + '_attack_pistol')
                    elif self.__weapon is not None and isinstance(self.__weapon, MeleeWeapon):
                        self.setStatus(self.getStatus() + '_attack_knife')
                    elif self.__weapon is None:
                        self.setStatus(self.getStatus() + '_attack')
            ## 
        else:
            if 'attack_pistol' in self.getStatus():
                self.setStatus(self.getStatus().replace('_attack_pistol',''))
            elif 'attack_knife' in self.getStatus():
                self.setStatus(self.getStatus().replace('_attack_knife',''))
            if 'attack' in self.getStatus():
                self.setStatus(self.getStatus().replace('_attack',''))
      
        
    def draw(self):
        surface = pygame.display.get_surface()
        self.__light.draw(surface)


    def animate(self):
        animation = self.animations[self.getStatus()]
        self.setFrameIndex(self.getFrameIndex() + self.getAnimationSpeed())
        if self.getFrameIndex() >= len(animation):
            self.setFrameIndex(0)
        self.setImage(animation[int(self.getFrameIndex())])
        self.rect = self.getImage().get_rect(center = self.getHitbox().center)
        
    def update(self):
        if self.__weapon is not None:
            self.cooldowns(self.__weapon.getAttackCooldown())
        else:
            self.cooldowns()
        self.get_status()
        self.animate()
        self.__light.update()
    
    def loadInventory(self):
        self.__inventory, self.__weapon = PlayerPickable().fromPickles()

    def saveInventory(self):
        PlayerPickable().toPickles(self)

    def getLight(self):
        return self.__light

    def get_weapon(self):
        return self.__weapon
    
    def getDead(self):
        return self.__dead
    
    def die(self):
        self.__dead = True
    