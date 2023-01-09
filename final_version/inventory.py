from item import Item


class Inventory():
    def __init__(self):
        self.__item_list = [None]*9

    def setItemList(self, item_list):
        self.__item_list = item_list
    
    def getItemList(self):
        return self.__item_list
    
    def use_item(self, id, jogador):
        if isinstance(self.__item_list[id-1], Item):
            self.__item_list[id-1].use(jogador)
            self.__item_list[id-1] = None
    
    def add_item(self, item):
        for pos, espaco in enumerate(self.__item_list):
            if espaco == None:
                self.__item_list[pos] = item
                return True
        return False
