# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hint2.ui'
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

class Ui_hint2(object):
    def setupUi(self, hint2):
        hint2.setObjectName(_fromUtf8("hint2"))
        hint2.resize(350, 250)
        hint2.setStyleSheet(_fromUtf8("background-image: url(:/IMAGES/back9.png);"))
        self.label = QtGui.QLabel(hint2)
        self.label.setGeometry(QtCore.QRect(60, 20, 221, 201))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(hint2)
        QtCore.QMetaObject.connectSlotsByName(hint2)

    def retranslateUi(self, hint2):
        hint2.setWindowTitle(_translate("hint2", "Form", None))
        self.label.setText(_translate("hint2", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55ff7f;\">a group of binary </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55ff7f;\">digits or bits</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55ff7f;\">(usually eight) </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55ff7f;\">operated on as a</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55ff7f;\">unit.</span></p></body></html>", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    hint2 = QtGui.QWidget()
    ui = Ui_hint2()
    ui.setupUi(hint2)
    hint2.show()
    sys.exit(app.exec_())

