'''!
Lanceur de l'application EPI
@author: V. Verdon
@version: 20231120
'''

import sys
from PyQt5.QtWidgets import QApplication
from controller.MainCtrl import MainCtrl
from view.MainView import MainView
       
if __name__=='__main__':
    app=QApplication(sys.argv)
    ctrl = MainCtrl()
    view = MainView(ctrl)
    sys.exit(app.exec())
    
    