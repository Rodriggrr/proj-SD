import tkinter as tk
import Classes_pb2
from PlayerProxy import *
from PIL import Image, ImageTk

class Interface:
    proxy = Proxy()

    def centralizeWindow(self, janela):
        janela.update_idletasks()
        width = janela.winfo_width()
        height = janela.winfo_height()
        x = (janela.winfo_screenwidth() // 2) - (width // 2)
        y = (janela.winfo_screenheight() // 2) - (height // 2)
        janela.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def Janela(self):
      
        janela = tk.Tk()
        janela.title("Campeonato")
        janela.geometry("690x514")
        self.centralizeWindow(janela)

        imgPillow = Image.open('img.gif')
        img = ImageTk.PhotoImage(imgPillow)
        canvas = tk.Canvas(janela, width=img.width(), height=img.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        pesquisarPlayer = tk.Button(janela, text="Pesquisar", command=self.pesquisarPlayer)
        addPlayer = tk.Button(janela, text="Adicionar", command=self.adicionarPlayer)
        pesquisarTime = tk.Button(janela, text="Pesquisar", command=self.pesquisarTime)
        addTime = tk.Button(janela, text="Adicionar", command=self.adicionarTime)

        # Place the buttons on top of the image
        pesquisarPlayer.place(x=170, y=100)
        addPlayer.place(x=400, y=100)
        pesquisarTime.place(x=172, y=240)
        addTime.place(x=400, y=240)

        janela.mainloop()
      
    def pesquisarPlayer(self):
 
        window = tk.Toplevel()
        window.title("Pesquisar Jogador")
        window.geometry("690x514")
        self.centralizeWindow(window)

        imgPillow = Image.open('img.gif')
        img = ImageTk.PhotoImage(imgPillow)
        canvas = tk.Canvas(window, width=img.width(), height=img.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        nome = tk.Entry(window)
        nome.place(x=190, y=100)
        atleta.nome = nome.get()
        button = tk.Button(window, text="Pesquisar", command=lambda: self.proxy.getAtleta(atleta))
        button.place(x=190, y=200)
    
    def adicionarPlayer(self):
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

    def pesquisarTime(self):
        time.nome = input("Digite o nome do time: ")
        self.proxy.getTime(time)

    def adicionarTime(self):
        time.nome = input("Digite o nome do time: ")
        time.tecnico = input("Digite o nome do técnico: ")
        time.pontos = int(input("Digite a pontuação do time: "))
        time.qtdJogos = int(input("Digite a quantidade de jogos do time: "))

        self.proxy.addTime(time)
    

atleta = Classes_pb2.Atleta()
time = Classes_pb2.Time()








#         print("""
# 1 - Listar Jogadores
# 2 - Adicionar Jogador
# 3 - Listar Times
# 4 - Adicionar Time
# """)