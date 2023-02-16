frase = 'Meu nome é João Victor Cordeiro'
palavras = frase.split()

for i, frase in enumerate(palavras):
    # Remove espaços da direita e esquerda
    print(palavras[i].strip())
