# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window7.ui'
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

class Ui_win7(object):
    def setupUi(self, win7):
        win7.setObjectName(_fromUtf8("win7"))
        win7.resize(600, 500)
        win7.setMinimumSize(QtCore.QSize(600, 500))
        win7.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtGui.QWidget(win7)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.win7writeinput = QtGui.QLineEdit(self.centralwidget)
        self.win7writeinput.setGeometry(QtCore.QRect(200, 330, 201, 31))
        self.win7writeinput.setObjectName(_fromUtf8("win7writeinput"))
        self.win7write = QtGui.QLabel(self.centralwidget)
        self.win7write.setGeometry(QtCore.QRect(230, 360, 161, 21))
        self.win7write.setObjectName(_fromUtf8("win7write"))
        self.win7hint = QtGui.QPushButton(self.centralwidget)
        self.win7hint.setGeometry(QtCore.QRect(480, 260, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win7hint.setFont(font)
        self.win7hint.setObjectName(_fromUtf8("win7hint"))
        self.win7proceed = QtGui.QPushButton(self.centralwidget)
        self.win7proceed.setGeometry(QtCore.QRect(260, 410, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win7proceed.setFont(font)
        self.win7proceed.setObjectName(_fromUtf8("win7proceed"))
        self.win7headinglabel = QtGui.QLabel(self.centralwidget)
        self.win7headinglabel.setGeometry(QtCore.QRect(130, 10, 361, 51))
        self.win7headinglabel.setObjectName(_fromUtf8("win7headinglabel"))
        self.win7imagelabel = QtGui.QLabel(self.centralwidget)
        self.win7imagelabel.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.win7imagelabel.setObjectName(_fromUtf8("win7imagelabel"))
        self.win7theword = QtGui.QLabel(self.centralwidget)
        self.win7theword.setGeometry(QtCore.QRect(270, 130, 201, 51))
        self.win7theword.setObjectName(_fromUtf8("win7theword"))
        self.win7Rearrangeimage = QtGui.QLabel(self.centralwidget)
        self.win7Rearrangeimage.setGeometry(QtCore.QRect(150, 100, 121, 101))
        self.win7Rearrangeimage.setObjectName(_fromUtf8("win7Rearrangeimage"))
        self.win7ytesb = QtGui.QLabel(self.centralwidget)
        self.win7ytesb.setGeometry(QtCore.QRect(210, 200, 181, 111))
        self.win7ytesb.setObjectName(_fromUtf8("win7ytesb"))
        self.win7imagelabel.raise_()
        self.win7writeinput.raise_()
        self.win7write.raise_()
        self.win7hint.raise_()
        self.win7proceed.raise_()
        self.win7headinglabel.raise_()
        self.win7theword.raise_()
        self.win7Rearrangeimage.raise_()
        self.win7ytesb.raise_()
        win7.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win7)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win7.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win7)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win7.setStatusBar(self.statusbar)

        self.retranslateUi(win7)
        QtCore.QMetaObject.connectSlotsByName(win7)

    def retranslateUi(self, win7):
        win7.setWindowTitle(_translate("win7", "MainWindow", None))
        self.win7write.setText(_translate("win7", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Write the answer here</span></p></body></html>", None))
        self.win7hint.setText(_translate("win7", "HINT", None))
        self.win7proceed.setText(_translate("win7", "PROCEED", None))
        self.win7headinglabel.setText(_translate("win7", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#aa0000;\">VOCABULARY TEST</span></p></body></html>", None))
        self.win7imagelabel.setText(_translate("win7", "<html><head/><body><p><img src=\":/IMAGES/back10.png\"/></p></body></html>", None))
        self.win7theword.setText(_translate("win7", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffaa00;\">the word </span></p><p align=\"center\"><span style=\" font-size:28pt; color:#ffaa00;\"><br/></span></p><p align=\"center\"><span style=\" font-size:28pt; color:#ffaa00;\"><br/></span></p></body></html>", None))
        self.win7Rearrangeimage.setText(_translate("win7", "<html><head/><body><p><img src=\":/IMAGES/i2.png\"/></p></body></html>", None))
        self.win7ytesb.setText(_translate("win7", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#0000ff;\">ytesb</span></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win7 = QtGui.QMainWindow()
    ui = Ui_win7()
    ui.setupUi(win7)
    win7.show()
    sys.exit(app.exec_())

