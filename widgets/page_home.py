from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt

class HomePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Üst başlık (isim yazan yer)
        header = QLabel("")
        header.setStyleSheet("font-size: 20px; font-weight: bold; color: #00ff00;")
        header.setAlignment(Qt.AlignLeft)

        title = QLabel("🔑 SafeCrypt Pro • Güvenli Şifreleme Sistemleri")
        title.setStyleSheet("font-size: 26px; font-weight: bold; color: #00ff00;")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Lütfen yapmak istediğiniz işlemi seçin:")
        subtitle.setStyleSheet("font-size: 14px;")
        subtitle.setAlignment(Qt.AlignCenter)

        # SHA512 kutusu
        sha_frame = QFrame()
        sha_layout = QVBoxLayout()
        sha_icon = QLabel("🔐")
        sha_icon.setAlignment(Qt.AlignCenter)
        sha_label = QLabel("SHA-512")
        sha_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        sha_label.setAlignment(Qt.AlignCenter)
        sha_text = QLabel("SHA-512 özetleme işlemi ile veri bütünlüğünü sağlayın.")
        sha_text.setWordWrap(True)
        sha_text.setAlignment(Qt.AlignCenter)
        sha_btn = QPushButton("📄 SHA-512 Hash")
        sha_btn.clicked.connect(lambda: main_window.stack.setCurrentWidget(main_window.page_sha))
        sha_layout.addWidget(sha_icon)
        sha_layout.addWidget(sha_label)
        sha_layout.addWidget(sha_text)
        sha_layout.addWidget(sha_btn)
        sha_frame.setLayout(sha_layout)
        sha_frame.setStyleSheet("QFrame { border: 2px solid #00ff00; border-radius: 10px; padding: 10px; }")

        # ECC kutusu
        ecc_frame = QFrame()
        ecc_layout = QVBoxLayout()
        ecc_icon = QLabel("🔑")
        ecc_icon.setAlignment(Qt.AlignCenter)
        ecc_label = QLabel("ECC")
        ecc_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        ecc_label.setAlignment(Qt.AlignCenter)
        ecc_text = QLabel("ECC algoritması ile metin şifreleyin ve çözün.")
        ecc_text.setWordWrap(True)
        ecc_text.setAlignment(Qt.AlignCenter)
        ecc_btn = QPushButton("🔒 ECC Şifrele / Çöz")
        ecc_btn.clicked.connect(lambda: main_window.stack.setCurrentWidget(main_window.page_ecc))
        ecc_layout.addWidget(ecc_icon)
        ecc_layout.addWidget(ecc_label)
        ecc_layout.addWidget(ecc_text)
        ecc_layout.addWidget(ecc_btn)
        ecc_frame.setLayout(ecc_layout)
        ecc_frame.setStyleSheet("QFrame { border: 2px solid #00ff00; border-radius: 10px; padding: 10px; }")

        # Kartları yatay sırala
        box_row = QHBoxLayout()
        box_row.addWidget(sha_frame)
        box_row.addWidget(ecc_frame)

        # Hepsini sırala
        layout.addWidget(header)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(box_row)

        self.setLayout(layout)
