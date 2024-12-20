def mostrarjogo(lst):
    for n in range(0,len(lst)):
        jogadores(lst[n]["jogador"])
        for l in range(0,5):
            for c in range(0,5):
                print (f"| {lst[n]["jogo"][l][c]:<3}|", end=" ")
            print ()
        print()
        

def jogadores(nome):
    print ("-"*34)
    print (nome.center(34))
    print ("-"*34)
    

def leianum(num):
    while True:
        try:
            n = int(input(num))
            
        except (ValueError, TypeError):
            print ("ERRO! INSIRA UM NUMERO INTEIRO!!!")
        
        else:
            return n
        
        
def inserirnumeros(lst, sorteio):
    for n in range(0,len(lst)):
        for l in range(0,5):
            for c in range(0,5):
                if lst[n]["jogo"][l][c] == sorteio:
                    lst[n]["jogo"][l][c] = "x" 
                    print ("|" +  f"Jogador: {lst[n]["jogador"]} pontuou".center(38) + "|")
                    
def ganhador(lst,n):
    print (f"PARABENS {lst[n]["jogador"]} GANHOU!!!!".center(40))

def verificarbingo(lst):
    for n in range(0,len(lst)):
        if lst[n]["jogo"][0][4] == "x" and lst[n]["jogo"][1][4] == "x" and lst[n]["jogo"][2][4] == "x" and lst[n]["jogo"][3][4] == "x" and lst[n]["jogo"][4][4] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][0][3] == "x" and lst[n]["jogo"][1][3] == "x" and lst[n]["jogo"][2][3] == "x" and lst[n]["jogo"][3][3] == "x" and lst[n]["jogo"][4][3] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][0][2] == "x" and lst[n]["jogo"][1][2] == "x" and lst[n]["jogo"][2][2] == "x" and lst[n]["jogo"][3][2] == "x" and lst[n]["jogo"][4][2] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][0][1] == "x" and lst[n]["jogo"][1][1] == "x" and lst[n]["jogo"][2][1] == "x" and lst[n]["jogo"][3][1] == "x" and lst[n]["jogo"][4][1] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][0][0] == "x" and lst[n]["jogo"][1][0] == "x" and lst[n]["jogo"][2][0] == "x" and lst[n]["jogo"][3][0] == "x" and lst[n]["jogo"][4][0] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][0][0] == "x" and lst[n]["jogo"][0][1] == "x" and lst[n]["jogo"][0][2] == "x" and lst[n]["jogo"][0][3] == "x" and lst[n]["jogo"][0][4] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][1][0] == "x" and lst[n]["jogo"][1][1] == "x" and lst[n]["jogo"][1][2] == "x" and lst[n]["jogo"][1][3] == "x" and lst[n]["jogo"][1][4] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][2][0] == "x" and lst[n]["jogo"][2][1] == "x" and lst[n]["jogo"][2][2] == "x" and lst[n]["jogo"][2][3] == "x" and lst[n]["jogo"][2][4] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][3][0] == "x" and lst[n]["jogo"][3][1] == "x" and lst[n]["jogo"][3][2] == "x" and lst[n]["jogo"][3][3] == "x" and lst[n]["jogo"][3][4] == "x":
            ganhador(lst,n)
            return False
        elif lst[n]["jogo"][4][0] == "x" and lst[n]["jogo"][4][1] == "x" and lst[n]["jogo"][4][2] == "x" and lst[n]["jogo"][4][3] == "x" and lst[n]["jogo"][4][4] == "x":
            ganhador(lst,n)
            return False


    

def menujogos(lst):
    print ("-"*40)
    print (f"{"|"} {"M E N U".center(36)} {"|"}")
    print ("-"*40)
    i = 0
    for n in lst:
        i += 1
        print (f"{"|":<6}[{i}{"]":<4} {n:<25} {"|"}")
    print ("-"*40)
    
