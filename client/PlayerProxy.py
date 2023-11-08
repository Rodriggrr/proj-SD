from ..include import Classes_pb2
from UDPClient import socket

class proxy:
    try:
        socket = socket("localhost", 49110)
    except:
        print("Erro ao conectar com o servidor")

    def getAtleta(self, nome):
        request = player_pb2.Player()
        request.name = nome
        self.doOperation(request, "getAtleta")

    def doOperation(self, request, method):
        msg = self.empacotaMensagem(request, method)
        self.socket.sendRequest(msg)
        response = self.desempacotaMensagem(self.socket.getResponse())
        return response

    def empacotaMensagem(self, request, method):
        self.ID += 1
        self.ultimoID = self.ID

        packed_message = {
            "ID": self.ID,
            "method": method,
            "request": request.SerializeToString()
        }

        return packed_message.serializeToString()
    
    def desempacotaMensagem(self, msg):
        unpacked_message = {
            "ID": msg["ID"],
            "method": msg["method"],
            "response": player_pb2.Player().ParseFromString(msg["response"])
        }

        if unpacked_message["ID"] <= self.ultimoID:
            print("Pacote duplicado detectado. Descartando pacote.")
            return None
        
        return unpacked_message
        



