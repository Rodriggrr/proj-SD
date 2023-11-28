import tkinter as tk
import Classes_pb2
from PlayerProxy import *

class Options:
    proxy = Proxy()

    
    
    def pesquisarPlayer(self):
        atleta.nome      = input("Digite o nome do atleta: ")
        self.proxy.getAtleta(atleta)
    
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
