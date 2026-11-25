import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QFrame, QGraphicsDropShadowEffect,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connexion")
        self.resize(1280, 720)
        self.bg = QPixmap("/var/www/html/dev/epi_python_2_2627/rendu_graphique/Rendu fond.png")

        root = QHBoxLayout(self)
        root.setContentsMargins(40, 40, 40, 40)
        root.addStretch(1)

        card = QFrame()
        card.setObjectName("card")
        card.setFixedWidth(470)
        ombre = QGraphicsDropShadowEffect(card)
        ombre.setBlurRadius(40)
        ombre.setOffset(0, 8)
        ombre.setColor(QColor(15, 47, 94, 45))
        card.setGraphicsEffect(ombre)

        lay = QVBoxLayout(card)
        lay.setContentsMargins(38, 36, 38, 32)

        titre = QLabel("Connexion")
        titre.setObjectName("titre")
        titre.setAlignment(Qt.AlignCenter)
        lay.addWidget(titre)
        lay.addSpacing(20)

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Identifiant")
        lay.addWidget(self.login_input)
        lay.addSpacing(14)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mot de passe")
        lay.addWidget(self.password_input)
        lay.addSpacing(22)

        self.login_btn = QPushButton("Se connecter")
        self.login_btn.setObjectName("loginBtn")
        self.login_btn.setCursor(Qt.PointingHandCursor)
        lay.addWidget(self.login_btn)
        lay.addSpacing(18)

        self.register_btn = QPushButton("Créer un compte")
        self.register_btn.setObjectName("registerBtn")
        self.register_btn.setCursor(Qt.PointingHandCursor)
        lay.addWidget(self.register_btn, alignment=Qt.AlignCenter)

        root.addWidget(card, 1, Qt.AlignCenter)

        self.setStyleSheet("""
            QFrame#card { background: white; border-radius: 18px; }
            QLabel#titre { font-size: 32px; font-weight: bold; color: #0F2F5E; }
            QLineEdit { border: 1px solid #D5DBE5; border-radius: 8px; padding: 14px 10px; font-size: 15px; }
            QLineEdit:focus { border: 1px solid #0F2F5E; }
            QPushButton#loginBtn { background: #0F2F5E; color: white; border: none;
                                   border-radius: 8px; padding: 15px; font-size: 16px; font-weight: bold; }
            QPushButton#loginBtn:hover { background: #16407F; }
            QPushButton#registerBtn { background: transparent; border: none; color: #0F2F5E;
                                      font-size: 15px; font-weight: bold; text-decoration: underline; }
        """)

    def paintEvent(self, event):
        img = self.bg.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        QPainter(self).drawPixmap((self.width() - img.width()) // 2,
                                  (self.height() - img.height()) // 2, img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    page = LoginPage()
    page.show()
    sys.exit(app.exec_())