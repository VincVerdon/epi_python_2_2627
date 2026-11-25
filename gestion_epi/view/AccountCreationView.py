import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QFrame, QGraphicsDropShadowEffect,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)


class CreationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Créer un compte")
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

        titre = QLabel("Créer un compte")
        titre.setObjectName("titre")
        titre.setAlignment(Qt.AlignCenter)
        lay.addWidget(titre)
        lay.addSpacing(16)

        self.prenom_input = self.champ(lay, "Prénom", "Votre prénom")
        self.nom_input = self.champ(lay, "Nom", "Votre nom")
        self.login_input = self.champ(lay, "Identifiant", "Choisissez un identifiant")
        self.password_input = self.champ(lay, "Mot de passe", "Choisissez un mot de passe")
        lay.addSpacing(10)

        self.create_btn = QPushButton("Créer mon compte")
        self.create_btn.setObjectName("createBtn")
        self.create_btn.setCursor(Qt.PointingHandCursor)
        lay.addWidget(self.create_btn)
        lay.addSpacing(14)

        self.back_btn = QPushButton("Retour à la connexion")
        self.back_btn.setObjectName("backBtn")
        self.back_btn.setCursor(Qt.PointingHandCursor)
        lay.addWidget(self.back_btn, alignment=Qt.AlignCenter)

        root.addWidget(card, 1, Qt.AlignCenter)

        self.setStyleSheet("""
            QFrame#card { background: white; border-radius: 18px; }
            QLabel#titre { font-size: 32px; font-weight: bold; color: #0F2F5E; }
            QLabel#label { font-size: 14px; font-weight: bold; color: #0F2F5E; }
            QLineEdit { border: 1px solid #D5DBE5; border-radius: 8px; padding: 12px 10px; font-size: 15px; }
            QLineEdit:focus { border: 1px solid #0F2F5E; }
            QPushButton#createBtn { background: #0F2F5E; color: white; border: none;
                                    border-radius: 8px; padding: 15px; font-size: 16px; font-weight: bold; }
            QPushButton#createBtn:hover { background: #16407F; }
            QPushButton#backBtn { background: transparent; border: none; color: #0F2F5E;
                                  font-size: 15px; text-decoration: underline; }
        """)

    def champ(self, lay, texte, placeholder):
        label = QLabel(texte)
        label.setObjectName("label")
        champ = QLineEdit()
        champ.setPlaceholderText(placeholder)
        lay.addWidget(label)
        lay.addWidget(champ)
        lay.addSpacing(8)
        return champ

    def paintEvent(self, event):
        img = self.bg.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        QPainter(self).drawPixmap((self.width() - img.width()) // 2,
                                  (self.height() - img.height()) // 2, img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    page = CreationPage()
    page.show()
    sys.exit(app.exec_())