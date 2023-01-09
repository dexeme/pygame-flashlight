from weapon import Weapon
from Projectile import Projectile


class ProjectileWeapon(Weapon):

    def __init__(self, x, y, name, damage, shot_speed, cooldown):
        super().__init__(x, y, name, cooldown)
        self.__name = name
        self.__damage = damage
        self.__shot_speed = shot_speed

    def attack(self, attack_direction):
        if attack_direction == 'up' or attack_direction == 'up_idle':
            direction = (0, -1)
        elif attack_direction == 'down' or attack_direction == 'down_idle':
            direction = (0, 1)
        elif attack_direction == 'left' or attack_direction == 'left_idle':
            direction = (-1, 0)
        elif attack_direction == 'right' or attack_direction == 'right_idle':
            direction = (1, 0)
        return Projectile(f'{self.__name}_projectile', direction, self.__damage, self.__shot_speed)
