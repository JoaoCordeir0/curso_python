import os
import math

os.system('cls')

print('a' * 80)

caminho = os.path.join('desktop', 'curso', 'file.txt')
print(caminho)

diretorio, arquivo = os.path.split(caminho)

print(diretorio)
print(arquivo)

print(os.path.exists(caminho))

print(os.path.abspath('.'))

print(os.listdir())

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

print(formata_tamanho(os.path.getsize('./m_os.py')))
