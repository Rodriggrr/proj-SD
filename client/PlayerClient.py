from PlayerProxy import proxy
from ..proto import player_pb2 as player

class PlayerClient:
    def __init__(self):
        self.proxy = proxy()

    def menu(self):
        print("1 - Listar Jogadores")
        option = input("Digite a opção desejada: ")

        if option == "1":
            nome = input("Digite o nome do jogador: ")
            self.getAtleta(nome)
        else:
            print("Opção inválida")
            self.menu()

    def getAtleta(self):
        self.proxy.getAtleta()

