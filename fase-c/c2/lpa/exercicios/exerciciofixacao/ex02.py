# PARTE 1: ENTRADA DE DADOS
# Pede dois números pro usuário
x = int(input('Digite um valor: '))  # Primeiro número
y = int(input('Digite outro valor: '))  # Segundo número

# PARTE 2: CRIANDO AS VARIÁVEIS DO LOOP
cont: int = 1  # Contador que começa em 1 (vai contar quantas vezes somamos)
multi = 0  # Variável que vai guardar o resultado da "multiplicação"

# PARTE 3: LOOP QUE REPETE X VEZES
while cont <= x:  # Enquanto o contador for menor ou igual a x, continua repetindo

    # Soma o valor de y na variável multi
    multi = multi + y  # Adiciona y mais uma vez

    # Aumenta o contador
    cont = cont + 1  # Passa pra próxima repetição

# PARTE 4: MOSTRA O RESULTADO
print(f'Resultado da multiplicação: {x} x {y} = {multi}')