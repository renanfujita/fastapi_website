from fastapi import APIRouter, Depends, HTTPException
from app import modelos
from app.modelos.clientes import Cliente
from typing import Annotated
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependencias import obter_cliente_repositorio

router = APIRouter(

    prefix="/clientes"
)

CLIENT_LIST = [Cliente(id_=1, nome="Rafael", email ="rafael@htormail.com", telefone ="117217271"),
                     Cliente(id_=2, nome="Isabela", email ="bela@hotmail.com", telefone="4232233")]

  

@router.get("/", response_model=list[Cliente])
async def listar_clientes(clientes_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
        return await clientes_repositorio.listar_clientes()

   
@router.get("/{cliente_id}", response_model=Cliente | None)
async def obter_cliente(
        clientes_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
        cliente_id: int
):
        cliente = await clientes_repositorio.obter_cliente(cliente_id)

        if not cliente:
                raise HTTPException(status_code=404, detail="Cliente não encontrado!")
                  
        return cliente
