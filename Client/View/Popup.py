# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
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

class Ui_Popup(object):
    def setupUi(self, Popup):
        Popup.setObjectName(_fromUtf8("Popup"))
        Popup.resize(200, 70)
        Popup.setMinimumSize(QtCore.QSize(200, 70))
        self.description = QtGui.QLabel(Popup)
        self.description.setGeometry(QtCore.QRect(10, 40, 173, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        self.description.setMinimumSize(QtCore.QSize(30, 20))
        self.description.setMaximumSize(QtCore.QSize(173, 20))
        self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description.setObjectName(_fromUtf8("description"))
        self.title = QtGui.QLabel(Popup)
        self.title.setGeometry(QtCore.QRect(10, 10, 94, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(27, 10))
        self.title.setMaximumSize(QtCore.QSize(94, 24))
        self.title.setObjectName(_fromUtf8("title"))
        self.button = QtGui.QPushButton(Popup)
        self.button.setGeometry(QtCore.QRect(150, 10, 43, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setMinimumSize(QtCore.QSize(43, 21))
        self.button.setMaximumSize(QtCore.QSize(20, 10))
        self.button.setFlat(True)
        self.button.setObjectName(_fromUtf8("button"))

        self.retranslateUi(Popup)
        QtCore.QMetaObject.connectSlotsByName(Popup)

    def retranslateUi(self, Popup):
        Popup.setWindowTitle(_translate("Popup", "Popup", None))
        self.description.setText(_translate("Popup", "Body", None))
        self.title.setText(_translate("Popup", "Title", None))
        self.button.setText(_translate("Popup", "×", None))
