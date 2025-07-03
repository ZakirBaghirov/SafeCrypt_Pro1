from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QStackedWidget, QLabel,
    QPushButton, QHBoxLayout, QFrame, QMessageBox
)
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt
from widgets.page_home import HomePage
from widgets.page_sha512 import Sha512Page
from widgets.page_ecc import ECCPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SafeCrypt Pro - Güvenli Şifreleme Sistemleri")
        self.setGeometry(100, 100, 1000, 700)

        # Arka plan görseli ayarla
        palette = QPalette()
        background = QPixmap("assets/background.jpg")
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # Navbar
        navbar = QFrame()
        navbar.setFixedHeight(50)
        navbar.setStyleSheet("background-color: #000000;")
        nav_layout = QHBoxLayout(navbar)
        nav_layout.setContentsMargins(20, 0, 20, 0)
        nav_layout.setSpacing(40)

        # Sol taraf - adınız
        name_label = QLabel("🧑‍💻 Zakir Baghirov • SafeCrypt Pro")
        name_label.setStyleSheet("color: #00ff00; font-weight: bold; font-size: 16px;")
        nav_layout.addWidget(name_label)

        nav_layout.addStretch()

        # Orta menü - sayfa geçiş butonları
        home_btn = QPushButton("Ana Sayfa")
        sha_btn = QPushButton("SHA-512")
        ecc_btn = QPushButton("ECC")
        contact_btn = QPushButton("İletişim")

        for btn in [home_btn, sha_btn, ecc_btn, contact_btn]:
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #00ff00;
                    border: none;
                    font-size: 14px;
                }
                QPushButton:hover {
                    color: #ffffff;
                    font-weight: bold;
                }
            """)
            nav_layout.addWidget(btn)

        # Sayfalar
        self.stack = QStackedWidget()
        self.page_home = HomePage(self)
        self.page_sha = Sha512Page(self)
        self.page_ecc = ECCPage(self)

        self.stack.addWidget(self.page_home)
        self.stack.addWidget(self.page_sha)
        self.stack.addWidget(self.page_ecc)

        main_layout.addWidget(navbar)
        main_layout.addWidget(self.stack)

        # Varsayılan sayfa
        self.stack.setCurrentWidget(self.page_home)

        # Buton geçişleri
        home_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_home))
        sha_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_sha))
        ecc_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_ecc))
        contact_btn.clicked.connect(self.show_contact)

        # Tema stilleri
        self.setStyleSheet("""
            * {
                font-family: 'Segoe UI', sans-serif;
            }

            QWidget {
                background-color: transparent;
                color: #00ffcc;
                font-size: 16px;
            }

            QLabel {
                font-size: 16px;
            }

            QPushButton {
                background-color: rgba(0, 0, 0, 0.6);
                color: #00ffcc;
                border: 2px solid #00ffcc;
                padding: 10px;
                border-radius: 10px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #00ffcc;
                color: #000000;
                font-weight: bold;
            }

            QTextEdit, QLineEdit {
                background-color: rgba(30, 30, 30, 0.8);
                color: #00ffcc;
                border: 1px solid #00ffcc;
                padding: 5px;
            }
        """)

    def show_contact(self):
        contact_text = (
            "<b>İletişim Bilgileri</b><br><br>"
            "📧 <b>Email:</b> bagirovz2005@gmail.com<br>"
            "🔗 <b>LinkedIn:</b> <a href='https://www.linkedin.com/in/zakir-baghirov-ab4873233'>linkedin.com/in/zakir-baghirov</a><br>"
            "📸 <b>Instagram:</b> <a href='https://www.instagram.com/zakirrbagirov/'>@zakirrbagirov</a>"
        )
        msg = QMessageBox(self)
        msg.setWindowTitle("İletişim")
        msg.setTextFormat(Qt.RichText)
        msg.setText(contact_text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #0f0f0f;
                color: #00ffcc;
                font-size: 14px;
                font-family: Segoe UI;
            }
            QPushButton {
                background-color: #000;
                color: #00ffcc;
                border: 2px solid #00ffcc;
                padding: 5px 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #00ffcc;
                color: #000;
            }
        """)
        msg.exec_()