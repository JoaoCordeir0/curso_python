import os

secret_key = 'Cavalo'
right_letters = ''
tentativas = 0

while True:        
    char = input("Digite um caracter _> ")
    tentativas += 1

    if len(char) > 1:
        print('Digite apenas um caracter')
        continue
    
    if char in secret_key:
        right_letters += char
    else:       
        print('Caracter não existe na palavra secreta')
        continue

    key = ''

    for c in secret_key:
        if c in right_letters:
            key += c
        else:
            key += '*'
    print(key)

    if key == secret_key:
        os.system('cls')
        print('Você ganhou!! Parabéns!')
        print(f'A palavra era: {secret_key}')
        print(f'Total de tentativas: {tentativas}')
        break
    