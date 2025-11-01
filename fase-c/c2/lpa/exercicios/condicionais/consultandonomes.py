nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

if nome == 'Amanda':
    print('Olá, Amanda!')
elif idade < 18:
    print('Você não é a Amanda! E é menor de idade!')
elif idade > 100:
    print('Diferentre de você, a Amanda não é imortal')