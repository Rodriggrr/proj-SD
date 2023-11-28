import Classes_pb2
from termcolor import colored
import sys
from UDPClient import *

requestID = 0

#Proxy tem a função de fazer a comunicação entre o cliente e o servidor

#Classe de exceção personalizada para argumentos inválidos
class ArgsErrorException(SystemExit):
    def __init__(self, message="Invalid arguments"):
        self.message = message
        super().__init__(self.message)

#Classe de exceção personalizada para requisição duplicada
class DuplicateRequestException(SystemExit):
    def __init__(self, message="Duplicate request"):
        self.message = message
        super().__init__(self.message)

class Proxy:
    #Instancia um socket da classe UDPClient
    socket = UDPClient("localhost", 49110)
    
    #Função para mostrar um atleta
    def getAtleta(self, atleta):
        #Chama o método doOperation passando o objeto atleta e o respectivo método
        bytes = self.doOperation(atleta, "getAtleta", "Campeonato")
        #Instancia um objeto da classe Atleta
        atleta = Classes_pb2.Atleta()
        #Recebe a resposta doOperation e printa no objeto atleta
        atleta.ParseFromString(bytes)
        print(colored("\n{\n\n" + str(atleta) + "\n}", "yellow"))
        return atleta

    #Função para adicionar um atleta
    def addAtleta(self, atleta):
        bytes = self.doOperation(atleta, "addAtleta", "Campeonato")
        atleta = Classes_pb2.Atleta()
        atleta.ParseFromString(bytes)
        print(colored("\n{\n\n" + str(atleta) + "\n}", "yellow"))

    def getTime(self, time):
        bytes = self.doOperation(time, "getTime", "Campeonato")
        time = Classes_pb2.Time()
        time.ParseFromString(bytes)
        print(colored("\n{\n\n" + str(time) + "\n}", "yellow"))

    def addTime(self, time):
        bytes = self.doOperation(time, "addTime", "Campeonato")
        time = Classes_pb2.Time()
        time.ParseFromString(bytes)
        print(colored("\n{\n\n" + str(time) + "\n}", "yellow"))
    
    def getTecnico(self, time):
        bytes = self.doOperation(time, "getTecnico", "Campeonato")
        tecnico = time.Tecnico()
        tecnico.ParseFromString(bytes)
        print(colored("\n{\n\n" + str(tecnico) + "\n}", "yellow"))

    #doOperation tem a função de realizar a operação em si
    def doOperation(self, request, method, objRef = None):
        msg = self.empacotaMensagem(request, method, objRef)
        self.socket.sendRequest(msg)
        response = self.desempacotaMensagem(self.socket.getResponse())
        return response

    #empacotaMensagem tem a função de empacotar a mensagem para ser enviada ao servidor
    #adicinando o id da requisição, o método e os argumentos
    def empacotaMensagem(self, request, method, objRef = None):
        global requestID 
        message = Classes_pb2.Message()
        message.id = requestID
        message.objRef = objRef
        message.methodID = method
        message.args = request.SerializeToString()
        return message.SerializeToString()
    
    #desempacotaMensagem tem a função de desempacotar a mensagem recebida do servidor
    #e retorna os argumentos
    def desempacotaMensagem(self, msg):
        global requestID
        
        response = Classes_pb2.Message()
        response.ParseFromString(msg)
        
        if response.error == 1:
            #Caso o servidor responda com erro, lança uma exceção personalizada ArgsErrorException
            raise ArgsErrorException(response.args.decode())
        if response.id < requestID:
            #Se a requisição for duplicada, lança uma exceção personalizada DuplicateRequestException
            raise DuplicateRequestException()

        #Atualiza o id esperado para a próxima requisição
        requestID = requestID + 1

        #Retorna os argumentos
        bytes = response.args
        return bytes