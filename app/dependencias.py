from app.banco_de_dados.local_db import BancoDeDadosLocal
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio

from typing import Annotated
from fastapi import Depends


banco_de_dados = BancoDeDadosLocal()
banco_de_dados.inicializar_banco()

def obter_banco_de_dados () -> BancoDeDadosLocal:
    return banco_de_dados

def obter_cliente_repositorio(banco_de_dados_local: Annotated[BancoDeDadosLocal, 
                                                              Depends(obter_banco_de_dados)],

    ) -> ClienteRepositorio:
    return ClienteRepositorio(banco_de_dados_local)
