def generator(n=0, max=10):
    # yield 1 # Pausar
    # print('Continuando...')
    # yield 2
    # print("Mais uma vez...")
    # yield 3 # Pausar
    # print('Vou terminar')
    # return 'Acabou'

    while True:
        yield n

        n += 1

        if n > max:
            return        

# from com generator
def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen):
    yield from gen
    yield 4 
    yield 5
    yield 6

gen = generator(max=5)
for n in gen:
    print(n)

g = gen2(gen1())
for n in g:
    print(n)


