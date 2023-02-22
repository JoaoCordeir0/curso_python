a, b = 1,2 
a, b = a, b

pessoa = {
    'nome': 'João',
    'sobrenome': 'Cordeiro',
}

# (a1, a2), (b1, b2) = pessoa.items()

# print(a1, a2)
# print(b1, b2)

dados_pessoa = {
    'idade': 19,
    'altura': 1.8,
}

# Extração de dicionário
pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

def mostra_argumentos_nomeados(*args, **kwargs):
    print("Não nomeados: ", args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostra_argumentos_nomeados(nome="João", sobrenome="Cordeiro")
# mostra_argumentos_nomeados(pessoa_completa)
mostra_argumentos_nomeados(**pessoa_completa)