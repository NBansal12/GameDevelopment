from PyQt4 import QtCore, QtGui

from RULES import Ui_win2rules

from import_rc import back13
           

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

class Ui_gamerdetails(object):
    
    def openwin2rules(self):
        self.window=QtGui.QWidget()
        self.ui =Ui_win2rules()
        self.ui.setupUi(self.window)
        gamerdetails.hide()
        self.window.show()
    
    def setupUi(self, gamerdetails):
        gamerdetails.setObjectName(_fromUtf8("gamerdetails"))
        gamerdetails.resize(364, 216)
        self.male = QtGui.QRadioButton(gamerdetails)
        self.male.setGeometry(QtCore.QRect(80, 130, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.male.setFont(font)
        self.male.setObjectName(_fromUtf8("male"))
        self.female = QtGui.QRadioButton(gamerdetails)
        self.female.setGeometry(QtCore.QRect(210, 130, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.female.setFont(font)
        self.female.setObjectName(_fromUtf8("female"))
        self.savedetails = QtGui.QPushButton(gamerdetails)
        self.savedetails.setGeometry(QtCore.QRect(140, 160, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.savedetails.setFont(font)
        self.savedetails.setObjectName(_fromUtf8("savedetails"))
        
        self.savedetails.clicked.connect(self.openwin2rules)
        
        self.graphicsView = QtGui.QGraphicsView(gamerdetails)
        self.graphicsView.setGeometry(QtCore.QRect(-35, -19, 521, 371))
        self.graphicsView.setMinimumSize(QtCore.QSize(521, 371))
        self.graphicsView.setStyleSheet(_fromUtf8("background-image: url(:/IMAGES/back13.png);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.lineEdit = QtGui.QLineEdit(gamerdetails)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 111, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        
        self.lineEdit.clicked.input()
        
        self.name = QtGui.QLabel(gamerdetails)
        self.name.setGeometry(QtCore.QRect(70, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName(_fromUtf8("name"))
        self.details = QtGui.QLabel(gamerdetails)
        self.details.setGeometry(QtCore.QRect(50, 40, 241, 31))
        self.details.setObjectName(_fromUtf8("details"))
        self.img = QtGui.QLabel(gamerdetails)
        self.img.setGeometry(QtCore.QRect(0, 0, 361, 211))
        self.img.setObjectName(_fromUtf8("img"))
        self.img.raise_()
        self.graphicsView.raise_()
        self.male.raise_()
        self.female.raise_()
        self.savedetails.raise_()
        self.lineEdit.raise_()
        self.name.raise_()
        self.details.raise_()

        self.retranslateUi(gamerdetails)
        QtCore.QMetaObject.connectSlotsByName(gamerdetails)

    def retranslateUi(self, gamerdetails):
        gamerdetails.setWindowTitle(_translate("gamerdetails", "Form", None))
        self.male.setText(_translate("gamerdetails", "Male", None))
        self.female.setText(_translate("gamerdetails", "Female", None))
        self.savedetails.setText(_translate("gamerdetails", "Save", None))
        self.name.setText(_translate("gamerdetails", "<html><head/><body><p><span style=\" font-size:10pt;\">Name:</span></p></body></html>", None))
        self.details.setText(_translate("gamerdetails", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">ENTER YOUR DETAILS</span></p></body></html>", None))
        self.img.setText(_translate("gamerdetails", "<html><head/><body><p><img src=\":/IMAGES/back5.png\"/></p></body></html>", None))
       
  
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    gamerdetails = QtGui.QWidget()
    ui = Ui_gamerdetails()
    ui.setupUi(gamerdetails)
    gamerdetails.show()
    sys.exit(app.exec_())

