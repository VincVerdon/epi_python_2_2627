'''!
@author: V. Verdon
@version: 20231125
'''

class Manufacturer():
    '''
    Classe métier représentant les fabricants (manufacturers)
    '''
    
    def __init__(self, name:str=None, short_name:str=None, id:int=None ):
        '''
        Constructor
        '''
        self.__id = id
        self.__name = name
        self.__shortName = short_name
    
    
    def __str__(self) -> str:
        return "id = " + str(self.__id) + " ; name = " + str(self.__name) + " ; short name = " + str(self.__shortName)
    
    
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getShortName(self):
        return self.__shortName
    
    def setId(self, value):
        self.__id = value
        
    def setName(self, value):
        self.__name = value
        
    def setShortName(self, value):
        self.__shortName = value
        
        