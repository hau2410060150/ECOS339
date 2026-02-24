import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow

API_BASE = "http://127.0.0.1:5001/api/caesar"   

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def _get_key_int(self) -> int:
        key_str = self.ui.txt_key.text().strip()
        if key_str == "":
            raise ValueError("Key không được để trống")
        if not key_str.lstrip("-").isdigit():
            raise ValueError("Key phải là số nguyên (ví dụ: 2)")
        return int(key_str)

    def call_api_encrypt(self):
        try:
            payload = {
                "plain_text": self.ui.txt_plain.text(),
                "key": self._get_key_int()
            }
            res = requests.post(f"{API_BASE}/encrypt", json=payload, timeout=10)
            data = res.json()

            if res.status_code != 200:
                raise Exception(data.get("error", "Encrypt error"))

            self.ui.txt_cipher.setText(data.get("encrypted_message", ""))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_decrypt(self):
        try:
            payload = {
                "cipher_text": self.ui.txt_cipher.text(),
                "key": self._get_key_int()
            }
            res = requests.post(f"{API_BASE}/decrypt", json=payload, timeout=10)
            data = res.json()

            if res.status_code != 200:
                raise Exception(data.get("error", "Decrypt error"))

            self.ui.txt_plain.setText(data.get("decrypted_message", ""))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())
