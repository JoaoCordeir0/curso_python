string = 'Cordeiro'
metodo = 'upper'

# Serve para checar se o método existe na string
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método ', metodo)