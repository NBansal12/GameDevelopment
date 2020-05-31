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
    
    def __init__(self):
       super(Ui_win1,self).__init__()
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
    gamerdetails = QtGui.QWidget()
    ui = Ui_gamerdetails()
    ui.setupUi(gamerdetails)
    gamerdetails.show()
    win2rules = QtGui.QWidget()
    ui = Ui_win2rules()
    ui.setupUi(win2rules)
    win2rules.show()
    sys.exit(app.exec_())
    
    
###########################wiget1######################################
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
           

###################################################rules
class Ui_win2rules(object):
    def setupUi(self, win2rules):
        win2rules.setObjectName(_fromUtf8("win2rules"))
        win2rules.resize(600, 500)
        win2rules.setMinimumSize(QtCore.QSize(600, 500))
        win2rules.setMaximumSize(QtCore.QSize(600, 500))
        win2rules.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));"))
        self.win2instruction = QtGui.QTextBrowser(win2rules)
        self.win2instruction.setGeometry(QtCore.QRect(70, 110, 471, 271))
        self.win2instruction.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.win2instruction.setObjectName(_fromUtf8("win2instruction"))
        self.win2label = QtGui.QLabel(win2rules)
        self.win2label.setGeometry(QtCore.QRect(170, 50, 251, 31))
        self.win2label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.win2label.setObjectName(_fromUtf8("win2label"))
        self.win2skipbutton = QtGui.QPushButton(win2rules)
        self.win2skipbutton.setGeometry(QtCore.QRect(260, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.win2skipbutton.setFont(font)
        self.win2skipbutton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.win2skipbutton.setObjectName(_fromUtf8("win2skipbutton"))

        self.retranslateUi(win2rules)
        QtCore.QMetaObject.connectSlotsByName(win2rules)

    def retranslateUi(self, win2rules):
        win2rules.setWindowTitle(_translate("win2rules", "Form", None))
        self.win2instruction.setHtml(_translate("win2rules", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">WELCOME TO THE 3GAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">THIS GAME HAS THREE ROUNDS.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">ROUND 1 (BEGINNERS ROUND)</span><span style=\" font-size:8pt;\">: IN THIS ROUND, YOU NEED TO GUESS THE NAME OF THE LOGOS. LOGOS PICTURE AND 4 OPTIONS WILL BE PROVIDED. THERE WILL BE 3 QUESTIONS IN THIS ROUND. IF YOU GIVE AT LEAST TWO ANSWER CORRECTLY, YOU WILL BE PROMOTED TO THE NEXT ROUND. THERE WILL NOT BE ANY OPTION  IN THIS ROUND.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">ROUND 2 (INTERMEDIATE ROUND):</span><span style=\" font-size:8pt;\"> IN THIS ROUND, YOUR VOCABULARY WILL BE TESTED. THERE WILL BE 2 QUESTIONS WITH THE HINT. BUT IF YOU USE HINT, YOU WILL NOT BE AWARDED WITH MARKS THOUGH YOU CAN PROCEED TO THE NEXT QUESTION. IF YOU GIVE AT LEAST 1 ANSWER CORRECTLY, YOU WILL BE PROMOTED TO THE NEXT ROUND.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">ROUND 3 (EXPERT ROUND):</span><span style=\" font-size:8pt;\"> IN THIS ROUND, YOU LOGICAL SKILL WILL BE TESTED. THERE IS ONLY ONE QUESTION AND NO OPTION AND HINT WILL BE PROVIDED. TO WIN THE GAME, YOU NEED TO PASS THIS ROUND.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">AFTER COMPLETING THIS GAME, A RESULT OF YOUR WILL BE GENERATED.</span></p></body></html>", None))
        self.win2label.setText(_translate("win2rules", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">RULES OF THE 3GAME</span></p></body></html>", None))
        self.win2skipbutton.setText(_translate("win2rules", "SKIP", None))