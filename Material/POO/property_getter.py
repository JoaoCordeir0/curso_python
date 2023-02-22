class Caneta:
    def __init__(self, cor) -> None:
        self.cor_tinta = cor

    # Getter -> 
    # def get_cor(self):
    #     return self.cor

    # Property -> Faz um método virar um atributo
    @property
    def cor(self):
        return self.cor_tinta

caneta = Caneta('Azul')    

# print(caneta.get_cor())
print(caneta.cor)