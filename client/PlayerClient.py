from options import *
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


#Código que deve ser executado pelo cliente
#onde cria uma instância da classe Proxy e chama os métodos

class PlayerClient:
    #Cria uma instância da classe Proxy
    proxy = Proxy()

    #Inicia o programa mostrando o menu de opções
    def menu(self):

        def centralizeWindow(janela):
            janela.update_idletasks()
            width = janela.winfo_width()
            height = janela.winfo_height()
            x = (janela.winfo_screenwidth() // 2) - (width // 2)
            y = (janela.winfo_screenheight() // 2) - (height // 2)
            janela.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        print("""
1 - Listar Jogadores
2 - Adicionar Jogador
3 - Listar Times
4 - Adicionar Time
""")
        
        janela = tk.Tk()
        janela.title("Campeonato")
        janela.geometry("690x514")
        centralizeWindow(janela)

        #para os botes sobrepor a imagem:
        imgPillow = Image.open('img.gif')
        img = ImageTk.PhotoImage(imgPillow)

        canvas = tk.Canvas(janela, width=img.width(), height=img.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        pesquisarPlayer = tk.Button(janela, text="Pesquisar", command=op.pesquisarPlayer)
        addPlayer = tk.Button(janela, text="Adicionar", command=op.adicionarPlayer)
        pesquisarTime = tk.Button(janela, text="Pesquisar", command=op.pesquisarTime)
        addTime = tk.Button(janela, text="Adicionar", command=op.adicionarTime)

       

        janela.mainloop()
        

#Instancia um objeto da classe Atleta
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