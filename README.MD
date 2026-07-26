# RF Technology API - CRM Backend

> 🟡 **Status do Projeto:** Em Desenvolvimento Inicial (v0.1.0 / MVP em Memória)

API RESTful para gestão de clientes e Ordens de Serviço da **RF Technology**, desenvolvida em Python utilizando o framework **FastAPI**.

Atualmente, o projeto encontra-se na fase de estruturação da arquitetura base e disponibilização das primeiras rotas com dados simulados em memória.

---

## 📂 Arquitetura da Aplicação

A estrutura do projeto adota uma divisão modular simples de responsabilidades:

```text
app/
├── modelos/        # Schemas de dados e validações Pydantic
│   └── clientes.py
├── rotas/          # Endpoints REST segregados por recurso (APIRouter)
│   └── clientes.py
└── main.py         # Ponto de entrada, middlewares e inicialização do FastAPI


🛠️ **Tecnologias Utilizadas**

Python 3.11+

FastAPI (Framework Web REST)

Pydantic (Validação e Serialização de Dados)

Uvicorn (Servidor ASGI)

**Endpoints Atuais:**

GET/Health Check: Verificação do status do servidor
GET/front: Landing page simples de status técnico
GET/clientes: Retorna a listagem de clientes cadastrados 
GET/clientes/{cliente_id}: Retorna o detalhe de um cliente por ID

**Execução da Aplicação**

Com as dependências instaladas, inicie o servidor com:

Bash
uvicorn app.main:app --reload
Acesse a documentação interativa em:

Swagger UI: http://127.0.0.1:8000/docs

**Próximos passos:**

1 - Implementar cadastro (POST), atualização (PUT) e remoção (DELETE) de clientes.
2 - Conectar a aplicação a um banco de dados relacional.
3 - Implementar persistência de dados com ORM (SQLAlchemy).
4 - Adicionar tratamento global de exceções e respostas padronizadas de erro HTTP.