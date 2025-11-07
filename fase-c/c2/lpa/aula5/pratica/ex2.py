# Suponha que você é um colecionador de jogos de videogame. Escreva um algoritmo que permita cadastrar esses jogos informando o nome e a qual videogame ele pertence
# Para isso, crie um menu de opções contendo: cadastrar novo item, listar tudo que foi cadastrado e sair.
# Para resolver esse exercício, crie pelo menos uma função para cada item do menu
# Além disso, armazene todos os dados em disco e manter os dados cadastrados

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write(f'{nomeJogo}; {nomeVideogame}\n')
    finally:
        a.close()


def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        conteudo = a.read()
        if conteudo.strip() == '':
            print('Nenhum jogo cadastrado.\n')
        else:
            print(conteudo)
    finally:
        a.close()


# Programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print("Arquivo localizado no computador.")
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo)

while True:
    print('Menu')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)

    if op == 1:
        print("Opção de cadastrar novo item selecionada...\n")
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print("Opção de listar selecionada...\n")
        listarArquivo(arquivo)

    elif op == 3:
        print('Encerrando o programa...')
        break
