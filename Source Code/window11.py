from PyQt4 import QtCore, QtGui
#################################
from widget1 import Ui_gamerdetails
################################


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

class Ui_win1(object):
    #####################################
    def opengamerdetails(self):
        self.window=QtGui.QWidget()
        self.ui =Ui_gamerdetails()
        self.ui.setupUi(self.window)
        win1.hide()
        self.window.show()
    ####################################
    def setupUi(self, win1):
        win1.setObjectName(_fromUtf8("win1"))
        win1.resize(600, 500)
        win1.setMinimumSize(QtCore.QSize(600, 500))
        win1.setMaximumSize(QtCore.QSize(600, 500))
        font = QtGui.QFont()
        font.setPointSize(12)
        win1.setFont(font)
        self.centralwidget = QtGui.QWidget(win1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gamelabel = QtGui.QLabel(self.centralwidget)
        self.gamelabel.setGeometry(QtCore.QRect(80, 80, 421, 181))
        self.gamelabel.setObjectName(_fromUtf8("gamelabel"))
        self.win1imagelabel = QtGui.QLabel(self.centralwidget)
        self.win1imagelabel.setGeometry(QtCore.QRect(-30, -20, 691, 531))
        self.win1imagelabel.setObjectName(_fromUtf8("win1imagelabel"))
        self.win1playlabel = QtGui.QPushButton(self.centralwidget)
        self.win1playlabel.setGeometry(QtCore.QRect(260, 330, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.win1playlabel.setFont(font)
        self.win1playlabel.setObjectName(_fromUtf8("win1playlabel"))
        #################################################
        self.win1playlabel.clicked.connect(self.opengamerdetails)
        ###################################################
        self.win1imagelabel.raise_()
        self.gamelabel.raise_()
        self.win1playlabel.raise_()
        win1.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(win1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        win1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(win1)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        win1.setStatusBar(self.statusbar)

        self.retranslateUi(win1)
        QtCore.QMetaObject.connectSlotsByName(win1)

    def retranslateUi(self, win1):
        win1.setWindowTitle(_translate("win1", "MainWindow", None))
        self.gamelabel.setText(_translate("win1", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">3</span><span style=\" font-size:72pt; font-weight:600; color:#00007f;\">GA</span><span style=\" font-size:72pt; font-weight:600; color:#55aa00;\">M</span><span style=\" font-size:72pt; font-weight:600; color:#00007f;\">E</span></p></body></html>", None))
        self.win1imagelabel.setText(_translate("win1", "<html><head/><body><p><img src=\":/IMAGES/back15.png\"/></p></body></html>", None))
        self.win1playlabel.setText(_translate("win1", "PLAY!", None))

#import images_rc as img
       
 


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win1 = QtGui.QMainWindow()
    ui = Ui_win1()
    ui.setupUi(win1)
    win1.show()
    sys.exit(app.exec_())

