# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window9.ui'
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

class Ui_win9(object):
    def setupUi(self, win9):
        win9.setObjectName(_fromUtf8("win9"))
        win9.resize(600, 500)
        win9.setMinimumSize(QtCore.QSize(600, 500))
        win9.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtGui.QWidget(win9)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.win9name = QtGui.QLabel(self.centralwidget)
        self.win9name.setGeometry(QtCore.QRect(60, 90, 61, 21))
        self.win9name.setObjectName(_fromUtf8("win9name"))
        self.win9gender = QtGui.QLabel(self.centralwidget)
        self.win9gender.setGeometry(QtCore.QRect(296, 90, 71, 21))
        self.win9gender.setObjectName(_fromUtf8("win9gender"))
        self.win9heading = QtGui.QLabel(self.centralwidget)
        self.win9heading.setGeometry(QtCore.QRect(230, 30, 131, 31))
        self.win9heading.setObjectName(_fromUtf8("win9heading"))
        self.win9round1score = QtGui.QLabel(self.centralwidget)
        self.win9round1score.setGeometry(QtCore.QRect(120, 170, 101, 16))
        self.win9round1score.setObjectName(_fromUtf8("win9round1score"))
        self.win9round2score = QtGui.QLabel(self.centralwidget)
        self.win9round2score.setGeometry(QtCore.QRect(120, 220, 111, 16))
        self.win9round2score.setObjectName(_fromUtf8("win9round2score"))
        self.win9round3score = QtGui.QLabel(self.centralwidget)
        self.win9round3score.setGeometry(QtCore.QRect(120, 270, 101, 16))
        self.win9round3score.setObjectName(_fromUtf8("win9round3score"))
        self.win9nameinput = QtGui.QLineEdit(self.centralwidget)
        self.win9nameinput.setGeometry(QtCore.QRect(130, 90, 121, 21))
        self.win9nameinput.setObjectName(_fromUtf8("win9nameinput"))
        self.win9round1scoreinput = QtGui.QLineEdit(self.centralwidget)
        self.win9round1scoreinput.setGeometry(QtCore.QRect(310, 170, 113, 20))
        self.win9round1scoreinput.setObjectName(_fromUtf8("win9round1scoreinput"))
        self.win9round2scoreinput = QtGui.QLineEdit(self.centralwidget)
        self.win9round2scoreinput.setGeometry(QtCore.QRect(310, 220, 113, 20))
        self.win9round2scoreinput.setObjectName(_fromUtf8("win9round2scoreinput"))
        self.win9round3scoreinput = QtGui.QLineEdit(self.centralwidget)
        self.win9round3scoreinput.setGeometry(QtCore.QRect(310, 270, 113, 20))
        self.win9round3scoreinput.setObjectName(_fromUtf8("win9round3scoreinput"))
        self.win9totalscore = QtGui.QLabel(self.centralwidget)
        self.win9totalscore.setGeometry(QtCore.QRect(150, 360, 141, 31))
        self.win9totalscore.setObjectName(_fromUtf8("win9totalscore"))
        self.win9totalscoreinput = QtGui.QLineEdit(self.centralwidget)
        self.win9totalscoreinput.setGeometry(QtCore.QRect(310, 370, 113, 20))
        self.win9totalscoreinput.setObjectName(_fromUtf8("win9totalscoreinput"))
        self.win9imagelabel = QtGui.QLabel(self.centralwidget)
        self.win9imagelabel.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.win9imagelabel.setObjectName(_fromUtf8("win9imagelabel"))
        self.win9genderinput = QtGui.QLineEdit(self.centralwidget)
        self.win9genderinput.setGeometry(QtCore.QRect(390, 90, 121, 21))
        self.win9genderinput.setObjectName(_fromUtf8("win9genderinput"))
        self.win9imagelabel.raise_()
        self.win9name.raise_()
        self.win9gender.raise_()
        self.win9heading.raise_()
        self.win9round1score.raise_()
        self.win9round2score.raise_()
        self.win9round3score.raise_()
        self.win9nameinput.raise_()
        self.win9round1scoreinput.raise_()
        self.win9round2scoreinput.raise_()
        self.win9round3scoreinput.raise_()
        self.win9totalscore.raise_()
        self.win9totalscoreinput.raise_()
        self.win9genderinput.raise_()
        win9.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win9)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win9.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win9)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win9.setStatusBar(self.statusbar)

        self.retranslateUi(win9)
        QtCore.QMetaObject.connectSlotsByName(win9)

    def retranslateUi(self, win9):
        win9.setWindowTitle(_translate("win9", "MainWindow", None))
        self.win9name.setText(_translate("win9", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Name:</span></p></body></html>", None))
        self.win9gender.setText(_translate("win9", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Gender:</span></p></body></html>", None))
        self.win9heading.setText(_translate("win9", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">RESULT</span></p></body></html>", None))
        self.win9round1score.setText(_translate("win9", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">ROUND 1 SCORE</span></p></body></html>", None))
        self.win9round2score.setText(_translate("win9", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">ROUND 2 SCORE</span></p></body></html>", None))
        self.win9round3score.setText(_translate("win9", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">ROUND 3 SCORE</span></p></body></html>", None))
        self.win9totalscore.setText(_translate("win9", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">TOTAL SCORE:</span></p></body></html>", None))
        self.win9imagelabel.setText(_translate("win9", "<html><head/><body><p><img src=\":/IMAGES/back2.png\"/></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win9 = QtGui.QMainWindow()
    ui = Ui_win9()
    ui.setupUi(win9)
    win9.show()
    sys.exit(app.exec_())

