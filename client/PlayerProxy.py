from ..include import Classes_pb2
from UDPClient import socket

class proxy:
    try:
        socket = socket("localhost", 49110)
    except:
        print("Erro ao conectar com o servidor")

    def getAtleta(self, atleta):
        self.doOperation(atleta, "getAtleta")
        
    def doOperation(self, request, method):
        msg = self.empacotaMensagem(request, method)
        self.socket.sendRequest(msg)
        response = self.desempacotaMensagem(self.socket.getResponse()).ParseFromString()
        return response

    def empacotaMensagem(self, request, method):
        args = request.SerializeToString()
        return args
    
    def desempacotaMensagem(self, msg):
        response = Classes_pb2.Atleta()
        response.ParseFromString(msg)
        args = response.args()
        return args
        



