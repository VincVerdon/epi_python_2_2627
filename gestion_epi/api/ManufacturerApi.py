'''!
@author: V. Verdon
@version: 20231125
'''

from api.Api import Api
from model.Manufacturer import Manufacturer


class ManufacturerApi(Api):
    '''!
    Classe donnant accès à l 'API REST distante 
    pour gestion des manufacturers
    '''

    def __init__(self):
        '''!
        Constructeur
        @note: appel du constructeur parent obligatoire !
        '''
        super().__init__()
        
    
    def readAll(self):
        '''!
        Récupère la liste des manufacturers
        '''
        res = self._get('manufacturers')
        listMan = []
        for man in res:
            listMan.append(Manufacturer(man["name"], man["short_name"], man["id"]))
        return listMan
    
    
    def create(self, man:Manufacturer):
        '''!
        Enregistre un nouveau manufacturer
        '''
        data = '{"name": "' + man.getName() + '", "short_name": "' + man.getShortName() + '"}'
        self._post('manufacturers', data)
    
    
    def update(self, man:Manufacturer):
        '''!
        Mise à jour d'un manufacturer
        '''
        data = '{"name": "' + man.getName() + '", "short_name": "' + man.getShortName() + '"}'
        self._put('manufacturers', data, man.getId())
    
    
    def delete(self, id:int):
        '''!
        Suppression d'un manufacturer
        '''
        self._del('manufacturers', id)
    
    
        