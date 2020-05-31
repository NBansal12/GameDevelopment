# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'round3welcome.ui'
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

class Ui_round3welcome(object):
    def setupUi(self, round3welcome):
        round3welcome.setObjectName(_fromUtf8("round3welcome"))
        round3welcome.resize(350, 250)
        round3welcome.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));"))
        self.textEdit = QtGui.QTextEdit(round3welcome)
        self.textEdit.setGeometry(QtCore.QRect(80, 50, 201, 151))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(round3welcome)
        QtCore.QMetaObject.connectSlotsByName(round3welcome)

    def retranslateUi(self, round3welcome):
        round3welcome.setWindowTitle(_translate("round3welcome", "Form", None))
        self.textEdit.setHtml(_translate("round3welcome", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ff5500;\">WELCOME </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ff5500;\">TO </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ff5500;\">ROUND 3</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    round3welcome = QtGui.QWidget()
    ui = Ui_round3welcome()
    ui.setupUi(round3welcome)
    round3welcome.show()
    sys.exit(app.exec_())

