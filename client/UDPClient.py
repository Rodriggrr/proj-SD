import socket
from timeout_decorator import timeout

class ServerTimedOutException(SystemExit):
    def __init__(self, message="O tempo limite do servidor foi excedido, está fora do ar?"):
        self.message = message
        super().__init__(self.message)

#classe que faz conexão com o servidor
class UDPClient:
    #valores padrão para o host e porta
    name = 'localhost'
    port = 49110

    #cria o socket
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #incializa a instância da classe
    def __init__(self, name, port):
        self.name = name
        self.port = port

    #envia a requisição para o servidor
    def sendRequest(self, bytes):
        self.socket.sendto(bytes, (self.name, self.port))

    @staticmethod
    @timeout(2) 
    def _getResponse():
        #metodo estático que recebe a resposta do servidor com timeout de 2 segundos
        return UDPClient.socket.recv(1024)

    def getResponse(self):
        errors = 0
        while True:
            #Lança uma exceção personalizada ServerTimedOutException, caso o servidor não responda em 3 tentativas
            if errors == 3:
                raise ServerTimedOutException()
            try:
                #Recebe a resposta do servidor
                response = self._getResponse()
            except Exception as e:
                #Caso o servidor não responda, incrementa o contador de erros e tenta novamente
                errors += 1
                continue
            break
        return response
        
            

    
