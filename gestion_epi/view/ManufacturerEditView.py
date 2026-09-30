'''!
@author: V. Verdon
@version: 20231125
'''

from PyQt5.QtWidgets import QPushButton,QGridLayout, QWidget,\
    QLabel, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.Qt import QIcon, Qt
from model.Manufacturer import Manufacturer


class ManufacturerEditView(QWidget):
    '''
    Vue permettant la création où la modification d'un manufacturer
    '''
    
    def __init__(self, ctrl, update:bool=False):
        '''
        Constructor
        '''
        super().__init__()
        #stockage du contrôleur
        self.__ctrl = ctrl
        
        #parametrage de la fenetre
        self.setWindowTitle("Edition des fabricants")
        #self.resize(400,300)
        #Ajout d'un icône
        win_ico = QIcon("icons/epi.png")
        self.setWindowIcon(win_ico)
        
        #Contenu fenêtre
        self.__centralLay = QVBoxLayout()
        self.setLayout(self.__centralLay)
        self.__gridLay =  QGridLayout()
        self.__centralLay.addLayout(self.__gridLay)
        lId = QLabel("Numéro : ")
        lName = QLabel("Nom : ")
        lSName = QLabel("Nom court : ")
        self.__gridLay.addWidget(lName, 1, 0, Qt.AlignRight)
        self.__gridLay.addWidget(lSName, 2, 0, Qt.AlignRight)
        self.__edId = QLineEdit()
        self.__edName = QLineEdit()
        self.__edSName = QLineEdit()
        self.__gridLay.addWidget(self.__edName, 1, 1)
        self.__gridLay.addWidget(self.__edSName, 2, 1)
        if update :
            #Cas où on est en modification pas en création
            self.__gridLay.addWidget(lId, 0, 0, Qt.AlignRight)
            self.__gridLay.addWidget(self.__edId, 0, 1)
        
        self.__buttonLay = QHBoxLayout()
        self.__centralLay.addLayout(self.__buttonLay)
        self.__butValid = QPushButton("OK")
        self.__butAbort = QPushButton("Annuler")
        self.__buttonLay.addWidget(self.__butValid)
        self.__buttonLay.addWidget(self.__butAbort)
        
        #Gestion des événements pour les différentes actions
        self.__butAbort.clicked.connect(self.__ctrl.destroyManufacturerEditUI)
        if update :
            self.__butValid.clicked.connect(self.__ctrl.updateManufacturerProcess)
        else :
            self.__butValid.clicked.connect(self.__ctrl.createManufacturerProcess)
        
        #Affichage vue
        self.show()
    
    
    def getManufacturer(self)->Manufacturer:
        '''!
        Permet de récupérer le manufacturer qui a été édité
        @return: manufacturer créé / modifié
        '''
        return Manufacturer(self.__edName.text(), self.__edSName.text(), self.__edId.text())
    
    
        