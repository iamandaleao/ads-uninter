# Escopo de Variáveis

def omelete():
    ovos = 12 #'variável local de omelete'
    print('Ovos = ', ovos)

def bacon():
    ovos = 6 # 'variável local de bacon'
    print('Ovos = ', ovos)
    omelete()
    print('Ovos = ', ovos)

#Programa principal
ovos = 2 # 'variável global'
bacon()
print('Ovos = ', ovos)