import socket

class UDPClient:
    name = 'localhost'
    port = 49110
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, name, port):
        self.name = name
        self.port = port

    def sendRequest(self, bytes):
        self.socket.sendto(bytes, (self.name, self.port))

    def getResponse(self):
        return self.socket.recv(1024)
    
