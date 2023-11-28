from interface import *

#Código que deve ser executado pelo cliente
#onde cria uma instância da classe Proxy e chama os métodos

class PlayerClient:

    def menu():
        interface = Interface()
        interface.Janela()
        
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
            #Descarta a mensagem duplicada
            print(e) 
        
main()