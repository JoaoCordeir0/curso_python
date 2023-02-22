lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

# Minha solução
# index = 0
# lista_soma = list()
# for item in lista_b:
#     lista_soma.append(item + lista_a[index])
#     index += 1

# print(lista_soma)


# Solução do curso
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)


    