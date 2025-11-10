# Listas

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#Conta quantas vezes tem o número 7 na lista:
print(notas.count(7))
print(notas)

#Muda o ultimo valor para 4
notas[-1] = 4
print(notas)

#Qual o maior valor da lista
print(max(notas))

#Ordena os valores em ordem crescente
notas.sort()
print(notas)

#Media dos valores da lista
print(sum(notas) / len(notas))