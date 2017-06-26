import struct
import  threading
import time

from PyQt4 import  QtCore

from Client.Model import Header


class ThreadClientConn(threading.Thread,QtCore.QThread):


    def __init__(self, id, addr,parent,file):
        super().__init__()
        self.SSTHRESH = 1000
        self.CWND = 512
        threading.Thread.__init__(self)
        self.parent = parent
        self.queue = list()
        self.addr = addr
        self.id = id
        with open(file, 'rb') as f:
            self.file = f.read()
        self.filelen = len(self.file)
        self.deamon = True
        self.header = Header.Header(0, 0, 0, 0, 0, None)
        self.outstack = list()
    def run(self):
        payload = self.fileSplit()


        self.handShake(self.parent.serverAddr)


        lenfile = 0
        tempo = time.perf_counter()
        timeout = 0


        while True:

            if len(self.queue) > 0:
                data, addr = self.queue.pop()
                self.addr = addr

                tempo = time.perf_counter()

                header = self.dump(data)

                self.outstack.append(header)
                if len(self.file) == self.header.getSeqNum()-12346:

                    self.closeConn(addr)

                if header[1] > self.header.getSeqNum():
                    self.header.setSeqNum(header[1])

                elif header[1] == self.header.getSeqNum():
                    timeout += 1
                    if timeout == 3:
                        self.SSTHRESH = self.CWND
                        self.CWND = 512

            if lenfile <= len(self.file):

                try:
                    file = next(payload)

                    self.parent.socket.socket.sendto(self.makeHeader(self.header.getSeqNum(),
                                                          self.header.getAckNum(),
                                                          self.id,
                                                          0,
                                                          file,
                                                          False,
                                                          False,
                                                          False),
                                                              self.addr)
                    lenfile += len(file)
                except Exception:
                    self.closeConn(self.addr)
                    pass
                time.sleep(0.3)


                if self.CWND <= self.SSTHRESH:
                    self.CWND += 512

                elif self.CWND >= self.SSTHRESH:
                    self.CWND += (512*512)/self.CWND
                if tempo +10 <= time.perf_counter():
                    self.closeConn(self.addr,True)

    def handShake(self,addr):
        header = self.makeHeader(12345,
                                 0,
                                 0,
                                 0,
                                 str(self.filelen).encode(),
                                 False,
                                 True,
                                 False)
        print(self.dump(header))
        self.parent.socket.socket.sendto(header, addr)
        tempo = time.perf_counter()
        while True:
            if len(self.queue) > 0:
                data,addr = self.queue.pop()
                header = self.dump(data)

                if header[4] == 6:
                    self.setHeader(header)
                    self.header.setSeqNum(header[1])
                    self.header.setAckNum(header[0])
                    self.addr = addr
                    break

            if tempo + 10 <= time.perf_counter():
                raise ConnectionError("TIME OUT")




    def closeConn(self,addr,error = False):
        if error:

            raise ConnectionError("DEU RUIM")

        else:
            header = self.makeHeader(self.header.getSeqNum(),
                                     0,
                                     self.id,
                                     0,
                                     None,
                                     False,
                                     False,
                                     True)
            self.parent.socket.socket.sendto(header,addr)
            while True:
                if len(self.queue) > 0:
                    data, addr = self.queue.pop()
                    header = self.dump(data)
                    print(header)
                    if header[4] == 3:
                        self.setHeader(header)
                        exit(0)


    def setHeader(self, header):

         self.header.setSeqNum(header[0])
         self.header.setAckNum(header[1])
         self.id = header[2]
         self.header.setNotUse(header[3])
         self.header.setFlags(header[4])
         self.header.setData(header[5])

    def makeHeader(self, seqNum, ackNum, id, notUse, payload=None, a=False, s=False, f=False):
        flags = (f | (a << 1) | (s << 2))

        if payload:
            if flags == 4:
                print(payload)
                return struct.pack('@I I H b B ' + str(len(payload)) + 's', seqNum, ackNum, id, notUse, flags,
                                   payload)
            else:
                return struct.pack('@I I H b B ' + str(len(payload)) + 's', seqNum, ackNum, id, notUse, flags,
                                       payload)

        return struct.pack('@I I H b B ', seqNum, ackNum, id, notUse, flags)

    def dump(self, data):
        return struct.unpack('@I I H b B ' + str(len(data) - 12) + 's', data)


    def placeData(self, data):
        self.queue.append(data)

    def fileSplit(self):
        while True:
            if (self.header.getSeqNum()-12346)+512 <= len(self.file):
                yield self.file[(self.header.getSeqNum()-12346):(self.header.getSeqNum()-12346)+512]
            else:
                yield  self.file[(self.header.getSeqNum()-12346):-1]
                break



