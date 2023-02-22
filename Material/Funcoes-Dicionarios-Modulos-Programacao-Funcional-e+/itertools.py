l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]

# print(zipper(l1, l2))

# usando o zip do python que faz a mesma coisa 

# print(list(zip(l1,l2)))

# ou zipar usando o valor da lista maior

from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue='Sem nome')))