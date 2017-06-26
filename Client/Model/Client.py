import socket


'''
Feito Com Amor em Python 3
Criado Por: Luiz Vieira Gonzaga Neto
Disciplina Redes de Computadores 2017.1 UFC CAMPUS RUSSAS

'''


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def getSock(self):
        return self.socket
    def setSock(self, socket):
        self.socket = socket

    def close(self):
        self.socket.close()
