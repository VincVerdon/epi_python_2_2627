'''!
@author: V. Verdon
@version: 20231125
'''

from api.ManufacturerApi import ManufacturerApi
from view.ManufacturerEditView import ManufacturerEditView
#from view.ManufacturerDialog import ManufacturerDialog
from PyQt5.Qt import QIcon, Qt, QInputDialog

class ManufacturerCtrl():
    '''!
    Contrôleur pour les vues manufacturer
    '''
        
    def getManufacturersList(self):
        '''!
        Récupère la liste des manufacturers
        '''
        api = ManufacturerApi()
        list_man = api.readAll()
        return list_man
    
    
    def createManufacturerUI(self):
        '''!
        Affichage fenêtre de création d'un nouveau manufacturer
        '''
        self.__manForm = ManufacturerEditView(self)
       
       
    def createManufacturerProcess(self):
        '''!
        Traitement des données de la fenêtre de création d'un manufacturer
        '''
        man = self.__manForm.getManufacturer()
        api = ManufacturerApi()
        api.create(man)
        self.__manForm.destroy()
    
    
    def updateManufacturerUI(self):
        '''!
        Affichage fenêtre d'update d'un manufacturer
        '''
        self.__manForm = ManufacturerEditView(self,True)
    
    
    def updateManufacturerProcess(self):
        '''!
        Traitement des données de la fenêtre d'update d'un manufacturer
        '''
        man = self.__manForm.getManufacturer()
        api = ManufacturerApi()
        api.update(man)
        self.__manForm.destroy()
    
        
    def destroyManufacturerEditUI(self):
        '''!
        Suppression fenêtre d'édition d'un manufacturer
        @see updateManufacturerUI
        @see createManufacturerUI
        '''
        self.__manForm.destroy()
    
    def deleteManufacturerUI(self):
        '''!
        Affichage fenêtre de suppression d'un manufacturer
        @todo A déplacer dans une vue...
        '''
        self.__manNum = 0
        res = QInputDialog.getInt(
            None,
            "Supprimer un fabricant",
            "Veuillez saisir le numéro du fabricant à supprimer",
            0,
            self.__manNum
            )
        
        if res[1]:
            self.__manNum = res[0]
            #print(str(self.__manNum))
            api = ManufacturerApi()
            api.delete(res[0])
            
        