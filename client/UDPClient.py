import socket
from timeout_decorator import timeout

class UDPClient:
    name = 'localhost'
    port = 49110
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, name, port):
        self.name = name
        self.port = port

    def sendRequest(self, bytes):
        self.socket.sendto(bytes, (self.name, self.port))

    @staticmethod
    @timeout(2) 
    def _getResponse():
        return UDPClient.socket.recv(1024)

    def getResponse(self):
        response = self._getResponse()
        return response
        
            

    
