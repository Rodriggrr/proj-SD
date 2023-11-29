audio = True
import tkinter as tk
import threading
import Classes_pb2
from PlayerProxy import *
from PIL import Image, ImageTk
from google.protobuf.json_format import MessageToJson


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

        imgPillow = Image.open('util/janela.gif')
        img = ImageTk.PhotoImage(imgPillow)
        canvas = tk.Canvas(janela, width=img.width(), height=img.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        pesquisarPlayer = tk.Button(janela, text="Pesquisar Jogador", command=self.pesquisarPlayer)
        addPlayer = tk.Button(janela, text="Adicionar Jogador", command=self.adicionarPlayer)
        pesquisarTime = tk.Button(janela, text="Pesquisar Time", command=self.pesquisarTime)
        addTime = tk.Button(janela, text="Adicionar Time", command=self.adicionarTime)
        pesquisarTecnico = tk.Button(janela, text="Pesquisar Técnico", command=self.pesquisarTecnico)
        mute = tk.Button(janela, text="Mute", command=self.mute)

        # Place the buttons on top of the image
        pesquisarPlayer.place(x=170, y=100)
        addPlayer.place(x=400, y=100)
        pesquisarTime.place(x=172, y=240)
        addTime.place(x=400, y=240)
        pesquisarTecnico.place(x=170, y=380)
        mute.place(x=400, y=380)

        janela.mainloop()
      
    def pesquisarPlayer(self):
 
        window = tk.Toplevel()
        window.title("Pesquisar Jogador")
        window.geometry("690x514")
        self.centralizeWindow(window)

        self.imgPillow = Image.open('util/pesqPlayer.gif')
        self.img = ImageTk.PhotoImage(self.imgPillow)
        canvas = tk.Canvas(window, width=self.img.width(), height=self.img.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
   
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

        self.imgPillow = Image.open('util/addPlayer.gif')
        self.img = ImageTk.PhotoImage(self.imgPillow)
        canvas = tk.Canvas(window, width=self.img.width(), height=self.img.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

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
            if resultado is True:
                label.configure(text="Adicionado com sucesso!")
        
        button = tk.Button(window, text="Adicionar", command=lambda: doOp(self))
        button.place(x=230, y=250)
        label = tk.Label(window, text="")
        label.place(x=210, y=300)

    def pesquisarTime(self):
            
            window = tk.Toplevel()
            window.title("Pesquisar Time")
            window.geometry("690x514")
            self.centralizeWindow(window)
    
            self.imgPillow = Image.open('util/pesqTime.gif')
            self.img = ImageTk.PhotoImage(self.imgPillow)
            canvas = tk.Canvas(window, width=self.img.width(), height=self.img.height())
            canvas.pack()
            canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
    
            nome = tk.Entry(window)
            nome.place(x=190, y=100)
            
            time = Classes_pb2.Time()
    
            def doOp(self):
                def changeName(nome, time):
                    time.nome = nome
                    return time
                resultado = self.proxy.getTime(changeName(nome.get(), time))
                print (str(resultado))

                label.config(text=resultado)
                

            button = tk.Button(window, text="Pesquisar", command=lambda: doOp(self))
            button.place(x=230, y=150)
            label = tk.Label(window, text="")
            label.place(x=210, y=200)

    def adicionarTime(self):
        
        window = tk.Toplevel()
        window.title("Adicionar Time")
        window.geometry("690x514")
        self.centralizeWindow(window)

        self.imgPillow = Image.open('util/addTime.gif')
        self.img = ImageTk.PhotoImage(self.imgPillow)
        canvas = tk.Canvas(window, width=self.img.width(), height=self.img.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

        labelNome = tk.Label(window, text="Nome do time:")
        labelNome.place(x=100, y=100)
        nome = tk.Entry(window)
        nome.place(x=190, y=100)
        labelNomeTec = tk.Label(window, text="Nome do técnico:")
        labelNomeTec.place(x=100, y=130)
        nomeTec = tk.Entry(window)
        nomeTec.place(x=190, y=130)
        labelIdadeTec = tk.Label(window, text="Idade do técnico:")
        labelIdadeTec.place(x=100, y=160)
        idadeTec = tk.Entry(window)
        idadeTec.place(x=190, y=160)
        labelQtdTitulos = tk.Label(window, text="Quantidade de títulos:")
        labelQtdTitulos.place(x=100, y=190)
        qtdTitulos = tk.Entry(window)
        qtdTitulos.place(x=190, y=190)
        labelPontos = tk.Label(window, text="Pontos do time:")
        labelPontos.place(x=100, y=220)
        pontos = tk.Entry(window)
        pontos.place(x=190, y=220)
        labelQtdJogos = tk.Label(window, text="Quantidade de jogos:")
        labelQtdJogos.place(x=100, y=250)
        qtdJogos = tk.Entry(window)
        qtdJogos.place(x=190, y=250)

        def doOp(self):
            time = Classes_pb2.Time()
            tecnico = time.Tecnico()
            def changeTime(nome, nomeTec, idadeTec, qtdTitulos, pontos, qtdJogos, time, tecnico):
                time.nome = nome
                tecnico.nome = nomeTec
                tecnico.idade = int(idadeTec)
                tecnico.qtdTitulos = int(qtdTitulos)
                time.tecnico = tecnico.SerializeToString()
                time.pontos = int(pontos)
                time.qtdJogos = int(qtdJogos)
                return time
            resultado = self.proxy.addTime(changeTime(nome.get(), nomeTec.get(), idadeTec.get(), qtdTitulos.get(), pontos.get(), qtdJogos.get(), time, tecnico))
            label.config(text=resultado)

        button = tk.Button(window, text="Adicionar", command=lambda: doOp(self))
        button.place(x=230, y=300)

        label = tk.Label(window, text="")
        label.place(x=210, y=350)
    
    def pesquisarTecnico(self):
            
            window = tk.Toplevel()
            window.title("Pesquisar Técnico")
            window.geometry("690x514")
            self.centralizeWindow(window)
    
            self.imgPillow = Image.open('util/pesqTec.gif')
            self.img = ImageTk.PhotoImage(self.imgPillow)
            canvas = tk.Canvas(window, width=self.img.width(), height=self.img.height())
            canvas.pack()
            canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
    

            labelNome = tk.Label(window, text="Nome do time:")
            labelNome.place(x=100, y=100)
            nome = tk.Entry(window)
            nome.place(x=190, y=100)
            
            time = Classes_pb2.Time()
    
            def doOp(self):
                def changeName(nome, time):
                    time.nome = nome
                    return time
                resultado = self.proxy.getTecnico(changeName(nome.get(), time))
                label.config(text=resultado)

            button = tk.Button(window, text="Pesquisar", command=lambda: doOp(self))
            button.place(x=230, y=150)
            label = tk.Label(window, text="")
            label.place(x=210, y=200)

    def mute(self):
        global audio
        if audio is True:
            audio = False
        else:
            audio = True
            

atleta = Classes_pb2.Atleta()
time = Classes_pb2.Time()
tecnico = time.Tecnico()
