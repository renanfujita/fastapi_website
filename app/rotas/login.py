from fastapi import APIRouter, Form, Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.banco_de_dados.usuario_repositorio import UsuarioRepositorio
from app.dependencias import obter_usuario_repositorio
from typing import Annotated

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/login"
)

@router.get("/", response_class=HTMLResponse)
async def pagina_login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )

@router.post("/")
async def login(
        usuario_repositorio: Annotated[UsuarioRepositorio, Depends(obter_usuario_repositorio)],
        request: Request, 
        email: str = Form(...), 
        senha: str = Form(...),
):
    usuario = await usuario_repositorio.buscar_usuario_por_email_senha(email, senha)
        # 1. Se acertar o login, redireciona:
    if usuario:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="session_token", value="token-senha", httponly=True)
        return response

    # 2. Se errar o login (fora do if), renderiza o erro:
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "email": email,
            "senha": senha,
            "error": "Credenciais inválidas"
        }
    )

@router.get("/logout")
async def logout():
    # 1. Cria o redirecionamento para a tela de login
    response = RedirectResponse(url="/login", status_code=303)
    
    # 2. Remove o cookie de autenticação do navegador
    response.delete_cookie(key="session_token", path="/")
    
    return response