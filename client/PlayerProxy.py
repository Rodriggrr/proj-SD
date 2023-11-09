from Classes_pb2 import *
from UDPClient import UDPClient

class Proxy:
    socket = UDPClient("localhost", 49110)
    
    def getAtleta(self, atleta):
        bytes = self.doOperation(atleta, "getAtleta")
        atleta = Atleta()
        atleta.ParseFromString(bytes)
        print(atleta)

    def addAtleta(self, atleta):
        bytes = self.doOperation(atleta, "addAtleta")
        atleta = Atleta()
        atleta.ParseFromString(bytes)
        print(atleta)
        
    def doOperation(self, request, method):
        msg = self.empacotaMensagem(request, method)
        self.socket.sendRequest(msg)
        response = self.desempacotaMensagem(self.socket.getResponse())
        return response

    def empacotaMensagem(self, request, method):
        message = Message()
        message.methodID = method
        message.args = request.SerializeToString()
        return message.SerializeToString()
    
    def desempacotaMensagem(self, msg):
        response = Message()
        response.ParseFromString(msg)
        bytes = response.args
        return bytes
        



