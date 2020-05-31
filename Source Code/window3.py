# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_win3(object):
    def setupUi(self, win3):
        win3.setObjectName(_fromUtf8("win3"))
        win3.resize(600, 500)
        win3.setMinimumSize(QtCore.QSize(600, 500))
        win3.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtGui.QWidget(win3)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.win3chevrolet = QtGui.QRadioButton(self.centralwidget)
        self.win3chevrolet.setGeometry(QtCore.QRect(160, 340, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.win3chevrolet.setFont(font)
        self.win3chevrolet.setAutoFillBackground(False)
        self.win3chevrolet.setIconSize(QtCore.QSize(25, 25))
        self.win3chevrolet.setObjectName(_fromUtf8("win3chevrolet"))
        self.win3mitsubishi = QtGui.QRadioButton(self.centralwidget)
        self.win3mitsubishi.setGeometry(QtCore.QRect(330, 340, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.win3mitsubishi.setFont(font)
        self.win3mitsubishi.setObjectName(_fromUtf8("win3mitsubishi"))
        self.win3mercedes = QtGui.QRadioButton(self.centralwidget)
        self.win3mercedes.setGeometry(QtCore.QRect(160, 380, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.win3mercedes.setFont(font)
        self.win3mercedes.setObjectName(_fromUtf8("win3mercedes"))
        self.win3peugeot = QtGui.QRadioButton(self.centralwidget)
        self.win3peugeot.setGeometry(QtCore.QRect(330, 380, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.win3peugeot.setFont(font)
        self.win3peugeot.setObjectName(_fromUtf8("win3peugeot"))
        self.win3proceed = QtGui.QPushButton(self.centralwidget)
        self.win3proceed.setGeometry(QtCore.QRect(260, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win3proceed.setFont(font)
        self.win3proceed.setObjectName(_fromUtf8("win3proceed"))
        self.win3headinglabel = QtGui.QLabel(self.centralwidget)
        self.win3headinglabel.setGeometry(QtCore.QRect(170, 20, 251, 51))
        self.win3headinglabel.setObjectName(_fromUtf8("win3headinglabel"))
        self.win3imagelabel = QtGui.QLabel(self.centralwidget)
        self.win3imagelabel.setGeometry(QtCore.QRect(0, 0, 601, 471))
        self.win3imagelabel.setAutoFillBackground(False)
        self.win3imagelabel.setObjectName(_fromUtf8("win3imagelabel"))
        self.win3logolabel = QtGui.QLabel(self.centralwidget)
        self.win3logolabel.setGeometry(QtCore.QRect(160, 90, 261, 201))
        self.win3logolabel.setObjectName(_fromUtf8("win3logolabel"))
        self.win3queslabel = QtGui.QLabel(self.centralwidget)
        self.win3queslabel.setGeometry(QtCore.QRect(170, 300, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.win3queslabel.setFont(font)
        self.win3queslabel.setObjectName(_fromUtf8("win3queslabel"))
        self.win3imagelabel.raise_()
        self.win3chevrolet.raise_()
        self.win3mitsubishi.raise_()
        self.win3mercedes.raise_()
        self.win3peugeot.raise_()
        self.win3proceed.raise_()
        self.win3headinglabel.raise_()
        self.win3logolabel.raise_()
        self.win3queslabel.raise_()
        win3.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win3.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win3)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win3.setStatusBar(self.statusbar)

        self.retranslateUi(win3)
        QtCore.QMetaObject.connectSlotsByName(win3)

    def retranslateUi(self, win3):
        win3.setWindowTitle(_translate("win3", "MainWindow", None))
        self.win3chevrolet.setText(_translate("win3", "Chevrolet", None))
        self.win3mitsubishi.setText(_translate("win3", "Mitsubishi", None))
        self.win3mercedes.setText(_translate("win3", "Mercedes", None))
        self.win3peugeot.setText(_translate("win3", "Peugeot", None))
        self.win3proceed.setText(_translate("win3", "PROCEED", None))
        self.win3headinglabel.setText(_translate("win3", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#00007f;\">GUESS THE LOGO</span></p></body></html>", None))
        self.win3imagelabel.setText(_translate("win3", "<html><head/><body><p><img src=\":/IMAGES/back13.png\"/></p></body></html>", None))
        self.win3logolabel.setText(_translate("win3", "<html><head/><body><p><img src=\":/IMAGES/mitsubishi.png\"/></p></body></html>", None))
        self.win3queslabel.setText(_translate("win3", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Choose any one of the following options</span></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win3 = QtGui.QMainWindow()
    ui = Ui_win3()
    ui.setupUi(win3)
    win3.show()
    sys.exit(app.exec_())

