'''!
@author: V. Verdon
@version: 20231128
'''

import requests
import json
import config.config_api as CONF


class Api():
    '''!
    Classe fournissant les méthodes génériques 
    pour se connecter à l'API REST distante
    @note: Créer des classes enfant pour s'en servir
    '''
    
    def __init__(self):
        '''!
        Penser à appeler ce constructeur depuis la classe enfant
        '''
        
        self._url = CONF.HOST + CONF.API_DIR
    
    
    def _get(self, route:str):
        '''!
        Méthode générique pour lire des objets depuis l'API
        '''
        res = None
        url = self._url + "/" + route
        response = requests.get(url)
        if response.ok:
            res = json.loads(response.content)
        return res
       
        
    def _post(self, route:str, datas:json):
        '''!
        Méthode générique pour envoyer un nouvel objet à l'API
        '''
        res = None
        url = self._url + "/" + route
        response = requests.post(url, datas)
        if response.ok:
            res = True
        return res
    
    
    def _put(self, route:str, datas:json, id:int):
        '''!
        Méthode générique  pour envoyer une modification d'objet à l'API
        '''
        res = None
        url = self._url + "/" + route + "/" + str(id)
        response = requests.put(url, datas)
        if response.ok:
            res = True
        return res
    
    
    def _del(self, route:str, id:int):
        '''!
        Méthode générique pour envoyer une suppression d'objet à l'API
        '''
        res = None
        url = self._url + "/" + route + "/" + str(id)
        response = requests.delete(url)
        if response.ok:
            res = True
        return res
    
