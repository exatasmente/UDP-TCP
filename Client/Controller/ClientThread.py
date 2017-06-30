import struct

from PyQt4 import QtCore

from Client.Controller import CThread



class SocketHandle(QtCore.QThread):
    def __init__(self, socket, serverAddr, file = None):
        super().__init__()
        self.socket = socket
        self.file = file
        self.serverAddr = serverAddr
        self.id = 0
        self.client = None
        self.client = CThread.ThreadClientConn(self.id, self.serverAddr
                                               , self, self.file)
        if file:
            self.client.start()

    def run(self):

        while True:

            data, addr = self.socket.socket.recvfrom(1024)
            print(addr)
            if data :
                eq = True
                for i in range(len(addr)):
                    if self.serverAddr[0][i] != addr[0][i]:
                        eq = False
                        break
                if eq:
                    self.client.placeData((data,addr))
                else:
                    print("Invalid Serve Address")

    def dump(self, data):
        return struct.unpack('@I I H b B ' + str(len(data) - 12) + 's', data)