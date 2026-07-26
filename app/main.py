from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from app.rotas import clientes


app = FastAPI(
    title="RF Technology API",
    description ="CRM para RF Technology API",
    version="1.0.0",
)

app.include_router(clientes.router)

@app.get ("/")
async def health_check():
        return {"status": "ok"}

@app.get ("/front", response_class=HTMLResponse)
async def front_page():
        html_content = """
        <html>
            <head>
                <title> RF Technology API</title>
            </head>
            <body>
                <h1> RF Technology API</h1>
                <p>Sistema de Gestão de Ordens de Serviço</p>
                <p>Status: <strong>Operacional</strong></p>
            </body>
        </html>
        """
        return html_content

