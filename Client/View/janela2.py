# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from  Client.Model import  Client
from  Client.Controller import ClientThread
from  Client.View import  janela3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(262, 180)
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 131, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 51, 41))
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"    background-color : rgb(0, 170, 0);\n"
"    border-radius : 10px;\n"
"}"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "File UpLoad", None))
        self.pushButton.setText(_translate("MainWindow", "Selecionar Arquivo", None))
        self.label.setToolTip(_translate("MainWindow", "Servidor Online", None))
        self.label.setWhatsThis(_translate("MainWindow", "Status Servidor", None))

class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,parentApp,ip,port, parent=None,):
        super(MainWindow, self).__init__(parent)
        self.parentApp = parentApp
        self.windows = list()
        self.setupUi(self)
        self.conn = 0
        self.get_thread = ClientThread.SocketHandle(Client.Client(),(ip,port))
        self.choseFile = janela3.Dialog(self)
        self.get_thread.start()

        self.popup = None


    def progressBar(self,value,id,lenfile):

        progressbar = self.findChild(QtGui.QProgressBar, id)

        if progressbar.value() < 100:
            a = int(lenfile)//512
            if int(value)> 0:
                b = (int(value)//512)
                c = int((b/a)*100)
                progressbar.setValue(c)
                if progressbar.value() == 100:
                    self.findChild(QtGui.QPushButton, id).setEnabled(True)




