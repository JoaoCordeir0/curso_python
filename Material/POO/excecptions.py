class MeuErro(Exception):
    ...

def levantar():
    exception_ = MeuErro('A msg do meu erro', 'a', 'z')
    exception_.add_note('Vc errou isso: blabla')
    raise exception_

try:
    levantar()
except (MeuErro, ZeroDivisionError) as err:
    print(f'({err.__class__.__name__}) - {err.args} - {err.__notes__}')
    