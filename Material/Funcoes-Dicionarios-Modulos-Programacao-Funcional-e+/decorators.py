def criar_funcao(func):
    def interna(*args, **kwargs):

        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs)        
        return resultado
    
    return interna

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')

def inverte_string(string):
    return string[::-1]

# print(inverte_string('João Victor Cordeiro'))
string_invertida = criar_funcao(inverte_string)

invertida = string_invertida('João Victor Cordeiro')
# invertida = string_invertida(123)

print(invertida)
