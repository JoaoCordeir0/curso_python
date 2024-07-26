# https://docs.python.org/3/library/typing.html

from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Luiz Otávio'

# Sequências
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Luiz')

# Dicionários e conjuntos

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias

pessoa: Dict[str, Union[str, int]] = {
    'nome': 'João', 
    'sobrenome': 'Cordeiro', 
    'idade': 20
}
pessoa2: MeuDict = {
    'nome': 'João',
    'sobrenome': 'Cordeiro', 
    'idade': 20, 
    'l': [1, 2]
}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(325456789)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x: int, y: int) -> int:
    return x + y

print(retorna_funcao(soma)(10, 20))