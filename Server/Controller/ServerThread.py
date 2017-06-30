import struct

from Controller import Thread
from PyQt4 import QtCore


class SocketHandle(QtCore.QThread):
    def __init__(self, server, dir,conn = 0):
        super(SocketHandle, self)
        super().__init__()
        self.server = server
        self.file = None
        self.threads = list()
        self.dir = dir
        self.conn = int(conn)

    def run(self):
        print("RODANDO")
        while True:
            data, addr = self.server.socket.recvfrom(1024)
            print(addr)
            header = self.dump(data)

            if header[2] == 0 :
                self.threads.append(Thread.ThreadServerConn(self.conn + 1, addr, self))
                self.threads[len(self.threads)-1].start()
                self.threads[len(self.threads)-1].placeData((data,addr))
                self.emit(QtCore.SIGNAL("newConn(QString)"), str(self.conn+1))
                self.conn +=1
            else:
                for t in self.threads:
                    if t.id == header[2]:
                        t.placeData((data, addr))
                        break
            for x in self.threads:
                if len(x.outstack) > 0:
                    a,b = x.outstack.pop()
                    self.signal(a,b,str(x.lenfile))

    def dump(self, data):
        return struct.unpack('@I I H b B '+str(len(data)-12)+'s', data)

    def getDir(self):
        return self.dir
    def signal(self,thread,value,lenfile):
        self.emit(QtCore.SIGNAL("progressBar(QString,QString,QString)"),thread,value,lenfile)

    def exit(self, returnCode=0):
        self.threads = None
        exit(0)
