# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window8.ui'
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

class Ui_win8(object):
    def setupUi(self, win8):
        win8.setObjectName(_fromUtf8("win8"))
        win8.resize(600, 500)
        win8.setMinimumSize(QtCore.QSize(600, 500))
        win8.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtGui.QWidget(win8)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.win8headinglabel = QtGui.QLabel(self.centralwidget)
        self.win8headinglabel.setGeometry(QtCore.QRect(180, 40, 261, 51))
        self.win8headinglabel.setObjectName(_fromUtf8("win8headinglabel"))
        self.win8writeques = QtGui.QLabel(self.centralwidget)
        self.win8writeques.setGeometry(QtCore.QRect(210, 340, 171, 21))
        self.win8writeques.setObjectName(_fromUtf8("win8writeques"))
        self.win8endgame = QtGui.QPushButton(self.centralwidget)
        self.win8endgame.setGeometry(QtCore.QRect(260, 400, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win8endgame.setFont(font)
        self.win8endgame.setObjectName(_fromUtf8("win8endgame"))
        self.win8logolabel = QtGui.QLabel(self.centralwidget)
        self.win8logolabel.setGeometry(QtCore.QRect(110, 80, 401, 251))
        self.win8logolabel.setObjectName(_fromUtf8("win8logolabel"))
        self.win8imagelabel = QtGui.QLabel(self.centralwidget)
        self.win8imagelabel.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.win8imagelabel.setObjectName(_fromUtf8("win8imagelabel"))
        self.win8writeinput = QtGui.QLineEdit(self.centralwidget)
        self.win8writeinput.setGeometry(QtCore.QRect(200, 360, 191, 31))
        self.win8writeinput.setObjectName(_fromUtf8("win8writeinput"))
        self.win8imagelabel.raise_()
        self.win8headinglabel.raise_()
        self.win8writeques.raise_()
        self.win8endgame.raise_()
        self.win8logolabel.raise_()
        self.win8writeinput.raise_()
        win8.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win8)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win8.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win8)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win8.setStatusBar(self.statusbar)

        self.retranslateUi(win8)
        QtCore.QMetaObject.connectSlotsByName(win8)

    def retranslateUi(self, win8):
        win8.setWindowTitle(_translate("win8", "MainWindow", None))
        self.win8headinglabel.setText(_translate("win8", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#ffffff;\">GUESS THE WORD</span></p></body></html>", None))
        self.win8writeques.setText(_translate("win8", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Write your answer below</span></p></body></html>", None))
        self.win8endgame.setText(_translate("win8", "END GAME", None))
        self.win8logolabel.setText(_translate("win8", "<html><head/><body><p><img src=\":/IMAGES/last round.png\"/></p></body></html>", None))
        self.win8imagelabel.setText(_translate("win8", "<html><head/><body><p><img src=\":/IMAGES/back12.png\"/></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win8 = QtGui.QMainWindow()
    ui = Ui_win8()
    ui.setupUi(win8)
    win8.show()
    sys.exit(app.exec_())

