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

class Ui_FileUpload(object):
    def setupUi(self, FileUpload):
        FileUpload.setObjectName(_fromUtf8("FileUpload"))
        FileUpload.resize(374, 300)
        FileUpload.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtGui.QWidget(FileUpload)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 240, 111, 41))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 113, 31))
        self.lineEdit.setPlaceholderText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 130, 81, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 130, 31, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 130, 41, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 50, 261, 61))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dirbutton = QtGui.QPushButton(self.centralwidget)
        self.dirbutton.setGeometry(QtCore.QRect(140, 170, 83, 24))
        self.dirbutton.setObjectName(_fromUtf8("dirbutton"))
        self.dirlabel = QtGui.QLabel(self.centralwidget)
        self.dirlabel.setGeometry(QtCore.QRect(50, 200, 271, 20))
        self.dirlabel.setText(_fromUtf8(""))
        self.dirlabel.setObjectName(_fromUtf8("dirlabel"))
        FileUpload.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FileUpload)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FileUpload.setStatusBar(self.statusbar)

        self.retranslateUi(FileUpload)
        QtCore.QMetaObject.connectSlotsByName(FileUpload)

    def retranslateUi(self, FileUpload):
        FileUpload.setWindowTitle(_translate("FileUpload", "File UpLoad", None))
        self.pushButton.setText(_translate("FileUpload", "Conectar", None))
        self.lineEdit.setText(_translate("FileUpload", "127.0.0.1", None))
        self.lineEdit_2.setText(_translate("FileUpload", "5000", None))
        self.label.setText(_translate("FileUpload", "IP", None))
        self.label_2.setText(_translate("FileUpload", "PORTA", None))
        self.label_3.setText(_translate("FileUpload", "Digite o IP e a Porta Servidor", None))
        self.dirbutton.setText(_translate("FileUpload", "Diretório", None))
