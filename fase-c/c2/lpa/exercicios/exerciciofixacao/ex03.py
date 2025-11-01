# PARTE 1: ENTRADA DE DADOS
# Pede para o usuário digitar dois números e guarda nas variáveis
inicial = int(input('Digite um valor inicial:'))  # int() converte o texto digitado em número inteiro
final = int(input('Digite um valor final:'))

# PARTE 2: CRIANDO AS VARIÁVEIS CONTADORAS E ACUMULADORAS
# Essas variáveis vão guardar informações enquanto o programa roda
qtd_positivo = 0  # Vai contar quantos números positivos (maiores que 0) existem
qtd_par = 0  # Vai contar quantos números pares existem
qtd_impar = 0  # Vai contar quantos números ímpares existem
soma_positivo = 0  # Vai somar todos os números positivos
soma_par = 0  # Vai somar todos os números pares
soma_impar = 0  # Vai somar todos os números ímpares

# PARTE 3: PREPARANDO O LOOP
i = inicial  # 'i' é a variável que vai percorrer os números do inicial até o final

# PARTE 4: VERIFICANDO SE O INICIAL É MENOR QUE O FINAL
if (inicial < final):  # Se o inicial for menor que o final, o programa continua

	# PARTE 5: LOOP - VAI REPETIR ATÉ CHEGAR NO VALOR FINAL
	while (i <= final):  # Enquanto 'i' for menor ou igual ao final, continua repetindo

		# Verifica se o número é POSITIVO (maior que 0)
		if (i > 0):
			qtd_positivo = qtd_positivo + 1  # Aumenta o contador de positivos em 1
			soma_positivo = soma_positivo + i  # Adiciona o número na soma de positivos

		# Verifica se o número é PAR (resto da divisão por 2 é zero)
		if (i % 2 == 0):  # O símbolo % é o resto da divisão
			qtd_par = qtd_par + 1  # Aumenta o contador de pares
			soma_par = soma_par + i  # Adiciona o número na soma de pares

		# Se NÃO for par, então é ÍMPAR
		else:
			qtd_impar = qtd_impar + 1  # Aumenta o contador de ímpares
			soma_impar = soma_impar + i  # Adiciona o número na soma de ímpares

		i = i + 1  # Aumenta o 'i' em 1 para passar pro próximo número

	# PARTE 6: CALCULANDO AS MÉDIAS
	# Média = soma total dividido pela quantidade
	media_positivo = soma_positivo / qtd_positivo
	media_par = soma_par / qtd_par
	media_impar = soma_impar / qtd_impar

	# PARTE 7: MOSTRANDO OS RESULTADOS NA TELA
	print(f'Quantidade de valores positivos: {qtd_positivo}')
	print(f'Média de valores positivos: {media_positivo}')
	print(f'Quantidade de valores pares: {qtd_par}')
	print(f'Média de valores pares: {media_par}')
	print(f'Quantidade de valores ímpares: {qtd_impar}')
	print(f'Média de valores ímpares: {media_impar}')

# PARTE 8: SE O INICIAL NÃO FOR MENOR QUE O FINAL
else:
	print('Você digitou um valor inicial maior ou igual ao final.')
	print('Encerrando o programa...')