import socket


'''
Feito Com Amor em Python 3
Criado Por: Luiz Vieira Gonzaga Neto
Disciplina Redes de Computadores 2017.1 UFC CAMPUS RUSSAS

'''


class Servidor:
    def __init__(self, IP, PORT):
        self.ip = IP
        self.port = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((IP, PORT))

    def getSock(self):
        return self.socket
    def setSock(self, socket):
        self.socket = socket

    def close(self):
        self.socket.close()
