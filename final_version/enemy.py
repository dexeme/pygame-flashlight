from character import Character
from abc import abstractmethod
from support import import_folder
from damageController import DamageController


class Enemy(Character):
    def __init__(self, health: int, pos: tuple, speed: float, sprite: str, damage: int, _range: int, cooldown):
        super().__init__(health, pos, speed, sprite, damage, _range)
        self.__player_pos = [10, 10]
        self.__status = Character.getStatus(self)
        self.import_enemy_assets()
        self.__dead = False
        self.__light_status = False
        self.__animation_speed = 0.04
        self.__cooldown = cooldown
    
    def attack(self):
        dmg_ctrl = DamageController()
        dmg_ctrl.melee_attack(self.getDamage(), self.getRange(), self.getStatus(), self)

    def update(self):
        self.cooldowns(attack_cooldown=self.__cooldown)
        self.reactToLight()
        self.animate()

    def getAnimationSpeed(self):
        return self.__animation_speed

    def light_info_update(self, player_pos: tuple, light_status: bool):
        self.__player_pos = player_pos
        self.__light_status = light_status

    def import_enemy_assets(self):
        # Vê se o inimigo é um enemyhighdmg ou um enemylowdmg
        if self.__class__.__name__ == 'EnemyHighDMG':
            character_path = 'graphics/enemyhighdmg/'
        else:
            character_path = 'graphics/enemylowdmg/'
        self.animations = {'left': [],'right': []}
        for animation in self.animations.keys():

            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def getStatus(self):
        return self.__status
            
    def animate(self):
        if self.getDirectionX() >= 0:
            self.__status = 'right'
        else:
            self.__status = 'left'            
        animation = self.animations[self.__status]

        #Loop de animação por frame
        self.setFrameIndex(self.getFrameIndex() + self.getAnimationSpeed())
        # Verifica se o frame atual é maior que o número de frames
        if self.getFrameIndex() >= len(animation):
            self.setFrameIndex(0)
        
        # Setando o frame atual
        self.setImage(animation[int(self.getFrameIndex())])
        self.setRect(self.getImage().get_rect(center = self.getHitbox().center))

    def getPlayerPos(self):
        return self.__player_pos

    def getLightStatus(self):
        return self.__light_status

    def die(self):
        self.__dead = True

    def getDead(self):
        return self.__dead

    @abstractmethod
    def reactToLight(self):
        pass
