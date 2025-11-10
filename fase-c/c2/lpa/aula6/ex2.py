import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global v1, v2, empate

    if jogador1 == 1:  # Pedra
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2:
            v2 += 1
        elif jogador2 == 3:
            v1 += 1

    elif jogador1 == 2:  # Papel
        if jogador2 == 1:
            v1 += 1
        elif jogador2 == 2:
            empate += 1
        elif jogador2 == 3:
            v2 += 1

    elif jogador1 == 3:  # Tesoura
        if jogador2 == 1:
            v2 += 1
        elif jogador2 == 2:
            v1 += 1
        elif jogador2 == 3:
            empate += 1

    return [v1, v2, empate]

print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - Sair')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if j1 == 0:
        break

    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

for jogada in jogadas:
    print(jogada[0], jogada[1])

print(f'Número de vitórias do jogador 1: {resultados[0]}')
print(f'Número de vitórias do jogador 2: {resultados[1]}')
print(f'Número de empates: {resultados[2]}')
