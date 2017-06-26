import sys

from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import *
from View import MainWindow

from Server.View import janela1

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
        self.StartButton.clicked.connect(self.startServer)
        self.StartButton.setShortcut(QtCore.Qt.Key_Return)

    def startServer(self):
        if self.label_2.text() and self.label_3.text():
            ip, port =self.lineEdit.text(),self.lineEdit_2.text()
            win = MainWindow.MainWindow(self, ip, int(port))
            self.parentApp.windows.pop()
            self.parentApp.windows.append(win)
            win.show()
            self.close()


def main():
    app = App(sys.argv)

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()

