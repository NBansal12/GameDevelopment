# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hint1.ui'
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

class Ui_hint1(object):
    def setupUi(self, hint1):
        hint1.setObjectName(_fromUtf8("hint1"))
        hint1.resize(350, 250)
        hint1.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));"))
        self.textEdit = QtGui.QTextEdit(hint1)
        self.textEdit.setGeometry(QtCore.QRect(30, 70, 301, 91))
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(hint1)
        QtCore.QMetaObject.connectSlotsByName(hint1)

    def retranslateUi(self, hint1):
        hint1.setWindowTitle(_translate("hint1", "Form", None))
        self.textEdit.setHtml(_translate("hint1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"><br /></span><span style=\" font-family:\'arial,sans-serif\'; font-size:14pt; font-weight:600; color:#55ff7f; background-color:#ffffff;\">not even or regular in pattern or movement; unpredictable.</span></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    hint1 = QtGui.QWidget()
    ui = Ui_hint1()
    ui.setupUi(hint1)
    hint1.show()
    sys.exit(app.exec_())

