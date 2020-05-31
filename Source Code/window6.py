# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window6.ui'
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

class Ui_win6(object):
    def setupUi(self, win6):
        win6.setObjectName(_fromUtf8("win6"))
        win6.resize(600, 500)
        win6.setMinimumSize(QtCore.QSize(600, 500))
        win6.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtGui.QWidget(win6)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.win6proceed = QtGui.QPushButton(self.centralwidget)
        self.win6proceed.setGeometry(QtCore.QRect(230, 400, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win6proceed.setFont(font)
        self.win6proceed.setObjectName(_fromUtf8("win6proceed"))
        self.win6hint = QtGui.QPushButton(self.centralwidget)
        self.win6hint.setGeometry(QtCore.QRect(460, 260, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win6hint.setFont(font)
        self.win6hint.setObjectName(_fromUtf8("win6hint"))
        self.win6mainqueslabel = QtGui.QLabel(self.centralwidget)
        self.win6mainqueslabel.setGeometry(QtCore.QRect(70, 130, 401, 51))
        self.win6mainqueslabel.setObjectName(_fromUtf8("win6mainqueslabel"))
        self.win6fast = QtGui.QRadioButton(self.centralwidget)
        self.win6fast.setGeometry(QtCore.QRect(90, 246, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win6fast.setFont(font)
        self.win6fast.setObjectName(_fromUtf8("win6fast"))
        self.win6irregular = QtGui.QRadioButton(self.centralwidget)
        self.win6irregular.setGeometry(QtCore.QRect(230, 240, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win6irregular.setFont(font)
        self.win6irregular.setObjectName(_fromUtf8("win6irregular"))
        self.win6valuable = QtGui.QRadioButton(self.centralwidget)
        self.win6valuable.setGeometry(QtCore.QRect(90, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win6valuable.setFont(font)
        self.win6valuable.setObjectName(_fromUtf8("win6valuable"))
        self.win6contradictory = QtGui.QRadioButton(self.centralwidget)
        self.win6contradictory.setGeometry(QtCore.QRect(230, 290, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win6contradictory.setFont(font)
        self.win6contradictory.setObjectName(_fromUtf8("win6contradictory"))
        self.win6headinglabel = QtGui.QLabel(self.centralwidget)
        self.win6headinglabel.setGeometry(QtCore.QRect(130, 20, 391, 71))
        self.win6headinglabel.setObjectName(_fromUtf8("win6headinglabel"))
        self.win6imagelabel = QtGui.QLabel(self.centralwidget)
        self.win6imagelabel.setGeometry(QtCore.QRect(0, 0, 611, 491))
        self.win6imagelabel.setObjectName(_fromUtf8("win6imagelabel"))
        self.win6optionques = QtGui.QLabel(self.centralwidget)
        self.win6optionques.setGeometry(QtCore.QRect(100, 200, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.win6optionques.setFont(font)
        self.win6optionques.setObjectName(_fromUtf8("win6optionques"))
        self.win6headingimage = QtGui.QLabel(self.centralwidget)
        self.win6headingimage.setGeometry(QtCore.QRect(90, 30, 481, 51))
        self.win6headingimage.setObjectName(_fromUtf8("win6headingimage"))
        self.win6imagelabel.raise_()
        self.win6proceed.raise_()
        self.win6mainqueslabel.raise_()
        self.win6fast.raise_()
        self.win6irregular.raise_()
        self.win6valuable.raise_()
        self.win6contradictory.raise_()
        self.win6hint.raise_()
        self.win6optionques.raise_()
        self.win6headingimage.raise_()
        self.win6headinglabel.raise_()
        win6.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win6)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win6.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win6)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win6.setStatusBar(self.statusbar)

        self.retranslateUi(win6)
        QtCore.QMetaObject.connectSlotsByName(win6)

    def retranslateUi(self, win6):
        win6.setWindowTitle(_translate("win6", "MainWindow", None))
        self.win6proceed.setText(_translate("win6", "PROCEED", None))
        self.win6hint.setText(_translate("win6", "HINT", None))
        self.win6mainqueslabel.setText(_translate("win6", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; font-style:italic; color:#ff00ff;\">Synonym of erractic?</span></p></body></html>", None))
        self.win6fast.setText(_translate("win6", "fast", None))
        self.win6irregular.setText(_translate("win6", "irregular", None))
        self.win6valuable.setText(_translate("win6", "valuable", None))
        self.win6contradictory.setText(_translate("win6", "contradictory", None))
        self.win6headinglabel.setText(_translate("win6", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#ffffff;\">VOCABULARY TEST</span></p></body></html>", None))
        self.win6imagelabel.setText(_translate("win6", "<html><head/><body><p><img src=\":/IMAGES/back8.png\"/></p></body></html>", None))
        self.win6optionques.setText(_translate("win6", "<html><head/><body><p><span style=\" font-size:11pt;\">Choose any one of the following</span></p></body></html>", None))
        self.win6headingimage.setText(_translate("win6", "<html><head/><body><p><img src=\":/IMAGES/back5.png\"/></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win6 = QtGui.QMainWindow()
    ui = Ui_win6()
    ui.setupUi(win6)
    win6.show()
    sys.exit(app.exec_())

