import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow


API_BASE = "http://127.0.0.1:5001/api/rsa"


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def show_msg(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.exec_()

    def call_api_gen_keys(self):
        try:
            r = requests.get(f"{API_BASE}/generate_keys")
            self.show_msg(r.json().get("message", "Done"))
        except Exception as e:
            self.show_msg(str(e))

    def call_api_encrypt(self):
        try:
            payload = {
                "message": self.ui.txt_plain_text.toPlainText(),
                "key_type": "public"
            }
            r = requests.post(f"{API_BASE}/encrypt", json=payload)
            data = r.json()
            self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])
            self.show_msg("Encrypted Successfully")
        except Exception as e:
            self.show_msg(str(e))

    def call_api_decrypt(self):
        try:
            payload = {
                "ciphertext": self.ui.txt_cipher_text.toPlainText(),
                "key_type": "private"
            }
            r = requests.post(f"{API_BASE}/decrypt", json=payload)
            data = r.json()
            self.ui.txt_plain_text.setPlainText(data["decrypted_message"])
            self.show_msg("Decrypted Successfully")
        except Exception as e:
            self.show_msg(str(e))

    def call_api_sign(self):
        try:
            payload = {
                "message": self.ui.txt_info.toPlainText()
            }
            r = requests.post(f"{API_BASE}/sign", json=payload)
            data = r.json()
            self.ui.txt_sign.setPlainText(data["signature"])
            self.show_msg("Signed Successfully")
        except Exception as e:
            self.show_msg(str(e))

    def call_api_verify(self):
        try:
            payload = {
                "message": self.ui.txt_info.toPlainText(),
                "signature": self.ui.txt_sign.toPlainText()
            }
            r = requests.post(f"{API_BASE}/verify", json=payload)
            data = r.json()

            if data["is_verified"]:
                self.show_msg("Verified Successfully")
            else:
                self.show_msg("Verified Fail")

        except Exception as e:
            self.show_msg(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())