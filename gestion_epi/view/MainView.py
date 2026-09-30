'''!
@author: V. Verdon
@version: 20231125
'''

from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QVBoxLayout,\
    QGroupBox, QWidget, QMenuBar, QMenu
from PyQt5.Qt import QIcon

from controller.MainCtrl import MainCtrl

class MainView(QMainWindow):
    
    TITRE_FENETRE="GestionEPI"
    
    def __init__(self, ctrl:MainCtrl):
        #Appel du constructeur de la super classe QMainWindow
        super().__init__()
        #stockage du contrôleur
        self.__ctrl = ctrl
        
        #parametrage de la fenetre
        self.setWindowTitle(MainView.TITRE_FENETRE)
        #self.resize(400,300)
        #Ajout d'un icône
        win_ico = QIcon("icons/epi.png")
        self.setWindowIcon(win_ico)
        
        # Barre de menus
        self.__menub = QMenuBar()
        self.setMenuBar(self.__menub)
        
        # Menu 1
        self.__m1 = QMenu("&Fichier")
        self.__menub.addMenu(self.__m1)
        self.__act_quit = self.__m1.addAction(QIcon("icons/exit.png"),"&Quitter")
        # Menu 2
        self.__m2 = QMenu("&Gestion")
        self.__menub.addMenu(self.__m2)
        self.__actionCreateManUI = self.__m2.addAction(QIcon("icons/manage.png"),"Gestion &fabricants")
        
        #widgets de l'interface
        '''!
        @todo: ajout liste des matériels gérés en zone centrale
        '''
        
        #Gestion des événements pour les différentes actions des menus
        self.__actionCreateManUI.triggered.connect(self.__ctrl.manufacturerUI)
        self.__act_quit.triggered.connect(self.__ctrl.quit)
        
        #Affichage vue
        self.show()
    
    
    def closeEvent(self, event):
        '''!
        Gestion événement si l'on ferme la fenêtre en cliquant sur la croix
        '''
        self.__ctrl.quit()
        