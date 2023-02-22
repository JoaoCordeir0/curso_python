import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# print(list(range(10)))

lista = []
for num in range(10):
    lista.append(num)

# print(lista)

# Lista comprehension ->
lista = [
    num * 2
    for num in range(10)
]

# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 30},
]


##
## O que vem antes do FOR é mapeamento, depois do FOR é filtro
## 
novos_produtos = [
    # Mapeamento: Gera um novo dicionário e altera o valor 
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}

    for produto in produtos

    # Filtro: Filtra preco maior que 10
    if produto['preco'] >= 20 and produto['preco'] * 1.05 > 10
]

#print(*novos_produtos, sep='\n')
# Utiliza pprint
p(novos_produtos) 

