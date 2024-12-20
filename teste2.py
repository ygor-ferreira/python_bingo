import random

jogos = {}
escolha = int(input("Quantos jogadores? "))

for n in range(0, escolha):
    matriz = [[], [], [], [], []]
    valores_existentes = set()

    jogos["jogador"] = str(input(f"Nome do jogador {n+1}: ")).title()

    for l in range(0, 5):
        for c in range(0, 5):
            while True:
                num = random.randint(0, 60)
                if num not in valores_existentes:
                    valores_existentes.add(num)
                    matriz[l].append(num)
                    break

    # Substituir o valor central por "x"
    matriz[2][2] = "x"

    # Adicionar a matriz ao dicionário do jogador
    jogos[jogos["jogador"]] = matriz

# Imprimir as matrizes para verificação
for jogador, matriz in jogos.items():
    if jogador != "jogador":  # Ignorar a chave temporária "jogador"
        print(f"\nCartela do {jogador}:")
        for linha in matriz:
            print(linha)