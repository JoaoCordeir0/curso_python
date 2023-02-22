a = 18
b = 0

try:    
    c = a/b    
    print(c)

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)

except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Msg: ', error)
    print('Nome: ', error.__class__.__name__)

except Exception:
    print('Erro desconhecido')

# Sempre será executado mesmo dando erro
finally: 
    print('FIM')
    