import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)

API_URL = "http://127.0.0.1:5001/api/caesar"

class CaesarGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caesar Cipher")
        self.setFixedSize(520, 340)

        # UI
        self.plain_text = QLineEdit()
        self.plain_text.setPlaceholderText("Plain text")

        self.cipher_text = QLineEdit()
        self.cipher_text.setPlaceholderText("Cipher text")

        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Key (number)")

        self.btn_encrypt = QPushButton("Encrypt")
        self.btn_decrypt = QPushButton("Decrypt")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Plain Text"))
        layout.addWidget(self.plain_text)
        layout.addWidget(QLabel("Cipher Text"))
        layout.addWidget(self.cipher_text)
        layout.addWidget(QLabel("Key"))
        layout.addWidget(self.key_input)
        layout.addWidget(self.btn_encrypt)
        layout.addWidget(self.btn_decrypt)

        self.setLayout(layout)

        # Events
        self.btn_encrypt.clicked.connect(self.call_encrypt_api)
        self.btn_decrypt.clicked.connect(self.call_decrypt_api)

    # ===== CALL ENCRYPT API =====
    def call_encrypt_api(self):
        try:
            payload = {
                "plain_text": self.plain_text.text(),
                "key": int(self.key_input.text())
            }

            res = requests.post(f"{API_URL}/encrypt", json=payload)
            data = res.json()

            if res.status_code != 200:
                raise Exception(data.get("error", "Encrypt error"))

            self.cipher_text.setText(data["encrypted_message"])

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ===== CALL DECRYPT API =====
    def call_decrypt_api(self):
        try:
            payload = {
                "cipher_text": self.cipher_text.text(),
                "key": int(self.key_input.text())
            }

            res = requests.post(f"{API_URL}/decrypt", json=payload)
            data = res.json()

            if res.status_code != 200:
                raise Exception(data.get("error", "Decrypt error"))

            self.plain_text.setText(data["decrypted_message"])

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaesarGUI()
    window.show()
    sys.exit(app.exec_())
