import Classes_pb2
from UDPClient import UDPClient

class Proxy:
    socket = UDPClient("localhost", 49110)
    
    def getAtleta(self, atleta):
        bytes = self.doOperation(atleta, "getAtleta")
        atleta = Classes_pb2.Atleta()
        atleta.ParseFromString(bytes)
        print("Posicao: " + atleta.DESCRIPTOR.enum_types_by_name['Posicao'].values_by_number[atleta.posicao].name)
        print(atleta)

    def addAtleta(self, atleta):
        bytes = self.doOperation(atleta, "addAtleta")
        atleta = Classes_pb2.Atleta()
        atleta.ParseFromString(bytes)
        print("Posicao: " + atleta.DESCRIPTOR.enum_types_by_name['Posicao'].values_by_number[atleta.posicao].name)
        print(atleta)
        
    def doOperation(self, request, method):
        msg = self.empacotaMensagem(request, method)
        self.socket.sendRequest(msg)
        response = self.desempacotaMensagem(self.socket.getResponse())
        return response

    def empacotaMensagem(self, request, method):
        message = Classes_pb2.Message()
        message.methodID = method
        message.args = request.SerializeToString()
        return message.SerializeToString()
    
    def desempacotaMensagem(self, msg):
        response = Classes_pb2.Message()
        response.ParseFromString(msg)
        bytes = response.args
        return bytes
        



