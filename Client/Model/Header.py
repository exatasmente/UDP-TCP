class Header:
    def __init__(self,ackNum,seqNum,id,notUse,flags,data):
        self.ackNum = ackNum
        self.id = id
        self.notUse = notUse
        self.seqNum = seqNum
        self.flags = flags
        self.data = data


    def getAckNum (self):
        return self.ackNum
    def setAckNum (self, ackNum):
        self.ackNum = ackNum
    def getId (self):
        return  self.id
    def setId (self, id):
        self.id = id
    def getNotUse(self):
        return  self.notUse
    def setNotUse(self,notUse):
        self.notUse = notUse
    def getSeqNum(self):
        return self.seqNum
    def setSeqNum(self,seqNum):
        self.seqNum = seqNum
    def getFlags(self,):
        return self.flags
    def setFlags(self,f):
        self.flags == 0

    def getData(self):
        return self.data
    def setData(self,data):
        self.data = data

