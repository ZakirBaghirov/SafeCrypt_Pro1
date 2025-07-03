import os
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from services.ecc_service import generate_keys, save_keys, load_keys, encrypt_with_ecc, decrypt_with_ecc

class ECCPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Başlık
        title = QLabel("🔒 ECC Şifreleme ve Çözme")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #00ff00;")
        title.setAlignment(Qt.AlignCenter)

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Şifrelemek istediğiniz metni buraya yazın...")

        self.encrypt_button = QPushButton("🔐 Metni Şifrele")
        self.encrypt_button.clicked.connect(self.encrypt)

        self.encrypted_label = QLabel("🔎 Şifreli metin burada görünecek.")
        self.encrypted_label.setWordWrap(True)

        self.decrypt_button = QPushButton("🔓 Şifreyi Çöz")
        self.decrypt_button.clicked.connect(self.decrypt)

        self.decrypted_label = QLabel("✅ Çözülmüş metin burada görünecek.")
        self.decrypted_label.setWordWrap(True)

        self.generate_key_button = QPushButton("🗝️ Yeni ECC Anahtar Üret")
        self.generate_key_button.clicked.connect(self.generate_keys)

        self.back_button = QPushButton("← Ana Sayfaya Dön")
        self.back_button.clicked.connect(lambda: main_window.stack.setCurrentWidget(main_window.page_home))

        # Butonları yatay sırala
        button_row = QHBoxLayout()
        button_row.addWidget(self.encrypt_button)
        button_row.addWidget(self.decrypt_button)

        layout.addWidget(title)
        layout.addWidget(QLabel("📝 Şifrelenecek Metin:"))
        layout.addWidget(self.text_input)
        layout.addLayout(button_row)
        layout.addWidget(QLabel("🧪 Şifreli Metin:"))
        layout.addWidget(self.encrypted_label)
        layout.addWidget(QLabel("🔓 Çözülmüş Metin:"))
        layout.addWidget(self.decrypted_label)
        layout.addStretch()
        layout.addWidget(self.generate_key_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        # Anahtarlar
        if os.path.exists("keys/private.pem"):
            self.sk, self.vk = load_keys()
        else:
            self.sk, self.vk = generate_keys()
            save_keys(self.sk, self.vk)

        self.encrypted_key = ""
        self.encrypted_message = ""

    def encrypt(self):
        text = self.text_input.toPlainText()
        self.encrypted_key, self.encrypted_message = encrypt_with_ecc(text, self.vk)
        self.encrypted_label.setText(f"{self.encrypted_message[:100]}...")

    def decrypt(self):
        try:
            message = decrypt_with_ecc(self.encrypted_key, self.encrypted_message, self.vk)
            self.decrypted_label.setText(f"{message}")
        except Exception as e:
            self.decrypted_label.setText(f"Hata: {str(e)}")

    def generate_keys(self):
        self.sk, self.vk = generate_keys()
        save_keys(self.sk, self.vk)
        self.decrypted_label.setText("Yeni anahtar çifti oluşturuldu.")
