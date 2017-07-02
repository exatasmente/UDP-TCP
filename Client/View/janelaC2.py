# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from  Client.Controller import ClientThread
from  Client.Model import  Client
from  Client.View import  Popup
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
        MainWindow.resize(333, 180)
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.filebutton = QtGui.QPushButton(self.centralwidget)
        self.filebutton.setGeometry(QtCore.QRect(90, 90, 131, 51))
        self.filebutton.setObjectName(_fromUtf8("filebutton"))
        self.arquivoProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.arquivoProgressBar.setGeometry(QtCore.QRect(10, 60, 322, 22))
        self.arquivoProgressBar.setProperty("value", 0)
        self.arquivoProgressBar.setEnabled(False)
        self.arquivoProgressBar.setObjectName(_fromUtf8("arquivoProgressBar"))
        self.filelabel = QtGui.QLabel(self.centralwidget)
        self.filelabel.setGeometry(QtCore.QRect(10, 19, 281, 31))
        self.filelabel.setText(_fromUtf8(""))
        self.filelabel.setObjectName(_fromUtf8("filelabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "File UpLoad", None))
        self.filebutton.setText(_translate("MainWindow", "Selecionar Arquivo", None))



class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,parentApp,ip,port,parent=None):
        super(MainWindow, self).__init__(parent)
        self.parentApp = parentApp
        self.windows = list()
        self.setupUi(self)
        self.connect(self.filebutton,QtCore.SIGNAL("clicked()"),self.fileChoose)
        self.get_thread = None
        self.serverAddr = (ip,int(port))
        self.popup = None
        self.get_thread = None

    def fileChoose(self):
        if(self.arquivoProgressBar.value() == 100):
            self.arquivoProgressBar.setValue(0)
        self.filelabel.setText(QtGui.QFileDialog.getOpenFileName())

        self.filebutton.setText("Enviar Arquivo")
        self.disconnect(self.filebutton, QtCore.SIGNAL("clicked()"), self.fileChoose)
        self.connect(self.filebutton, QtCore.SIGNAL("clicked()"), self.sendFile)


    def sendFile(self):

        self.filebutton.setText("Selecionar Arquivo")
        self.disconnect(self.filebutton, QtCore.SIGNAL("clicked()"), self.sendFile)
        self.connect(self.filebutton, QtCore.SIGNAL("clicked()"), self.fileChoose)
        self.filebutton.setEnabled(False)
        self.get_thread = ClientThread.SocketHandle(Client.Client(), self.serverAddr, None)
        self.connect(self.get_thread, QtCore.SIGNAL("progressBar(QString,QString)"), self.progressBar)
        self.get_thread.setFile(self.filelabel.text())
        self.get_thread.start()
    def progressBar(self,value,lenfile):
        self.arquivoProgressBar.setEnabled(True)

        if int(value) == -1 :

            self.arquivoProgressBar.setValue(100)
            self.popup = PopUpC(self, id, "Upload ERROR")
            self.popup.show()
        else:
            if self.arquivoProgressBar.value() < 100:
                a = int(lenfile)//512
                if int(value)> 0:
                    b = (int(value)//512)
                    c = int((b/a)*100)
                    self.arquivoProgressBar.setValue(c)
                    if self.arquivoProgressBar.value() == 100:
                        self.filebutton.setEnabled(True)
                        self.popup = PopUpC(self, self.filelabel.text(), "End of Upload")
                        self.popup.show()



    def closeEvent(self, QCloseEvent):

        self.get_thread.exit(0)
        QCloseEvent.accept()


class PopUpC(QtGui.QMainWindow, Popup.Ui_Popup):
    def __init__(self, parentApp, dsc, text = None, parent=None):
        super(PopUpC, self).__init__(parent)
        self.parentApp = parentApp
        self.setupUi(self)
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.close)
        if text:
            self.title.setText(text)
        self.description.setText("FileName : "+dsc)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.move(10000,10000)
