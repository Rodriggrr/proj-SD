import Classes_pb2
from termcolor import colored
from UDPClient import *

class ArgsErrorException(Exception):
    def __init__(self, message="Invalid arguments"):
        self.message = message
        super().__init__(self.message)

class Proxy:
    socket = UDPClient("localhost", 49110)
    
    def getAtleta(self, atleta):
        bytes = self.doOperation(atleta, "getAtleta")
        atleta = Classes_pb2.Atleta()
        atleta.ParseFromString(bytes)
        #print("Posicao: " + atleta.DESCRIPTOR.enum_types_by_name['Posicao'].values_by_number[atleta.posicao].name)
        print(colored("\n{\n\n" + str(atleta) + "\n}", "yellow"))

    def addAtleta(self, atleta):
        bytes = self.doOperation(atleta, "addAtleta")
        atleta = Classes_pb2.Atleta()
        atleta.ParseFromString(bytes)
        #print("Posicao: " + atleta.DESCRIPTOR.enum_types_by_name['Posicao'].values_by_number[atleta.posicao].name)
        print("\n{\n")
        print(atleta)
        print("}")
        
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
        if response.error == 1:
            raise ArgsErrorException(response.args.decode())
        bytes = response.args
        return bytes
        



