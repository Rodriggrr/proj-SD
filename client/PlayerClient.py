from PlayerProxy import proxy
from ..include import Classes_pb2

class PlayerClient:
    def __init__(self):
        self.proxy = proxy()

    def menu(self):
        print("1 - Listar Jogadores")
        option = input("Digite a opção desejada: ")

        if option == "1":
            atleta.nome = input("Digite o nome do atleta: ")
            proxy.getAtleta(atleta)
        else:
            print("Opção inválida")
            self.menu()

    def getAtleta(self):
        self.proxy.getAtleta()

atleta = Classes_pb2.Player()