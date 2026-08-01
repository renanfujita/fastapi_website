from fastapi import APIRouter, Depends, HTTPException
from app import modelos
from app.modelos.clientes import Cliente, ClienteCriarAtualizar
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


@router.post("/", response_model=Cliente, status_code=201)
async def criar_cliente(
        cliente_repositorio: Annotated[ClienteRepositorio, Depends (obter_cliente_repositorio)],
        cliente: ClienteCriarAtualizar

):
        return await cliente_repositorio.criar_cliente(cliente)

@router.put("/{cliente_id}", response_model=Cliente | None)
async def atualizar_cliente(
        cliente_repositorio: Annotated[ClienteRepositorio, Depends (obter_cliente_repositorio)],
        cliente_id: int,
        cliente: ClienteCriarAtualizar
):
        cliente_atualizado = await cliente_repositorio.atualizar_cliente(cliente_id, cliente)
        if not cliente_atualizado:
                raise HTTPException(status_code=404, detail="Cliente não encontrado!")

        return cliente_atualizado

@router.delete("/{cliente_id}", status_code=204)
async def deletar_cliente(
        cliente_repositorio: Annotated[ClienteRepositorio, Depends (obter_cliente_repositorio)],
        cliente_id: int
):

        sucesso = await cliente_repositorio.deletar_cliente(cliente_id)
        if not sucesso:
                raise HTTPException(status_code=404, detail="Cliente não encontrado!")