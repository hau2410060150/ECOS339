# -*- coding: utf-8 -*-
# File: ui/rsa.py
# Generated-style UI class (manual), compatible with: from ui.rsa import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 520)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ===== Main layout =====
        self.vbox_main = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vbox_main.setContentsMargins(18, 12, 18, 12)
        self.vbox_main.setSpacing(12)
        self.vbox_main.setObjectName("vbox_main")

        # ===== Header row =====
        self.hbox_header = QtWidgets.QHBoxLayout()
        self.hbox_header.setSpacing(10)
        self.hbox_header.setObjectName("hbox_header")

        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")

        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setMinimumSize(QtCore.QSize(140, 32))
        self.btn_gen_keys.setObjectName("btn_gen_keys")

        self.hbox_header.addWidget(self.lbl_title, 1)
        self.hbox_header.addWidget(self.btn_gen_keys, 0, QtCore.Qt.AlignTop)

        self.vbox_main.addLayout(self.hbox_header)

        # ===== Content row (2 columns) =====
        self.hbox_content = QtWidgets.QHBoxLayout()
        self.hbox_content.setSpacing(18)
        self.hbox_content.setObjectName("hbox_content")

        # ---------- LEFT COLUMN ----------
        self.left_col = QtWidgets.QVBoxLayout()
        self.left_col.setSpacing(10)
        self.left_col.setObjectName("left_col")

        # Plain Text
        self.hbox_plain = QtWidgets.QHBoxLayout()
        self.hbox_plain.setSpacing(10)
        self.hbox_plain.setObjectName("hbox_plain")

        self.lbl_plain = QtWidgets.QLabel(self.centralwidget)
        self.lbl_plain.setMinimumSize(QtCore.QSize(90, 0))
        self.lbl_plain.setObjectName("lbl_plain")

        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setMinimumHeight(110)
        self.txt_plain_text.setObjectName("txt_plain_text")

        self.hbox_plain.addWidget(self.lbl_plain, 0, QtCore.Qt.AlignTop)
        self.hbox_plain.addWidget(self.txt_plain_text, 1)

        # CipherText
        self.hbox_cipher = QtWidgets.QHBoxLayout()
        self.hbox_cipher.setSpacing(10)
        self.hbox_cipher.setObjectName("hbox_cipher")

        self.lbl_cipher = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cipher.setMinimumSize(QtCore.QSize(90, 0))
        self.lbl_cipher.setObjectName("lbl_cipher")

        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setMinimumHeight(110)
        self.txt_cipher_text.setObjectName("txt_cipher_text")

        self.hbox_cipher.addWidget(self.lbl_cipher, 0, QtCore.Qt.AlignTop)
        self.hbox_cipher.addWidget(self.txt_cipher_text, 1)

        # Buttons Encrypt / Decrypt
        self.hbox_left_btns = QtWidgets.QHBoxLayout()
        self.hbox_left_btns.setSpacing(14)
        self.hbox_left_btns.setObjectName("hbox_left_btns")

        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setMinimumSize(QtCore.QSize(140, 34))
        self.btn_encrypt.setObjectName("btn_encrypt")

        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setMinimumSize(QtCore.QSize(140, 34))
        self.btn_decrypt.setObjectName("btn_decrypt")

        self.hbox_left_btns.addStretch(1)
        self.hbox_left_btns.addWidget(self.btn_encrypt)
        self.hbox_left_btns.addSpacing(30)
        self.hbox_left_btns.addWidget(self.btn_decrypt)
        self.hbox_left_btns.addStretch(1)

        self.left_col.addLayout(self.hbox_plain)
        self.left_col.addLayout(self.hbox_cipher)
        self.left_col.addSpacing(6)
        self.left_col.addLayout(self.hbox_left_btns)

        # ---------- RIGHT COLUMN ----------
        self.right_col = QtWidgets.QVBoxLayout()
        self.right_col.setSpacing(10)
        self.right_col.setObjectName("right_col")

        # Information
        self.hbox_info = QtWidgets.QHBoxLayout()
        self.hbox_info.setSpacing(10)
        self.hbox_info.setObjectName("hbox_info")

        self.lbl_info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info.setMinimumSize(QtCore.QSize(90, 0))
        self.lbl_info.setObjectName("lbl_info")

        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setMinimumHeight(110)
        self.txt_info.setObjectName("txt_info")

        self.hbox_info.addWidget(self.lbl_info, 0, QtCore.Qt.AlignTop)
        self.hbox_info.addWidget(self.txt_info, 1)

        # Signature
        self.hbox_sign = QtWidgets.QHBoxLayout()
        self.hbox_sign.setSpacing(10)
        self.hbox_sign.setObjectName("hbox_sign")

        self.lbl_sign = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sign.setMinimumSize(QtCore.QSize(90, 0))
        self.lbl_sign.setObjectName("lbl_sign")

        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setMinimumHeight(110)
        self.txt_sign.setObjectName("txt_sign")

        self.hbox_sign.addWidget(self.lbl_sign, 0, QtCore.Qt.AlignTop)
        self.hbox_sign.addWidget(self.txt_sign, 1)

        # Buttons Sign / Verify
        self.hbox_right_btns = QtWidgets.QHBoxLayout()
        self.hbox_right_btns.setSpacing(14)
        self.hbox_right_btns.setObjectName("hbox_right_btns")

        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setMinimumSize(QtCore.QSize(140, 34))
        self.btn_sign.setObjectName("btn_sign")

        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setMinimumSize(QtCore.QSize(140, 34))
        self.btn_verify.setObjectName("btn_verify")

        self.hbox_right_btns.addStretch(1)
        self.hbox_right_btns.addWidget(self.btn_sign)
        self.hbox_right_btns.addSpacing(30)
        self.hbox_right_btns.addWidget(self.btn_verify)
        self.hbox_right_btns.addStretch(1)

        self.right_col.addLayout(self.hbox_info)
        self.right_col.addLayout(self.hbox_sign)
        self.right_col.addSpacing(6)
        self.right_col.addLayout(self.hbox_right_btns)

        # Add columns to content row
        self.hbox_content.addLayout(self.left_col, 1)
        self.hbox_content.addLayout(self.right_col, 1)

        self.vbox_main.addLayout(self.hbox_content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Cipher"))
        self.lbl_title.setText(_translate("MainWindow", "RSA CIPHER"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.lbl_plain.setText(_translate("MainWindow", "Plain Text:"))
        self.lbl_cipher.setText(_translate("MainWindow", "CipherText:"))
        self.lbl_info.setText(_translate("MainWindow", "Information:"))
        self.lbl_sign.setText(_translate("MainWindow", "Signature:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
