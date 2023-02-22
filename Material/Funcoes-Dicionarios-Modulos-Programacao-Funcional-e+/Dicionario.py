# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy
dic = {
    'nome': 'João Victor Cordeiro',
    'idade': 19,
    'sexo': 'Masculino'
}

print(len(dic))
print(dic.keys())
print(dic.values())

print(dic.items())
for key, value in dic.items():
    print(key, value)

print(dic['nome'])
print(dic.setdefault('idade', 20))

# copia superficial
dic2 = dic.copy()
# copia completa
dic2 = copy.deepcopy(dic)

print(dic.get('nome'))
print(dic.pop('sexo'))
print(dic.popitem())

dic.update(
    {
        'nome' : 'João Cordeiro'
    }
)
# OR
dic.update(nome='João Cordeiro')

