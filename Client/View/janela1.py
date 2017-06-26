# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileupload.ui'
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

class Ui_FileUpload(object):
    def setupUi(self, FileUpload):
        FileUpload.setObjectName(_fromUtf8("FileUpload Server"))
        FileUpload.resize(374, 300)
        FileUpload.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtGui.QWidget(FileUpload)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.StartButton = QtGui.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(130, 200, 111, 41))
        self.StartButton.setFlat(False)
        self.StartButton.setObjectName(_fromUtf8("pushButton"))
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
        FileUpload.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FileUpload)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FileUpload.setStatusBar(self.statusbar)

        self.retranslateUi(FileUpload)
        QtCore.QMetaObject.connectSlotsByName(FileUpload)

    def retranslateUi(self, FileUpload):
        FileUpload.setWindowTitle(_translate("FileUpload Client", "File UpLoad Client", None))
        self.StartButton.setText(_translate("FileUpload Client", "Conectar", None))
        self.lineEdit.setText(_translate("FileUpload Client", "127.0.0.1", None))
        self.lineEdit_2.setText(_translate("FileUpload Client", "5000", None))
        self.label.setText(_translate("FileUpload Client", "IP", None))
        self.label_2.setText(_translate("FileUpload Client", "PORTA", None))
        self.label_3.setText(_translate("FileUpload Client", "Digite o IP e a Porta Servidor", None))


c
