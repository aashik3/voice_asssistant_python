# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(929, 599)
        Dialog.setStyleSheet("background-color:black;")
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(0, -10, 931, 601))
        self.background.setStyleSheet("background-color:black;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.jarvisGIF = QtWidgets.QLabel(Dialog)
        self.jarvisGIF.setGeometry(QtCore.QRect(270, 110, 371, 311))
        self.jarvisGIF.setText("")
        self.jarvisGIF.setPixmap(QtGui.QPixmap("C:\\Users\\aaa\\Downloads\\heart.gif"))
        self.jarvisGIF.setScaledContents(True)
        self.jarvisGIF.setObjectName("jarvisGIF")
        self.ironmanGIF = QtWidgets.QLabel(Dialog)
        self.ironmanGIF.setGeometry(QtCore.QRect(610, 0, 321, 311))
        self.ironmanGIF.setText("")
        self.ironmanGIF.setPixmap(QtGui.QPixmap("C:\\Users\\aaa\\Downloads\\irontemplate.webp"))
        self.ironmanGIF.setScaledContents(True)
        self.ironmanGIF.setObjectName("ironmanGIF")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(600, 310, 241, 121))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\aaa\\Downloads\\start.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.facegui = QtWidgets.QLabel(Dialog)
        self.facegui.setGeometry(QtCore.QRect(0, -10, 301, 341))
        self.facegui.setStyleSheet("border:none;\n"
                                   "border-radius:none;")
        self.facegui.setText("")
        self.facegui.setPixmap(QtGui.QPixmap("C:\\Users\\aaa\\Downloads\\1_fhZsggnseKdBmY3_JonRkA.gif"))
        self.facegui.setScaledContents(True)
        self.facegui.setObjectName("facegui")
        self.startlabelnotbutton = QtWidgets.QTextBrowser(Dialog)
        self.startlabelnotbutton.setGeometry(QtCore.QRect(600, 310, 221, 121))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        self.startlabelnotbutton.setFont(font)
        self.startlabelnotbutton.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-radius:none;\n"
"")
        self.startlabelnotbutton.setObjectName("startlabelnotbutton")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(610, 450, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-radius:none;\n"
"")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(600, 440, 231, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\aaa\\Downloads\\exit.png"))
        self.label_2.setObjectName("label_2")
        self.quitlabelnotbutton = QtWidgets.QTextBrowser(Dialog)
        self.quitlabelnotbutton.setGeometry(QtCore.QRect(610, 440, 201, 101))
        self.quitlabelnotbutton.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-radius:none;\n"
"")
        self.quitlabelnotbutton.setObjectName("quitlabelnotbutton")
        self.startpushButton = QtWidgets.QPushButton(Dialog)
        self.startpushButton.setGeometry(QtCore.QRect(600, 310, 221, 121))
        self.startpushButton.setStyleSheet("background-color:transparent;")
        self.startpushButton.setText("")
        self.startpushButton.setObjectName("startpushButton")
        self.quitpushButton_2 = QtWidgets.QPushButton(Dialog)
        self.quitpushButton_2.setGeometry(QtCore.QRect(600, 440, 221, 101))
        self.quitpushButton_2.setStyleSheet("background-color:transparent;")
        self.quitpushButton_2.setText("")
        self.quitpushButton_2.setObjectName("quitpushButton_2")
        self.globegif = QtWidgets.QLabel(Dialog)
        self.globegif.setGeometry(QtCore.QRect(-20, 330, 321, 261))
        self.globegif.setText("")
        self.globegif.setPixmap(QtGui.QPixmap("C:\\Users\\aaa\\Downloads\\fa5c23af3f4cda50a9b49c4071ee4b55.gif"))
        self.globegif.setScaledContents(True)
        self.globegif.setObjectName("globegif")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.quitlabelnotbutton.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
