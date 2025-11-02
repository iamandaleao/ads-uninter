# Inicializa as variáveis
soma = 0  # Acumula a soma dos números positivos
qtd_num = 0  # Conta quantos números positivos foram digitados
x = 0  # Armazena o valor digitado pelo usuário

# Loop infinito - só para quando digitar 0
while True:
    # Solicita um número inteiro ao usuário
    x = int(input('Digite um valor inteiro: '))

    # Se o número for negativo, ignora e pede outro
    if x < 0:
        continue  # Volta pro início do loop sem somar

    # Se o número for zero, encerra o loop
    if not x:
        break  # Sai do loop e vai calcular a média

    # Adiciona o número positivo na soma
    soma += x
    # Incrementa o contador de números válidos
    qtd_num += 1

# Calcula a média dos números positivos digitados
media = soma / qtd_num
# Exibe o resultado
print(f'A média dos valores digitados é: {media}')