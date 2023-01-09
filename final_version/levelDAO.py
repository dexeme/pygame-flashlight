from DAO import DAO

class LevelDAO(DAO):
    def __init__(self):
        super().__init__('level.pkl')
        
    def add(self, level):
        super().add('selected_room', level.getSelectRoom())

    def get(self, key):
        return super().get(key)