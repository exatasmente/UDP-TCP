from Model import  Server
from PyQt4 import QtGui, QtCore
from View import  Popup
from View import janela4

from Server.Controller import ServerThread

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






class MainWindow(QtGui.QMainWindow, janela4.Ui_MainWindow):
    def __init__(self,parentApp,ip,port, parent=None,):
        super(MainWindow, self).__init__(parent)
        self.parentApp = parentApp
        self.windows = list()
        self.setupUi(self)
        self.conn = 0
        with open('/root/PycharmProjects/TCP over UDP/conn.bin','r') as conn:
            self.conn = conn.read()

        self.get_thread = ServerThread.SocketHandle(Server.Servidor(ip, port), "/", self.conn)

        self.connect(self.get_thread, QtCore.SIGNAL("progressBar(QString,QString,QString)"), self.progressBar)
        self.connect(self.get_thread, QtCore.SIGNAL("newConn(QString)"), self.newDir)
        self.connect(self.get_thread, QtCore.SIGNAL("closeConn(QString)"), self.delDir)
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
                    self.popup = PopUpC(self, id, "End of Upload")
                    self.popup.show()


    def delDir(self):
        label = self.sender()
        id = label.objectName()
        self.findChild(QtGui.QFormLayout, id).deleteLater()
        self.findChild(QtGui.QPushButton,id).deleteLater()
        self.findChild(QtGui.QLabel, id).deleteLater()
        self.findChild(QtGui.QProgressBar,id).deleteLater()



    def newDir(self,dirName):

       formLayout = QtGui.QFormLayout()
       formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
       formLayout.setObjectName(_fromUtf8(dirName))
       diretorioLabel = QtGui.QPushButton(self.gridLayoutWidget_2)
       diretorioLabel.setFlat(True)
       diretorioLabel.setEnabled(False)
       diretorioLabel.setGeometry(QtCore.QRect(1, 1, 27, 14))
       diretorioLabel.setObjectName(_fromUtf8(dirName))
       formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, diretorioLabel)
       arquivoLabel = QtGui.QLabel(self.gridLayoutWidget_2)
       arquivoLabel.setObjectName(_fromUtf8(dirName))
       formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, arquivoLabel)
       arquivoProgressBar = QtGui.QProgressBar(self.gridLayoutWidget_2)
       arquivoProgressBar.setProperty("value", 0)
       arquivoProgressBar.setObjectName(_fromUtf8(dirName))

       formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, arquivoProgressBar)
       diretorioLabel.setText(_translate("MainWindow", " X  ", None))
       arquivoLabel.setText(_translate("MainWindow", dirName, None))
       diretorioLabel.setToolTip("Fechar")
       diretorioLabel.clicked.connect(self.delDir)
       self.verticalLayout.addLayout(formLayout)
       self.popup = PopUpC(self,dirName)
       self.popup.show()

    def closeEvent(self, QCloseEvent):

        with open('conn.bin','w') as conn:
            conn.write(str(self.get_thread.conn))

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
        else:
            self.title.setText("New File ")
        self.description.setText("Connection Nº: "+dsc)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.move(10000,10000)
