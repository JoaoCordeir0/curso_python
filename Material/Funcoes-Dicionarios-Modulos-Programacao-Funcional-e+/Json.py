import json

pessoa = {
    'nome': 'João Victor',
    'sobrenome': 'Cordeiro',
    'enderecos': [
        {'rua': 'r1', 'numero':32},
        {'rua': 'r2', 'numero':65},
    ],
    'altura': 1.77,
    'numeros_preferidos': (2,4,6,8,10),
    'dev': True,
    'nada': None,
}

with open('aulaJson.json', 'w', encoding='utf8') as file:
    json.dump(
        pessoa,  
        file,
        ensure_ascii=False, # Corrigi caracteres
        indent=2
    )

# Lendo o arquivo json e transformando em dicionário
with open('aulaJson.json', 'r', encoding='utf8') as file:
    pessoa = json.load(file)
    print(pessoa)
    print(pessoa['nome'])


