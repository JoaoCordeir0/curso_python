def create_multi(mult):
    def multi(num):
        return num * mult
    return multi

duplicar = create_multi(2)
triplica = create_multi(3)
quadriplica = create_multi(4)

print(duplicar(2))
print(triplica(6))
print(quadriplica(4))