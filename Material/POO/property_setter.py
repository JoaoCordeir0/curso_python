class Caneta:
    def __init__(self, cor) -> None:    
        # Atributos que começar com um _ não devem ser utilizados fora da classe
        self._cor = cor
    

    # Property -> Faz um método virar um atributo
    @property
    def cor(self):
        # Esse é o getter
        return self._cor
       
    @cor.setter
    def cor(self, valor):
        # Esse é o setter
        self._cor = valor


caneta = Caneta('Azul')    

print(caneta.cor)

caneta.cor = 'Rosa'

print(caneta.cor)