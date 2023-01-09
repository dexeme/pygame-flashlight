from item import Item

class Door(Item):
    def __init__(self, x, y):
        super().__init__(x, y, 'porta')
        
    def use(self, jogador):
        pass
    