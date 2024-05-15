import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cria tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name TEXT,'
        'weight REAL'
    ')'
)
connection.commit()

# Deleta qualquer valor
cursor.execute(f'DELETE FROM {TABLE_NAME}')
connection.commit()

# Insere valores
sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'
cursor.execute(sql, ['Cordeiro', 20])
cursor.executemany(sql, [['João', 10], ['Victor', 20], ['Myn', 30]])

connection.commit()

cursor.close()
connection.close()