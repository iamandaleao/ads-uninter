cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO.')
        continue

    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = input('Qual o ano de nascimento?')
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)
# Cálculo das idades
from datetime import datetime
ano_atual = datetime.now().year

idades = []
for ano in cadastro['ano']:
    idades.append(ano_atual - int(ano))

# Total de cadastros
total = len(cadastro['nome'])
print(f'\nTotal de cadastros efetuados: {total}')

# Média das idades
media_idade = sum(idades) / len(idades) if idades else 0
print(f'Média das idades: {media_idade:.1f}')

# Lista de mulheres com menos de 30 anos
mulheres_menos_30 = []
for i in range(total):
    if cadastro['sexo'][i] == 'F' and idades[i] < 30:
        mulheres_menos_30.append(cadastro['nome'][i])

print(f'Mulheres com menos de 30 anos: {mulheres_menos_30}')

# Lista de homens acima da média
homens_acima_media = []
for i in range(total):
    if cadastro['sexo'][i] == 'M' and idades[i] > media_idade:
        homens_acima_media.append(cadastro['nome'][i])

print(f'Homens com idade acima da média: {homens_acima_media}')
