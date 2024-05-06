lista = [1, 30, 5, 8, 12]

# .pop - Apaga o ultimo indice ou o indice passado por parametro
# .insert - adiciona valor em indices = (indice, valor)
# .append - adiciona no final 
# del - apaga valor do indice passado

# Pegar indices de uma lista
indices = range(len(lista))
for c in indices:
    print(c)

# Tuples
valor1, valor2, *_ = lista
print(valor1)

# Enumerate
for indice, item in enumerate(lista):
    print(indice, item)