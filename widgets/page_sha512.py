from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QLabel, QVBoxLayout, QFileDialog, QHBoxLayout
from PyQt5.QtCore import Qt
from services.sha512_service import hash_text, hash_file

class Sha512Page(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Başlık
        title = QLabel("📄 SHA-512 Özeti Oluştur")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #00ff00;")
        title.setAlignment(Qt.AlignCenter)

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Lütfen özetini oluşturmak istediğiniz metni girin...")

        self.hash_button = QPushButton("🔐 Metni SHA-512 ile Özetle")
        self.hash_button.clicked.connect(self.hash_input)

        self.result_label = QLabel("🧪 Özet sonucu burada görünecek.")
        self.result_label.setWordWrap(True)

        self.file_button = QPushButton("📂 Dosya Seç ve Özetle")
        self.file_button.clicked.connect(self.hash_from_file)

        self.back_button = QPushButton("← Ana Sayfaya Dön")
        self.back_button.clicked.connect(lambda: main_window.stack.setCurrentWidget(main_window.page_home))

        # Butonları yatay diz
        button_row = QHBoxLayout()
        button_row.addWidget(self.hash_button)
        button_row.addWidget(self.file_button)

        layout.addWidget(title)
        layout.addWidget(QLabel("📝 Metin Girişi:"))
        layout.addWidget(self.text_input)
        layout.addLayout(button_row)
        layout.addWidget(QLabel("🔍 SHA-512 Çıktısı:"))
        layout.addWidget(self.result_label)
        layout.addStretch()
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def hash_input(self):
        text = self.text_input.toPlainText()
        digest = hash_text(text)
        self.result_label.setText(f"SHA-512 Özeti:\n{digest}")

    def hash_from_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Dosya Seç")
        if file:
            digest = hash_file(file)
            self.result_label.setText(f"Dosya Özeti:\n{digest}")

