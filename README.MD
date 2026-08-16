# RF Technology CRM OS - API & Web Application

Sistema de gestão de clientes (CRM) e controle de acesso desenvolvido em Python utilizando **FastAPI**, persistência relacional com **SQLite** e renderização de páginas web via **Jinja2 Templates**.

---

## 📂 Arquitetura da Aplicação

A estrutura do projeto adota uma divisão modular de responsabilidades baseada no padrão de repositórios (Repository Pattern) e injeção de dependências:

app/
├── banco_de_dados/      # Conexão SQLite e repositórios de dados
│   ├── local_db.py
│   ├── cliente_repositorio.py
│   └── usuario_repositorio.py
├── modelos/             # Schemas Pydantic para validação e serialização
│   ├── clientes.py
│   └── usuario.py
├── rotas/               # Endpoints REST e rotas de páginas web
│   ├── clientes.py
│   ├── login.py
│   └── registro.py
├── dependencias.py      # Injeção de dependências da aplicação
└── main.py              # Ponto de entrada e inicialização do FastAPI
static/                  # Arquivos estáticos (CSS customizado)
templates/               # Templates HTML renderizados com Jinja2

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**
* **FastAPI** (Framework Web REST e SSR)
* **Pydantic** (Validação e tipagem de dados)
* **SQLite3** (Persistência relacional em banco de dados local)
* **Jinja2** (Mecanismo de renderização de templates HTML)
* **Uvicorn** (Servidor ASGI)
* **Bootstrap 5** (Interface responsiva com tema customizado)

---

## 🌐 Rotas da Aplicação

**Páginas Web (Interface HTML):**
* `GET /` : Página inicial / Dashboard
* `GET /login` : Formulário de login
* `POST /login` : Processamento do login e emissão de cookie de sessão
* `GET /login/logout` : Encerramento de sessão e exclusão de cookies
* `GET /registro` : Formulário de criação de conta
* `POST /registro` : Cadastro de novo usuário no banco de dados
* `GET /clientes` : Listagem visual de clientes cadastrados
* `GET /clientes/novo` : Formulário para cadastrar novo cliente
* `GET /clientes/{cliente_id}` : Formulário para edição de cliente

**API REST (JSON):**
* `GET /health` : Verificação do status do servidor
* `GET /api/clientes` : Retorna a listagem de todos os clientes
* `GET /api/clientes/{cliente_id}` : Retorna os dados de um cliente por ID
* `POST /api/clientes` : Cria um novo cliente
* `PUT /api/clientes/{cliente_id}` : Atualiza os dados de um cliente existente
* `DELETE /api/clientes/{cliente_id}` : Remove um cliente do banco

---

## 🚀 Execução da Aplicação

Com as dependências instaladas, inicie o servidor com:

uvicorn app.main:app --reload

Acesse no navegador:
* **Aplicação Web:** http://127.0.0.1:8000
* **Swagger UI (Documentação Interativa):** http://127.0.0.1:8000/docs