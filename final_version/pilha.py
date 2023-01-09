from item import Item
from sound import Sound


class Pilha(Item):
    def __init__(self, x, y, sprite, nivel, status = True):
        super().__init__(x, y, sprite)
        self.__tempo_restante = nivel*30
        self.__tamanho = [nivel*5,10]
        self.__status = status
        self.__usando = False
    
    def getStatus(self):
        return self.__status
    
    def getTamanho(self):
        return self.__tamanho
    
    def getTempoRestante(self):
        return self.__tempo_restante
    
    def setUsando(self, usando):
        self.__usando = usando
    
    def getUsando(self):
        return self.__usando
    
    def use(self, jogador):
        jogador.getLight().setPilha(self)
        Sound().playSound('pilha')
        Sound().stopMusic(requestor='pilha')
        self.kill()
        return True
    
    def contador(self):
        if self.__usando:
            self.__tempo_restante -= 1
        
        if self.__tempo_restante == 0:
            self.__status = False
            Sound().playSound('sem_pilha')
            Sound().playMusic(requestor='pilha')
            return self.__status
