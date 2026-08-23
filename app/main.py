from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.rotas import clientes, login, registro
from fastapi.requests import Request
from app.rotas.clientes import front_router
from app.autenticacao_middleware import AuthenticationToken

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="RF Technology API",
    description ="CRM para RF Technology API",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(AuthenticationToken)

app.include_router(clientes.router)
app.include_router(clientes.front_router)

app.include_router(login.router)
app.include_router(registro.router)


@app.get ("/health")
async def health_check():
        return {"status": "ok"}

@app.get("/")
async def front_page(request: Request): # 1. Recebe a instância 'request' aqui
    return templates.TemplateResponse(
        request=request,                                       # 2. Passa a instância
        name="index.html",                                     # 3. Nome do arquivo
        context={"título": "RF Technology CRM", "versao": "1.0.0"} # 4. Dicionário de dados
    )

