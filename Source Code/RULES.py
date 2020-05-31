
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win2rules = QtGui.QWidget()
    ui = Ui_win2rules()
    ui.setupUi(win2rules)
    win2rules.show()
    sys.exit(app.exec_())

