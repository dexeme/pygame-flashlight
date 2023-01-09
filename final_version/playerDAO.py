from DAO import DAO

class PlayerDAO(DAO):
    def __init__(self):
        super().__init__('player.pkl')
        
    def add(self, key, obj):
        super().add(key, obj)

    def get(self, key):
        return super().get(key)