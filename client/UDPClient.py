import socket
from timeout_decorator import timeout

class ServerTimedOutException(Exception):
    def __init__(self, message="O tempo limite do servidor foi excedido, está fora do ar?"):
        self.message = message
        super().__init__(self.message)

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
        errors = 0
        while True:
            if errors == 3:
                raise ServerTimedOutException()
            try:
                response = self._getResponse()
            except Exception as e:
                errors += 1
                continue
            break
        return response
        
            

    
