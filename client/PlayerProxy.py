import Classes_pb2
from termcolor import colored
import sys
from UDPClient import *

requestID = 0

class ArgsErrorException(Exception):
    def __init__(self, message="Invalid arguments"):
        self.message = message
        super().__init__(self.message)

class DuplicateRequestException(Exception):
    def __init__(self, message="Duplicate request"):
        self.message = message
        super().__init__(self.message)

class Proxy:
    socket = UDPClient("localhost", 49110)
    
    def getAtleta(self, atleta):
        bytes = self.doOperation(atleta, "getAtleta")
        atleta = Classes_pb2.Atleta()
        atleta.ParseFromString(bytes)
        #print("Posicao: " + atleta.DESCRIPTOR.enum_types_by_name['Posicao'].values_by_number[atleta.posicao].name)
        print("\nAtleta {\n")
        print(atleta)
        print("}\n")

    def addAtleta(self, atleta):
        bytes = self.doOperation(atleta, "addAtleta")
        atleta = Classes_pb2.Atleta()
        atleta.ParseFromString(bytes)
        #print("Posicao: " + atleta.DESCRIPTOR.enum_types_by_name['Posicao'].values_by_number[atleta.posicao].name)
        print(colored("\n{\n\n" + str(atleta) + "\n}", "yellow"))

        
    def doOperation(self, request, method):
        msg = self.empacotaMensagem(request, method)
        self.socket.sendRequest(msg)
        response = self.desempacotaMensagem(self.socket.getResponse())
        return response

    def empacotaMensagem(self, request, method):
        global requestID 
        message = Classes_pb2.Message()
        message.id = requestID
        message.methodID = method
        message.args = request.SerializeToString()
        return message.SerializeToString()
    
    def desempacotaMensagem(self, msg):
        global requestID
        response = Classes_pb2.Message()
        response.ParseFromString(msg)
        
        if response.error == 1:
            raise ArgsErrorException(response.args.decode())
        if response.id < requestID:
            raise DuplicateRequestException()

        requestID = requestID + 1
        bytes = response.args
        return bytes
        



