palavras = ('Banana', 'Abacate', 'Cereja', 'Pimentão', 'Manga')

for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais:')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')