from random import randint
from pacote import *
from time import sleep

#deixar o menu um pouco mais bonito

geral = []

jogos = {}
sorteio = []


escolha = leianum("Quantos jogos deseja fazer? ")
for n in range(0,escolha):
    matriz = [[],[],[],[],[]]
    #numeros_repetidos serve como lista secundaria para poder verificar se tem algum numero repetido
    #apenas obs: a função set tira as duplicatas
    numeros_repetidos = set()
    
    jogos["jogador"] = str(input(f"Nome do jogador {n+1}: ")).title()
    for l in range(0,5):
        for c in range(0,5):
            #aqui ele verificar se vai ter algum numero repitido se nao tiver adiciona
            while True:
                num = randint(0,60)
                #desta forma
                if num not in numeros_repetidos:
                    numeros_repetidos.add(num)
                    matriz[l].append(num)
                    break

                
    #funcao para substituis os valores
    matriz[2][2] = "x"
    
    jogos["jogo"] = matriz[:]
    geral.append(jogos.copy())
    matriz.clear()
    jogos.clear()

while True:
    #funçao de verificar caso ele atenda todos requisito ira retorna false e ira da um break
    verificar = verificarbingo(geral)
    if verificar == False:
        break
    menujogos(["MOSTRAR JOGOS", "SORTEIA UM NUMERO", "HISTORICO DE NUMEROS", "SAIR"])
    escolha_menu = leianum("Escolha: ")
    if escolha_menu == 1:
        mostrarjogo(geral)
    elif escolha_menu == 2:
        print ("SORTEIO DOS NUMEROS".center(40))
        while True:
            num = randint(0,60)
            if num not in sorteio:
                sorteio.append(num)
                print("-"*40)
                print(f"Numero sorteado: {num}".center(40))
                print ("-"*40)
                #caso o numero sorteado tenha em algum jogo ira substituir o numero por um "x"
                inserirnumeros(geral,num)
                break
        
    elif escolha_menu == 3:
        print (sorteio)
    
    elif escolha_menu == 4:
        break
    else:
        print ("ERRO DIGITE UMA OPÇÃO CORRETA")
            

print ("teste")


