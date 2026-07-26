from app.banco_de_dados.local_db import BancoDeDadosLocal
from app.modelos.clientes import Cliente

### criando o repositorio para receber o DB 
class ClienteRepositorio:
    def __init__(self, database: BancoDeDadosLocal):
        self.db = database

    async def listar_clientes(self) ->  list(Cliente):
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("Select id, nome, email, telefone FROM clientes")
            linhas = cursor.fetchall()
            clientes = [
                Cliente(id_=linha[0], nome=linha[1], email=linha[2], telefone=[3])
                    for linha in linhas
            ]
            return clientes