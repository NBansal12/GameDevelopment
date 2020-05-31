# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'round2welcome.ui'
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

class Ui_welcomeround2(object):
    def setupUi(self, welcomeround2):
        welcomeround2.setObjectName(_fromUtf8("welcomeround2"))
        welcomeround2.resize(350, 250)
        welcomeround2.setStyleSheet(_fromUtf8("background-image: url(:/IMAGES/back3.png);"))
        self.textEdit = QtGui.QTextEdit(welcomeround2)
        self.textEdit.setGeometry(QtCore.QRect(80, 50, 201, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(welcomeround2)
        QtCore.QMetaObject.connectSlotsByName(welcomeround2)

    def retranslateUi(self, welcomeround2):
        welcomeround2.setWindowTitle(_translate("welcomeround2", "Form", None))
        self.textEdit.setHtml(_translate("welcomeround2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ffffff;\">WELCOME </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ffffff;\">TO </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ffffff;\">ROUND 2</span></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    welcomeround2 = QtGui.QWidget()
    ui = Ui_welcomeround2()
    ui.setupUi(welcomeround2)
    welcomeround2.show()
    sys.exit(app.exec_())

