from enemy import Enemy
from math import sqrt
from enemyLowDMG import EnemyLowDMG
from sound import Sound


class EnemyHighDMG(Enemy):

    def __init__(self, pos):
        super().__init__(health=1000, pos=pos, speed=3.2, sprite='enemyhighdmg', damage=100, _range=100, cooldown=2000)
        self.__confusion_counter = 0


    def reactToLight(self):
        posx, posy = self.getPlayerPos()
        diffx = posx - self.getPos()[0]
        diffy = posy - self.getPos()[1]
        dist = sqrt(diffx**2 + diffy**2)
        # RANGE DA LANTERNA:
        if (dist < 200) and self.getLightStatus():
            self.__confusion_counter = 100
        # DECISAO EM Y:
            if diffy >= 0:
                self.setDirectionY(-1)
                self.setStatus('up')
            else:
                self.setDirectionY(1)
                self.setStatus('down')
        # DECISAO EM X:
            if diffx >= 0:
                self.setDirectionX(-1)
                self.setStatus('left')
            else:
                self.setDirectionX(1)
                self.setStatus('right')
        # CONTADOR PARA CICLOS CONFUSO:
        elif self.__confusion_counter > 0:
            self.__confusion_counter -= 1
        # FORA DO RANGE DA LANTERNA:
        elif dist < 400:
            Sound().playMusic(requestor='eh')
            # DECISAO EM Y:
            if diffy > 0:
                self.setDirectionY(1)
                self.setStatus('down')
            elif diffx == 0:
                self.setDirectionY(0)
            else:
                self.setDirectionY(-1)
                self.setStatus('up')
            # DECISAO EM X:
            if diffx > 0:
                self.setDirectionX(1)
                self.setStatus('right')
            elif diffx == 0:
                self.setDirectionX(0)
            else:
                self.setDirectionX(-1)
                self.setStatus('left')
        else:
            self.setDirectionX(0)
            self.setDirectionY(0)

        # DETECCAO DO AUTO_ATAQUE (INACABADO - NAO ATACA COM A LANTERNA LIGADA):
        if dist < self.getRange() and not self.getLightStatus() and not self.getAttackingStatus():
            self.setAttackingStatus()
            self.setAttackTimer()
            self.attack()
            Sound().stopMusic(requestor='eh')
    def getBabies(self):
        baby1 = EnemyLowDMG((self.getPosX(), self.getPosY()))
        baby2 = EnemyLowDMG((self.getPosX()+20, self.getPosY()+20))
        baby3 = EnemyLowDMG((self.getPosX()+30, self.getPosY()+30))
        return [baby1, baby2, baby3]

    def die(self):
        Sound().stopMusic(requestor='eh')
        super().die()
