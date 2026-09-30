'''!
@author: V. Verdon
@version: 20231125
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton,QGridLayout, QMenuBar, QMenu, QWidget,\
    QLabel, QToolBar, QScrollArea, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.Qt import QIcon, Qt, QInputDialog
from model.Manufacturer import Manufacturer
from controller.ManufacturerCtrl import ManufacturerCtrl


class ManufacturerView(QMainWindow):
    '''
    Vue principale affichant la liste des manufacturers et permettant ajout et modif
    '''
    
    def __init__(self, ctrl:ManufacturerCtrl, manufacturersList:dict):
        '''
        Constructor
        '''
        super().__init__()
        #stockage du contrôleur
        self.__ctrl = ctrl
        
        #parametrage de la fenetre
        self.setWindowTitle("Gestion des fabricants")
        
        #Ajout d'un icône
        win_ico = QIcon("icons/epi.png")
        self.setWindowIcon(win_ico)
        
        #Toolbar
        self.__bar = QToolBar("Barre d'outils")
        self.addToolBar(self.__bar)
        self.__actionNew = self.__bar.addAction(QIcon("icons/new.png"),"&Ajouter fabricant")
        self.__actionMod = self.__bar.addAction(QIcon("icons/edit.png"),"&Modifier fabricant")
        self.__actionDel = self.__bar.addAction(QIcon("icons/delete.png"),"&Supprimer fabricant")
        
        #Gestion des événements pour les différentes actions
        self.__actionNew.triggered.connect(self.__ctrl.createManufacturerUI)
        self.__actionMod.triggered.connect(self.__ctrl.updateManufacturerUI)
        self.__actionDel.triggered.connect(self.__ctrl.deleteManufacturerUI)
        
        #zone centrale
        self.__grid = QTableWidget(self)
        self.setCentralWidget(self.__grid)
        self.__grid.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.__grid.setColumnCount(3)
        self.__grid.setHorizontalHeaderLabels(["numéro", "nom", "Nom court"])
        self.__grid.verticalHeader().setVisible(False)
        
        '''
        self.__grid = QWidget()
        self.__gridLay =  QGridLayout()
        self.__grid.setLayout(self.__gridLay)
        
        #__scroll
        self.__scroll = QScrollArea()
        self.__scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.__scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__scroll.setWidgetResizable(True)
        self.__scroll.setWidget(self.__grid)
        self.setCentralWidget(self.__scroll)
        
        lIdT = QLabel("Numéro")
        lIdT.setStyleSheet("font-weight:bold")
        lNameT = QLabel("Nom")
        lNameT.setStyleSheet("font-weight:bold")
        lSNameT = QLabel("Nom court")
        lSNameT.setStyleSheet("font-weight:bold")
        self.__gridLay.addWidget(lIdT, 0, 0, Qt.AlignCenter)
        self.__gridLay.addWidget(lNameT, 0, 1, Qt.AlignCenter)
        self.__gridLay.addWidget(lSNameT, 0, 2, Qt.AlignCenter)
        '''
        
        #Chargement de la liste dans la grille
        self.displayList(manufacturersList)
        
        #Affichage vue
        self.show()
        
        
    def addRow(self, man:Manufacturer):
        '''!
        Ajout d'une ligne dans la liste des manufacturers à afficher
        '''
        row = self.__grid.rowCount()
        self.__grid.setRowCount(row + 1)
        #self.__grid.setItem(row, 0, QTableWidgetItem(str(man.getId())))
        self.__grid.setCellWidget(row, 0, QPushButton(str(man.getId())))
        self.__grid.setItem(row, 1, QTableWidgetItem(man.getName()))
        self.__grid.setItem(row, 2, QTableWidgetItem(man.getShortName()))
        
        
        '''
        row = self.__gridLay.rowCount()  
        lId = QLabel(str(man.getId()))
        lName = QLabel(man.getName())
        lShortName = QLabel(man.getShortName())
        self.__buttonDel = QPushButton("Supprimer")
        self.__buttonDel.num = man.getId()
        self.__buttonMod = QPushButton("Modifier")
        self.__buttonMod.num = man.getId()
        self.__buttonMod.clicked.connect(self.__ctrl.updateManufacturerUI)
        self.__buttonDel.clicked.connect(self.__ctrl.deleteManufacturerUI)
        self.__gridLay.addWidget(lId, row, 0, Qt.AlignCenter)
        self.__gridLay.addWidget(lName, row, 1, Qt.AlignLeft)
        self.__gridLay.addWidget(lShortName, row, 2, Qt.AlignLeft)
        self.__gridLay.addWidget(self.__buttonMod, row, 3, Qt.AlignLeft)
        self.__gridLay.addWidget(self.__buttonDel, row, 4, Qt.AlignLeft)
        '''
        
        
    def displayList(self,list:dict):
        '''!
        Affiche la liste des manufacturers à l'écran
        '''
        for man in list:
            self.addRow(man)
            
        self.__grid.resizeColumnsToContents()
            
        