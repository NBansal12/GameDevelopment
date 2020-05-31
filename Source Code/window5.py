# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window5.ui'
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

class Ui_win5(object):
    def setupUi(self, win5):
        win5.setObjectName(_fromUtf8("win5"))
        win5.resize(600, 500)
        win5.setMinimumSize(QtCore.QSize(600, 500))
        win5.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtGui.QWidget(win5)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.win5alligator = QtGui.QRadioButton(self.centralwidget)
        self.win5alligator.setGeometry(QtCore.QRect(140, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win5alligator.setFont(font)
        self.win5alligator.setObjectName(_fromUtf8("win5alligator"))
        self.win5adacore = QtGui.QRadioButton(self.centralwidget)
        self.win5adacore.setGeometry(QtCore.QRect(330, 320, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win5adacore.setFont(font)
        self.win5adacore.setObjectName(_fromUtf8("win5adacore"))
        self.win5amaxinfotech = QtGui.QRadioButton(self.centralwidget)
        self.win5amaxinfotech.setGeometry(QtCore.QRect(140, 360, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win5amaxinfotech.setFont(font)
        self.win5amaxinfotech.setObjectName(_fromUtf8("win5amaxinfotech"))
        self.win5adobe = QtGui.QRadioButton(self.centralwidget)
        self.win5adobe.setGeometry(QtCore.QRect(330, 350, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win5adobe.setFont(font)
        self.win5adobe.setObjectName(_fromUtf8("win5adobe"))
        self.win5proceed = QtGui.QPushButton(self.centralwidget)
        self.win5proceed.setGeometry(QtCore.QRect(260, 410, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win5proceed.setFont(font)
        self.win5proceed.setObjectName(_fromUtf8("win5proceed"))
        self.win5headinglable = QtGui.QLabel(self.centralwidget)
        self.win5headinglable.setGeometry(QtCore.QRect(170, 40, 251, 51))
        self.win5headinglable.setObjectName(_fromUtf8("win5headinglable"))
        self.win5queslabel = QtGui.QLabel(self.centralwidget)
        self.win5queslabel.setGeometry(QtCore.QRect(170, 280, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.win5queslabel.setFont(font)
        self.win5queslabel.setObjectName(_fromUtf8("win5queslabel"))
        self.win5imagelabel = QtGui.QLabel(self.centralwidget)
        self.win5imagelabel.setGeometry(QtCore.QRect(0, -10, 631, 491))
        self.win5imagelabel.setObjectName(_fromUtf8("win5imagelabel"))
        self.win5logolabel = QtGui.QLabel(self.centralwidget)
        self.win5logolabel.setGeometry(QtCore.QRect(210, 110, 181, 151))
        self.win5logolabel.setObjectName(_fromUtf8("win5logolabel"))
        self.win5imagelabel.raise_()
        self.win5alligator.raise_()
        self.win5adacore.raise_()
        self.win5amaxinfotech.raise_()
        self.win5adobe.raise_()
        self.win5proceed.raise_()
        self.win5headinglable.raise_()
        self.win5queslabel.raise_()
        self.win5logolabel.raise_()
        win5.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win5.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win5)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win5.setStatusBar(self.statusbar)

        self.retranslateUi(win5)
        QtCore.QMetaObject.connectSlotsByName(win5)

    def retranslateUi(self, win5):
        win5.setWindowTitle(_translate("win5", "MainWindow", None))
        self.win5alligator.setText(_translate("win5", "Alligator", None))
        self.win5adacore.setText(_translate("win5", "Adacore", None))
        self.win5amaxinfotech.setText(_translate("win5", "Amax Infotech", None))
        self.win5adobe.setText(_translate("win5", "Adobe Systems", None))
        self.win5proceed.setText(_translate("win5", "PROCEED", None))
        self.win5headinglable.setText(_translate("win5", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#ffffff;\">GUESS THE LOGO</span></p></body></html>", None))
        self.win5queslabel.setText(_translate("win5", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Choose any one of the following options</span></p></body></html>", None))
        self.win5imagelabel.setText(_translate("win5", "<html><head/><body><p><img src=\":/IMAGES/back7.png\"/></p></body></html>", None))
        self.win5logolabel.setText(_translate("win5", "<html><head/><body><p><img src=\":/IMAGES/adobe system.png\"/></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win5 = QtGui.QMainWindow()
    ui = Ui_win5()
    ui.setupUi(win5)
    win5.show()
    sys.exit(app.exec_())

