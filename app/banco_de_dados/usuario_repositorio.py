from app.banco_de_dados.local_db import BancoDeDadosLocal
from app.modelos.usuario import Usuario, UsuarioCriarAtualizar

### criando o repositorio para receber o DB 
class UsuarioRepositorio:
    def __init__(self, database: BancoDeDadosLocal):
        self.db = database

    async def buscar_usuario_por_email_senha(self, email: str, senha: str) ->  Usuario | None:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("Select id, nome, email FROM usuarios Where email = ? AND senha = ?",  (email, senha))
            linha = cursor.fetchone()
            if linha:
                return Usuario(id_=linha[0], nome=linha[1], email=linha[2])
            return None

    async def buscar_usuario_por_email (self, email: str) ->  Usuario | None:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("Select id, nome, email FROM usuarios Where email = ?",  (email, ))
            linha = cursor.fetchone()
            if linha:
                return Usuario(id_=linha[0], nome=linha[1], email=linha[2])
            return None

    async def criar_usuario(self, nome: str, email: str, senha: str)-> Usuario:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", 
                (nome, email, senha)
            )
            usuario_id = cursor.lastrowid
            return Usuario(id_=usuario_id, nome=nome, email=email, senha=senha)
