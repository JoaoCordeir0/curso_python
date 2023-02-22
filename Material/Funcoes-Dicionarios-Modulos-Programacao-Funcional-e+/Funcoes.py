def getNome(idade, nome, sexo=None):
    dados = f'Nome: {nome} | Idade: {idade}'
    if sexo is not None:
        return f'{dados} | Sexo: {sexo}'
    return dados

# print(getNome(nome='João Victor Cordeiro', idade=19, sexo='Maculino'))
print(getNome(nome='João Victor Cordeiro', idade=19))



# Empacotamento de argumentos
def soma(*args):
    total = 0
    for c in args:
        total += c
    return total

print(soma(1, 2, 3, 4))
