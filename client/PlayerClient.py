from PlayerProxy import Proxy
import sys


import Classes_pb2

class PlayerClient:
    proxy = Proxy()

    def menu(self):
        print("""
1 - Listar Jogadores
2 - Adicionar Jogador
""")
        option = input("Digite a opção desejada: ")

        if option == "1":
            atleta.nome = input("Digite o nome do atleta: ")
            self.proxy.getAtleta(atleta)
        elif option =="2":
            atleta.nome      = input("Digite o nome do atleta: ")
            atleta.idade     = int(input("Digite a idade do atleta: "))
            atleta.posicao   = input("Digite a posição do atleta: ")
            atleta.numCamisa = int(input("Digite o número da camisa do atleta: "))
            atleta.time = input("Digite o time do atleta: ")
            self.proxy.addAtleta(atleta)
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