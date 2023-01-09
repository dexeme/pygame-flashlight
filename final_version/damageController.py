from singletonMeta import SingletonMeta
from math import sqrt
from character import Character


class DamageController(metaclass=SingletonMeta):
    
    def __init__(self):
        self.__enemies = None
        self.__player = None

    def update_characters(self, enemies, player):
        self.__enemies = enemies
        self.__player = player

    def melee_attack(self, damage, attack_range, attack_direction, attacker='player'):
        if attacker == 'player':
            enemies = self.__enemies
            attacker = self.__player
        else:
            enemies = [self.__player]
            if isinstance(attacker, Character):
                attacker = attacker
            else:
                return 0
        for enemy in enemies:
            x, y = enemy.getPos()
            x1, y1 = attacker.getPos()
            diffx = x - x1
            diffy = y - y1
            if (attack_direction == 'up' and diffy) > 0 or (attack_direction == 'down' and diffy) < 0 or (
                    attack_direction == 'left' and diffx > 0) or (attack_direction == 'right' and diffx < 0):
                continue
            dist = sqrt(diffx**2 + diffy**2)
            if dist <= attack_range:
                enemy.receiveDamage(damage)

    @staticmethod
    def projectile_damage(projectile, enemy):
        dmg = projectile.getDamage()
        enemy.receiveDamage(dmg)
