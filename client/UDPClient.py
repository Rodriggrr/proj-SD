import socket

class UDPClient:
    name = 'localhost'
    port = 49110
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, name, port):
        self.name = name
        self.port = port
        
    def connect(self, name=name, port=port):
        status = self.socket.connect((self.name, self.port))
        if status == 0:
            print('Connected to {}:{}'.format(self.name, self.port))

    def sendRequest(self, text):
        self.socket.send(text.encode('utf-8'))

    def getResponse(self):
        return self.socket.recv(1024).decode('utf-8')
    
