from PlayerProxy import Proxy
import sys


import Classes_pb2

class PlayerClient:
    proxy = Proxy()

    def menu(self):
        print("1 - Listar Jogadores")
        option = input("Digite a opção desejada: ")

        if option == "1":
            atleta.nome = input("Digite o nome do atleta: ")
            self.proxy.getAtleta(atleta)
        else:
            print("Opção inválida")
            self.menu()

    def getAtleta(self):
        self.proxy.getAtleta()

atleta = Classes_pb2.Atleta()

def main():
    choice = ""
    while choice != "exit":
        client = PlayerClient()
        client.menu()

main()