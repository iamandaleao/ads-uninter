x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))

cont: int = 1
multi = 0

while cont <= x:
	multi = multi + y
	cont = cont + 1

print(f'Resultado da multiplicação: {x} x {y} = {multi}')
