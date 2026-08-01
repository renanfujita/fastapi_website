# reset_db.py
from app.banco_de_dados.local_db import BancoDeDadosLocal

db = BancoDeDadosLocal()

with db.conectar() as conexao:
    cursor = conexao.cursor()
    cursor.execute("DROP TABLE IF EXISTS clientes")
    conexao.commit()

print("Tabela 'clientes' removida com sucesso!")