import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()

# Executa pausadamente, ou seja, não armazana tudo na memoria e sim cria 1 a 1
generator = (
    n 
    for n in range(10000)
)

print(sys.getsizeof(generator))

for n in generator:
    print(n)