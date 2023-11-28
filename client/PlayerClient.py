import Classes_pb2
import sys
from PlayerProxy import *
from interface import *

class PlayerClient:

    campeonato = Proxy()

    def menu(self):
        # limpa a tela
        print("\033c")

        print(""" 
Selecione uma opção:
              
1 - Adicionar Time
2 - Pesquisar Time
3 - Adicionar Atleta
4 - Pesquisar Atleta
5 - Pesquisar Técnico 
              """)
        op = int(input(">> "))
    
        if op == 1:
            time.nome = input("Digite o nome do time: ")
            tecnico.nome = input(colored("Digite o nome do técnico: ", "blue"))
            tecnico.idade = int(input(colored("Digite a idade do técnico: ", "blue")))
            tecnico.qtdTitulos = int(input(colored("Digite a quantidade de títulos do técnico: ", "blue")))
            time.tecnico = tecnico.SerializeToString()
            time.pontos = int(input("Digite a quantidade de pontos do time: "))
            time.qtdJogos = int(input("Digite a quantidade de jogos do time: "))

            self.campeonato.addTime(time)

        elif op == 2:
            time.nome = input("Digite o nome do time: ")
            self.campeonato.getTime(time)
        
        elif op == 3:
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
            self.campeonato.addAtleta(atleta)
        
        elif op == 4:
            atleta.nome = input("Digite o nome do atleta: ")
            self.campeonato.getAtleta(atleta) 
        
        elif op == 5:
            time.nome = input("Digite o nome do time do tecnico: ")
            self.campeonato.getTecnico(time)

    def inter(self):
        interface = Interface()
        interface.Janela()

atleta = Classes_pb2.Atleta()
time = Classes_pb2.Time()
tecnico = time.Tecnico()

def main():
    
    while True:
        try:
            #É criado um objeto da classe PlayerClient e chama o método menu()
            client = PlayerClient()
            # client.inter()
            client.menu()
        except ServerTimedOutException as e:
            #Caso o servidor não responda dentro do tempo limite, o programa é encerrado por timeout
            print("Erro: " + str(e))
            sys.exit(0)
        except ArgsErrorException as e:
            #Caso o servidor responda com erro, o programa é encerrado e mostra a mensagem de erro
            print(colored("Erro: " + str(e), "red"))
        except DuplicateRequestException as e:
            #Descarta a mensagem duplicada
            print(e) 
        
        print("Pressione ENTER para continuar...")
        input()
main()