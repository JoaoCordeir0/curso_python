produto = {
    'nome': 'Caneta azul',
    'preco': 3.5,
    'categoria': 'Escritório',
}

dc = {
    # Mapeamento
    chave: valor.upper()
    if isinstance(valor, (str)) else valor
    
    for chave, valor in produto.items()

    # Filtro
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

# print(dict(lista))

s1 = {i for i in range(10)}
# print(s1)
# print(set(range(10)))