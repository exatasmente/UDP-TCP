import sys

from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import *
from Server.View import janela1
from Server.View import  MainWindow
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





class App(QApplication):
    def __init__(self,argv = None):
        super(App, self).__init__(argv)
        self.windows = list()
        win = Window(self)
        win.show()
        self.windows.append(win)

class Window(QMainWindow, janela1.Ui_FileUpload):
    def __init__(self, parentApp, parent=None):
        super(Window, self).__init__(parent)
        self.parentApp = parentApp
        self.setupUi(self)
        self.pushButton.clicked.connect(self.startServer)
        self.pushButton.setShortcut(QtCore.Qt.Key_Return)
        self.dirbutton.clicked.connect(self.dirSelect)

        self.alert = None
    def startServer(self):
        if self.label_2.text() and self.label_3.text() and self.dirlabel.text():
            ip, port =self.lineEdit.text(),self.lineEdit_2.text()
            win = MainWindow.MainWindow(self, ip, int(port),self.dirlabel.text())
            self.parentApp.windows.pop()
            self.parentApp.windows.append(win)
            win.show()
            self.close()
        else:
            alert = QMessageBox()
            alert.setText("Preencha Todos os campos e escolha um diretorio Válido")
            alert.setWindowTitle("Alerta!")
            alert.setIcon(QMessageBox.Warning)
            alert.setStandardButtons(QMessageBox.Ok)
            self.alert = alert
            self.alert.show()
    def dirSelect(self):
        self.dirlabel.setText(QFileDialog.getExistingDirectory())



def main():
    app = App(sys.argv)

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()


