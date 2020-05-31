# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window4.ui'
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

class Ui_win4(object):
    def setupUi(self, win4):
        win4.setObjectName(_fromUtf8("win4"))
        win4.resize(600, 500)
        win4.setMinimumSize(QtCore.QSize(600, 500))
        win4.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtGui.QWidget(win4)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.win4Claiborne = QtGui.QRadioButton(self.centralwidget)
        self.win4Claiborne.setGeometry(QtCore.QRect(160, 340, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win4Claiborne.setFont(font)
        self.win4Claiborne.setObjectName(_fromUtf8("win4Claiborne"))
        self.win4Converse = QtGui.QRadioButton(self.centralwidget)
        self.win4Converse.setGeometry(QtCore.QRect(310, 340, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win4Converse.setFont(font)
        self.win4Converse.setObjectName(_fromUtf8("win4Converse"))
        self.win4Columbia = QtGui.QRadioButton(self.centralwidget)
        self.win4Columbia.setGeometry(QtCore.QRect(160, 370, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win4Columbia.setFont(font)
        self.win4Columbia.setObjectName(_fromUtf8("win4Columbia"))
        self.win4proceed = QtGui.QPushButton(self.centralwidget)
        self.win4proceed.setGeometry(QtCore.QRect(250, 410, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win4proceed.setFont(font)
        self.win4proceed.setObjectName(_fromUtf8("win4proceed"))
        self.win4Chanel = QtGui.QRadioButton(self.centralwidget)
        self.win4Chanel.setGeometry(QtCore.QRect(310, 370, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win4Chanel.setFont(font)
        self.win4Chanel.setObjectName(_fromUtf8("win4Chanel"))
        self.win4imagelabel = QtGui.QLabel(self.centralwidget)
        self.win4imagelabel.setGeometry(QtCore.QRect(0, -10, 621, 481))
        self.win4imagelabel.setObjectName(_fromUtf8("win4imagelabel"))
        self.win4headinglabel = QtGui.QLabel(self.centralwidget)
        self.win4headinglabel.setGeometry(QtCore.QRect(160, 40, 251, 51))
        self.win4headinglabel.setObjectName(_fromUtf8("win4headinglabel"))
        self.win4queslabel = QtGui.QLabel(self.centralwidget)
        self.win4queslabel.setGeometry(QtCore.QRect(160, 300, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.win4queslabel.setFont(font)
        self.win4queslabel.setObjectName(_fromUtf8("win4queslabel"))
        self.win4logolabel = QtGui.QLabel(self.centralwidget)
        self.win4logolabel.setGeometry(QtCore.QRect(140, 90, 311, 201))
        self.win4logolabel.setObjectName(_fromUtf8("win4logolabel"))
        self.win4imagelabel.raise_()
        self.win4Claiborne.raise_()
        self.win4Converse.raise_()
        self.win4Columbia.raise_()
        self.win4proceed.raise_()
        self.win4Chanel.raise_()
        self.win4headinglabel.raise_()
        self.win4queslabel.raise_()
        self.win4logolabel.raise_()
        win4.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win4.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win4)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win4.setStatusBar(self.statusbar)

        self.retranslateUi(win4)
        QtCore.QMetaObject.connectSlotsByName(win4)

    def retranslateUi(self, win4):
        win4.setWindowTitle(_translate("win4", "MainWindow", None))
        self.win4Claiborne.setText(_translate("win4", "Claiborne", None))
        self.win4Converse.setText(_translate("win4", "Converse", None))
        self.win4Columbia.setText(_translate("win4", "Columbia", None))
        self.win4proceed.setText(_translate("win4", "PROCEED", None))
        self.win4Chanel.setText(_translate("win4", "Chanel", None))
        self.win4imagelabel.setText(_translate("win4", "<html><head/><body><p><img src=\":/IMAGES/back6.png\"/></p></body></html>", None))
        self.win4headinglabel.setText(_translate("win4", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#00aa00;\">GUESS THE LOGO</span></p></body></html>", None))
        self.win4queslabel.setText(_translate("win4", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Choose any one of the following options</span></p></body></html>", None))
        self.win4logolabel.setText(_translate("win4", "<html><head/><body><p><img src=\":/IMAGES/chanel.png\"/></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win4 = QtGui.QMainWindow()
    ui = Ui_win4()
    ui.setupUi(win4)
    win4.show()
    sys.exit(app.exec_())

