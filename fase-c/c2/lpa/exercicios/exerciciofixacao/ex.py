# PARTE 1: CRIANDO AS VARIÁVEIS INICIAIS
soma = 0  # Variável que vai guardar a soma de todas as notas
cont = 1  # Contador que começa em 1 (primeira nota)

# PARTE 2: LOOP QUE REPETE 5 VEZES
while (cont <= 5):  # Enquanto o contador for menor ou igual a 5, continua repetindo

    # Pede para o usuário digitar uma nota
    # f'Digite a {cont}ª nota:' mostra qual nota está pedindo (1ª, 2ª, 3ª...)
    x = float(input(f'Digite a {cont}ª nota:'))  # float() converte em número decimal

    # Adiciona a nota digitada na soma total
    soma = soma + x  # Pega a soma anterior e adiciona a nova nota

    # Aumenta o contador em 1 para passar para a próxima nota
    cont = cont + 1  # 1 vira 2, 2 vira 3, 3 vira 4...

# PARTE 3: MOSTRA O RESULTADO
print(f'Somatório: {soma}')  # Mostra a soma de todas as 5 notas
