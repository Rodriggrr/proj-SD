import tkinter as tk
import Classes_pb2
from PlayerProxy import *
from PIL import Image, ImageTk
from google.protobuf.json_format import MessageToDict

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

        # imgPillow = Image.open('img.gif')
        # img = ImageTk.PhotoImage(imgPillow)
        # canvas = tk.Canvas(janela, width=img.width(), height=img.height())
        # canvas.pack()
        # canvas.create_image(0, 0, anchor=tk.NW, image=img)

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

        # self.imgPillow = Image.open('img.gif')
        # self.img = ImageTk.PhotoImage(self.imgPillow)
        # canvas = tk.Canvas(window, width=self.img.width(), height=self.img.height())
        # canvas.pack()
        # canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
   
        nome = tk.Entry(window)
        nome.place(x=190, y=100)
        
        atleta = Classes_pb2.Atleta()

        def doOp(self):
            def changeName(nome, atleta):
                atleta.nome = nome
                return atleta
            resultado = self.proxy.getAtleta(changeName(nome.get(), atleta))
            label.config(text=resultado)

        button = tk.Button(window, text="Pesquisar", command=lambda: doOp(self))
        button.place(x=230, y=150)
        label = tk.Label(window, text="")
        label.place(x=210, y=200)
            
    def adicionarPlayer(self):
        
        window = tk.Toplevel()
        window.title("Adicionar Jogador")
        window.geometry("690x514")
        self.centralizeWindow(window)

        # self.imgPillow = Image.open('img.gif')
        # self.img = ImageTk.PhotoImage(self.imgPillow)
        # canvas = tk.Canvas(window, width=self.img.width(), height=self.img.height())
        # canvas.pack()
        # canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

        labelNome = tk.Label(window, text="Nome:")
        labelNome.place(x=100, y=100)
        nome = tk.Entry(window)
        nome.place(x=190, y=100)
        labelNome = tk.Label(window, text="Idade:")
        labelNome.place(x=100, y=130)
        idade = tk.Entry(window)
        idade.place(x=190, y=130)
        labelNome = tk.Label(window, text="""Posição: 1 - Goleiro
2 - Zagueiro
3 - Lateral
4 - Meio Campo
5 - Atacante""")
        labelNome.place(x=100, y=160)
        posicao = tk.Entry(window)
        posicao.place(x=190, y=160)
        labelNumCamisa = tk.Label(window, text="Número da Camisa:")
        labelNumCamisa.place(x=100, y=190)
        numCamisa = tk.Entry(window)
        numCamisa.place(x=190, y=190)
        labelTime = tk.Label(window, text="Time:")
        labelTime.place(x=100, y=220)
        time = tk.Entry(window)
        time.place(x=190, y=220)

        atleta = Classes_pb2.Atleta()

        def doOp(self):
            def changeAtleta(nome, idade, posicao, numCamisa, time, atleta):
                atleta.nome = nome
                atleta.idade = int(idade)
                if posicao == 1:
                    atleta.posicao = Classes_pb2.Atleta.GOLEIRO
                elif posicao == 2:
                    atleta.posicao = Classes_pb2.Atleta.ZAGUEIRO
                elif posicao == 3:
                    atleta.posicao = Classes_pb2.Atleta.LATERAL
                elif posicao == 4:
                    atleta.posicao = Classes_pb2.Atleta.MEIOCAMPO
                elif posicao == 5:
                    atleta.posicao = Classes_pb2.Atleta.ATACANTE
                atleta.numCamisa = int(numCamisa)
                atleta.time = time
                return atleta
            resultado = self.proxy.addAtleta(changeAtleta(nome.get(), idade.get(), posicao.get(), numCamisa.get(), time.get(), atleta))
            label.config(text=resultado)
        
        button = tk.Button(window, text="Adicionar", command=lambda: doOp(self))
        button.place(x=230, y=250)
        label = tk.Label(window, text="")
        label.place(x=210, y=300)

    def pesquisarTime(self):
            
            window = tk.Toplevel()
            window.title("Pesquisar Time")
            window.geometry("690x514")
            self.centralizeWindow(window)
    
            # self.imgPillow = Image.open('img.gif')
            # self.img = ImageTk.PhotoImage(self.imgPillow)
            # canvas = tk.Canvas(window, width=self.img.width(), height=self.img.height())
            # canvas.pack()
            # canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
    
            nome = tk.Entry(window)
            nome.place(x=190, y=100)
            
            time = Classes_pb2.Time()
            
            texto = tk.Text(window, height=5, width=5)
            texto.pack()
    
            def doOp(self):
                def changeName(nome, time):
                    time.nome = nome
                    return time
                resultado = self.proxy.getTime(changeName(nome.get(), time))
                print(resultado)
                resu = str(resultado)
                texto.insert(tk.END, resu)

            button = tk.Button(window, text="Pesquisar", command=lambda: doOp(self))
            button.place(x=230, y=150)
            label = tk.Label(window, text="")
            label.place(x=210, y=200)

    def adicionarTime(self):
        time.nome = input("Digite o nome do time: ")
        time.tecnico = input("Digite o nome do técnico: ")
        time.pontos = int(input("Digite a pontuação do time: "))
        time.qtdJogos = int(input("Digite a quantidade de jogos do time: "))

        self.proxy.addTime(time)
    

atleta = Classes_pb2.Atleta()
time = Classes_pb2.Time()
