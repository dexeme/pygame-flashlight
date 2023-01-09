from playerDAO import PlayerDAO
from abstractPickable import AbstractPickable
from item import Item

class PlayerPickable(AbstractPickable):
    def __init__(self):
        super().__init__(PlayerDAO())
        
    def fromPickles(self):
        inventory = self.getDAO().get('inventory')
       
        for item in inventory.getItemList():
            if isinstance(item, Item):
                item.setImage(True)
        
        weapon = self.getDAO().get('weapon')
        if isinstance(weapon, Item):
            weapon.setImage(True)
        
        return inventory, weapon
        
    def toPickles(self, player):
        inventory = player.getInventory()
        for item in inventory.getItemList():
            if isinstance(item, Item):
                item.setImage(False)
        
        
        weapon = player.get_weapon()
        if isinstance(weapon, Item):
            weapon.setImage(False)
        
        self.getDAO().add('inventory', inventory)
        self.getDAO().add('weapon', weapon)