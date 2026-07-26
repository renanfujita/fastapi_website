from fastapi import APIRouter
from app import modelos
from app.modelos.clientes import Cliente

router = APIRouter(
    prefix="/clientes"
)

CLIENT_LIST = [Cliente(id_=1, nome="Rafael", email ="rafael@htormail.com", telefone ="117217271"),
                     Cliente(id_=2, nome="Isabela", email ="bela@hotmail.com", telefone="4232233")]

  

@router.get("/", response_model=list[Cliente])
async def listar_clientes():
        return CLIENT_LIST

   


@router.get("/{cliente_id}", response_model=Cliente | None)
async def obter_cliente(cliente_id: int):
        for cliente in CLIENT_LIST:
                if cliente.id_ == cliente_id:
                        return cliente

        return None
