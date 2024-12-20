from random import randint
from pacote import *

"""menujogos(["MOSTRAR JOGOS", "SORTEIA UM NUMERO", "HISTORICO DE NUMEROS", "SAIR"])

t = leianum("Digite um numero: ")

print (f"O T é {t}")"""



geral = []

jogos = {}
sorteio = []


escolha = leianum("Quantos jogos deseja fazer? ")
for n in range(0,escolha):
    matriz = [[],[],[],[],[]]
    valores_existentes = set()
    
    jogos["jogador"] = str(input(f"Nome do jogador {n+1}: ")).title()
    for l in range(0,5):
        for c in range(0,5):
            while True:
                num = randint(0,60)
                if num not in valores_existentes:
                    valores_existentes.add(num)
                    matriz[l].append(num)
                    break
                
    #funcao para substituis os valores
    matriz[2][2] = "x"
    
    jogos["jogo"] = matriz[:]
    geral.append(jogos.copy())
    matriz.clear()
    jogos.clear()
    
mostrarjogo(geral)
form = int(input("escolha: "))
print (geral[0]["jogo"][2][3])
if geral[0]["jogo"][2][3] == form:
    geral[0]["jogo"][2][3] = "x"
print (geral)
    
"""while True:
    for n in range(0,len(geral)):
        jogadores(geral[n]["jogador"])
        for l in range(0,5):
            for c in range(0,5):
                print (f"| {geral[n]["jogo"][l][c]:<3}|", end=" ")
            print ()
        print()
    num = int(input("escolha um numero"))
    for n in range(0,len(geral)):
        for l in range(0,5):
            for c in range(0,5):
                if geral[n]["jogo"][n][c] == sorteio:
                    print ("funciona")
    escolha = str(input("continuar? "))
    if escolha == "n":
        break"""



