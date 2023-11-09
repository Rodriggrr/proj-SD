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
            
            posicao = input ("""
Digite a Posição:
                             
1 - Goleiro
2 - Zagueiro
3 - Lateral
4 - Meio Campo
5 - Atacante
""")
            if posicao == "1":
                atleta.posicao = Classes_pb2.Atleta.GOLEIRO
            elif posicao == "2":
                atleta.Posicao.ZAGUEIRO
            elif posicao == "3":
                atleta.Posicao.LATERAL
            elif posicao == "4":
                atleta.Posicao.MEIOCAMPO
            elif posicao == "5":
                atleta.Posicao.ATACANTE
                
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
   
    while true:
        client = PlayerClient()
        client.menu()
        


main()
print("não foi possível conectar ao servidor")