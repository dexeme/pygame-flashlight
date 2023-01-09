from abc import ABC, abstractmethod


class AbstractPickable:
    def __init__(self, dao):
        self.__dao = dao
    
    def getDAO(self):
        return self.__dao
    
    @abstractmethod
    def fromPickles(self):
        pass

    @abstractmethod
    def toPickles(self, key):
        pass