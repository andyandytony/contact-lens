# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_paw_lens.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1458, 801)
        self.label_2_title = QtWidgets.QLabel(Dialog)
        self.label_2_title.setGeometry(QtCore.QRect(490, 0, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2_title.setFont(font)
        self.label_2_title.setMouseTracking(False)
        self.label_2_title.setTabletTracking(False)
        self.label_2_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2_title.setAutoFillBackground(False)
        self.label_2_title.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_2_title.setObjectName("label_2_title")
        self.label_Burr = QtWidgets.QLabel(Dialog)
        self.label_Burr.setGeometry(QtCore.QRect(20, 50, 700, 600))
        self.label_Burr.setStyleSheet("background-color: rgb(240, 238, 255);")
        self.label_Burr.setObjectName("label_Burr")
        self.label_Yolo = QtWidgets.QLabel(Dialog)
        self.label_Yolo.setGeometry(QtCore.QRect(730, 50, 700, 600))
        self.label_Yolo.setStyleSheet("background-color: rgb(226, 245, 255);")
        self.label_Yolo.setObjectName("label_Yolo")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(810, 690, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 189, 236);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 690, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(179, 191, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 690, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(204, 255, 201);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2_title.setText(_translate("Dialog", "Contact lens defect detection"))
        self.label_Burr.setText(_translate("Dialog", "TextLabel"))
        self.label_Yolo.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "Run"))
        self.pushButton_2.setText(_translate("Dialog", "init"))
        self.pushButton_3.setText(_translate("Dialog", "setting"))

