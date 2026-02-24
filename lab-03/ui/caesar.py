from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 340)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(0, 10, 520, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")

        # Plain Text
        self.lbl_plain = QtWidgets.QLabel(self.centralwidget)
        self.lbl_plain.setGeometry(QtCore.QRect(30, 60, 100, 20))
        self.lbl_plain.setObjectName("lbl_plain")

        self.txt_plain = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_plain.setGeometry(QtCore.QRect(140, 55, 350, 30))
        self.txt_plain.setObjectName("txt_plain")

        # Cipher Text
        self.lbl_cipher = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cipher.setGeometry(QtCore.QRect(30, 110, 100, 20))
        self.lbl_cipher.setObjectName("lbl_cipher")

        self.txt_cipher = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cipher.setGeometry(QtCore.QRect(140, 105, 350, 30))
        self.txt_cipher.setObjectName("txt_cipher")

        # Key
        self.lbl_key = QtWidgets.QLabel(self.centralwidget)
        self.lbl_key.setGeometry(QtCore.QRect(30, 160, 100, 20))
        self.lbl_key.setObjectName("lbl_key")

        self.txt_key = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(140, 155, 350, 30))
        self.txt_key.setObjectName("txt_key")

        # Buttons
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(140, 220, 350, 35))
        self.btn_encrypt.setObjectName("btn_encrypt")

        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(140, 270, 350, 35))
        self.btn_decrypt.setObjectName("btn_decrypt")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caesar Cipher"))
        self.lbl_title.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.lbl_plain.setText(_translate("MainWindow", "Plain Text:"))
        self.lbl_cipher.setText(_translate("MainWindow", "Cipher Text:"))
        self.lbl_key.setText(_translate("MainWindow", "Key:"))
        self.txt_plain.setPlaceholderText(_translate("MainWindow", "Plain text"))
        self.txt_cipher.setPlaceholderText(_translate("MainWindow", "Cipher text"))
        self.txt_key.setPlaceholderText(_translate("MainWindow", "Key (number)"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
