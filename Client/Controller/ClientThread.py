import struct

from PyQt4 import QtCore

from Client.Controller import CThread

class SocketHandle(QtCore.QThread):
    def __init__(self, socket, serverAddr, file = None):
        super(SocketHandle, self)
        super().__init__()
        self.socket = socket
        self.file = file
        self.serverAddr = serverAddr
        self.id = 0
        self.client = None
        self.client = None

    def setFile(self,file):
        self.file = file
        self.client = CThread.ThreadClientConn(self.id, self.serverAddr, self, self.file)

    def run(self):
        self.client.start()
        while True:

            data, addr = self.socket.socket.recvfrom(1024)

            if data :

                if self.checkAddr(addr):
                    self.client.placeData((data,addr))
                else:
                    print("Invalid Server Address")

    def dump(self, data):
        return struct.unpack('@I I H b B ' + str(len(data) - 12) + 's', data)

    def checkAddr(self, addr):
        for i in range(len(addr)):
            if self.serverAddr[0][i] != addr[0][i]:
                return False
        return True


    def signal(self, value, lenfile):
        self.emit(QtCore.SIGNAL("progressBar(QString,QString)"), value, lenfile)