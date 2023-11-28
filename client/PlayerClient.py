from PlayerProxy import *
import Classes_pb2
from options import *
import tkinter as tk

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
3 - Listar Times
4 - Adicionar Time
""")
        
        janela = tk.Tk()
        janela.title("Campeonato")
        janela.geometry("500x500")
        
        pesquisarPlayer = tk.Button(janela, text="Pesquisar", command=op.pesquisarPlayer)
        addPlayer = tk.Button(janela, text="Adicionar", command=op.adicionarPlayer)
        pesquisarTime = tk.Button(janela, text="Pesquisar", command=op.pesquisarTime)
        addTime = tk.Button(janela, text="Adicionar", command=op.adicionarTime)
        pesquisarPlayer.pack()
        addPlayer.pack()
        pesquisarTime.pack()
        addTime.pack()

        janela.mainloop()
        

#Instancia um objeto da classe Atleta
atleta = Classes_pb2.Atleta()
time = Classes_pb2.Time()
op = Options()

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