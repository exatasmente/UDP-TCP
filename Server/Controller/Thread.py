import struct
import  threading
import time

from PyQt4 import QtCore

from Client.Model import Header


class ThreadServerConn(threading.Thread, QtCore.QThread):

    def __init__(self, id, addr,parent):
        super(ThreadServerConn, self)
        super().__init__()
        threading.Thread.__init__(self)
        self.parent = parent
        self.queue = list()
        self.addr = addr
        self.id = id
        self.file = None
        self.deamon = True
        self.outstack= list()
        self.lenfile  = 0
        self.end = False
        self.header = Header.Header(0, 0, 0, 0, 0, None)


    def run(self):
        tempo = time.perf_counter()
        while True:
            if len(self.queue) > 0:
                data, addr = self.queue.pop()
                header = self.dump(data)

                if header[4] == 4:

                    self.handShake(header,addr)
                    self.lenfile = header[5].decode('utf-8')
                    break

            if tempo + 10 <= time.perf_counter():
                del self.parent.threads[self.id-1]
                raise ConnectionError("TIME OUT")


        tempo = time.perf_counter()
        while True:

            if len(self.queue) > 0:
                data, addr = self.queue.pop()
                header = self.dump(data)

                if header[4] == 1:
                    self.closeConn(addr)
                    break
                tempo = time.perf_counter()
                if len(header) == 6:
                    self.outstack.append(header)

                    self.write(header[5])
                    self.header.setAckNum(header[0]+len(header[5]))
                    self.header.setSeqNum(header[1])

                    Theader = self.makeHeader(self.header.getSeqNum(),
                                             self.header.getAckNum(),
                                             self.id,
                                             0,
                                             None,
                                             True,
                                             False,
                                             False)

                    self.parent.server.socket.sendto(Theader, addr)
                    self.outstack.append(((str(header[0] - 12346)), str(self.id)))



            if tempo + 10 <= time.perf_counter():
                self.write("ERRO".encode(),True)
                raise ConnectionError("TIME OUT")


    def setHeader(self, header):
        self.header.setSeqNum(header[0])
        self.header.setAckNum(header[1])
        self.header.setNotUse(header[3])
        self.header.setFlags(header[4])

        if len(header) == 6:
            self.header.setData(header[5])

    def handShake(self,data,addr):
        self.setHeader(data)
        header = self.makeHeader(4321,
                                 12346,
                                 self.id,
                                 0,
                                 None,
                                 True,
                                 True,
                                 False)


        self.parent.server.socket.sendto(header, addr)

    def closeConn(self,addr):
        header = self.makeHeader(self.header.getSeqNum(),
                                 self.header.getAckNum(),
                                 self.id,
                                 0,
                                 None,
                                 True,
                                 False,
                                 True)
        self.parent.server.socket.sendto(header,addr)

        self.parent.threads.remove(self)



    def makeHeader(self, seqNum, ackNum, id, notUse, payload=None, a=False, s=False, f=False):
        flags = (f | (a << 1) | (s << 2))
        if payload:
            return struct.pack('@I I H b B ' + str(len(payload)) + 's', seqNum, ackNum, id, notUse, flags, payload)

        return struct.pack('@I I H b B ', seqNum, ackNum, id, notUse, flags)

    def dump(self, data):
        if len(data)-12 > 0:
            return struct.unpack('@I I H b B '+str(len(data)-12)+'s', data)
        else:
            return struct.unpack('@I I H b B ', data)

    def write(self, data,error= False):
        if error:
            with open(str(self.id) + '.file', 'wb') as file:
                file.write(data)
        else:
            with open(str(self.id) + '.file', 'ab') as file:
                file.write(data)


    def placeData(self,data):
        self.queue.append(data)

