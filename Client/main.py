from Client.Controller import  ClientThread
from Client.Model import  Client
import sys
def main(ip,port,filem):
    server = Client.Client()
    s = ClientThread.SocketHandle(server,(str(ip),int(port)),str(filem))
    s.run()


if __name__ == '__main__':
        main(sys.argv[0],sys.argv[1],sys.argv[2])
