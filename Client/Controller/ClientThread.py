import struct

from PyQt4 import QtCore

from Controller import CThread
from Model import Client


class SocketHandle(QtCore.QThread):
    def __init__(self, socket, serverAddr, file = None):
        super().__init__()
        self.socket = socket
        self.file = file
        self.serverAddr = serverAddr
        self.id = 0
        self.client = None
        self.client = CThread.ThreadClientConn(self.id, None, self, self.file)
        if file:
            self.client.start()

    def run(self):

        while True:

            data, addr = self.socket.socket.recvfrom(1024)

            if data:
                self.client.placeData((data,addr))



    def dump(self, data):
        return struct.unpack('@I I H b B ' + str(len(data) - 12) + 's', data)


def main():
    server = Client.Client()
    s = SocketHandle(server, '/root/Downloads/Model.py',('127.0.1',5000))
    s.run()


if __name__ == '__main__':
        main()

