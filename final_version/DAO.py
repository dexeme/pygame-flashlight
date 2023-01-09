import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__objectCache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()
    
    def dump(self):
        pickle.dump(self.__objectCache, open(self.__datasource, 'wb'))
    
    def load(self):
        self.__objectCache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__objectCache[key] = obj
        self.dump()

    def get(self, key):
        try:
            return self.__objectCache[key]
        except KeyError as e:
            print(e)

    def remove(self, key):
        pass
    
    def get_all(self):
        return self.__objectCache.values()