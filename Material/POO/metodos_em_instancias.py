class Carro:
    def __init__(self, marca, cor, modelo):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo

    def tunar(self):
        print('Colocar escapamento esportivo no', self.modelo)

vectra = Carro(marca='Chevrolet', cor='Prata', modelo='Vectra - GTX')

print(vectra.marca)
vectra.tunar()
        