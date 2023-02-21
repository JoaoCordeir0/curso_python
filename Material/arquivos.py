import os 

path = 'texto.txt'

# '+' adiciona opção de escrita ou leitura

##----------##
# Escrevendo #
##----------##
with open(path, 'w', encoding='utf-8') as file:
    file.write('linha 1')

##-----##
# Lendo #
##-----##
with open(path, 'r', encoding='utf8') as file:
    print(file.read())
    print(file.readline().strip) # or , end=''

##-------------------------------##
# Adicionando conteúdo no arquivo #
##-------------------------------##
with open(path, 'a', encoding='utf8') as file:
    file.write('linha 1')

##-------------------##
# Apagando um arquivo #
##-------------------##
os.remove(path)
# or
os.unlink(path)

##---------------------##
# Renomeando um arquivo #
##---------------------##
os.rename(path, 'new_texto.txt')