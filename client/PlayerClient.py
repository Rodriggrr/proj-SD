from PlayerProxy import *
import Classes_pb2

#Código que deve ser executado pelo cliente
#onde cria uma instância da classe Proxy e chama os métodos

class PlayerClient:
    #Cria uma instância da classe Proxy
    proxy = Proxy()

    #Inicia o programa mostrando o menu de opções
    def menu(self):
        print("""
1 - Listar Jogadores
2 - Adicionar Jogador
""")
        option = input("Digite a opção desejada: ")

        if option == "1":
            atleta.nome      = input("Digite o nome do atleta: ")
            self.proxy.getAtleta(atleta)
        elif option =="2":
            atleta.nome      = input("Digite o nome do atleta: ")
            atleta.idade     = int(input("Digite a idade do atleta: "))
            
            posicao = input("""
Digite a Posição:
                             
1 - Goleiro
2 - Zagueiro
3 - Lateral
4 - Meio Campo
5 - Atacante
""")
            #chama o enum de acordo com a opção escolhida
            if   posicao == "1":
                atleta.posicao = Classes_pb2.Atleta.GOLEIRO
            elif posicao == "2":
                atleta.posicao = Classes_pb2.Atleta.ZAGUEIRO
            elif posicao == "3":
                atleta.posicao = Classes_pb2.Atleta.LATERAL
            elif posicao == "4":
                atleta.posicao = Classes_pb2.Atleta.MEIO_CAMPO
            elif posicao == "5":
                atleta.posicao = Classes_pb2.Atleta.ATACANTE
                
            atleta.numCamisa = int(input("Digite o número da camisa do atleta: "))
            atleta.time = input("Digite o time do atleta: ")
            self.proxy.addAtleta(atleta)
        else:
            print("Opção inválida")
            self.menu()

    def getAtleta(self):
        self.proxy.getAtleta()

#Instancia um objeto da classe Atleta
atleta = Classes_pb2.Atleta()

def main():
    
    while True:
        try:
            #É criado um objeto da classe PlayerClient e chama o método menu()
            client = PlayerClient()
            client.menu()
        except ServerTimedOutException as e:
            #Caso o servidor não responda dentro do tempo limite, o programa é encerrado por timeout
            print("Erro: " + str(e))
            sys.exit(0)
        except ArgsErrorException as e:
            #Caso o servidor responda com erro, o programa é encerrado e mostra a mensagem de erro
            print(colored("Erro: " + str(e), "red"))
        except DuplicateRequestException as e:
            None #Descarta a mensagem duplicada
        
main()