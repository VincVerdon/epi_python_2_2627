'''!
@author: V. Verdon
@version: 20231125
'''

import sys
#from view.MainView import MainView
from view.ManufacturerView import ManufacturerView
from controller.ManufacturerCtrl import ManufacturerCtrl


class MainCtrl():
    '''!
    Contrôleur gérant la fenêtre principe MainView
    @see view.MainView
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
    
    
    def manufacturerUI(self):
        '''!
        Affiche la vue de gestion des manufacturers
        @see view.ManufacturerView
        '''
        man_ctrl = ManufacturerCtrl()
        list = man_ctrl.getManufacturersList()
        self.__manView = ManufacturerView(man_ctrl, list)
        
        
    def quit(self):
        '''!
        Gestion de la fermeture
        Doit permettre l'arrêt de l'application
        @note: provisoire, il faudra gérer la fermeture de l'appli plus proprement
        '''
        sys.exit(0)