# AGENTS.md

## Purpose
This file helps AI coding agents understand the structure and conventions of this FastAPI project.

## Project overview
- Python 3.11+ FastAPI backend for RF Technology CRM.
- Entry point: `app/main.py`
- Run locally with: `uvicorn app.main:app --reload`
- Swagger UI available at `http://127.0.0.1:8000/docs`

## Key folders and files
- `app/main.py` - FastAPI app creation, health check, front page, router registration.
- `app/rotas/clientes.py` - `/clientes` endpoints and route dependencies.
- `app/modelos/clientes.py` - Pydantic models: `Cliente`, `ClienteCriarAtualizar`.
- `app/banco_de_dados/local_db.py` - local SQLite database helper for `RFtech.db`.
- `app/banco_de_dados/cliente_repositorio.py` - repository layer for client CRUD operations.
- `app/dependencias.py` - dependency injection helpers for FastAPI.

## Important conventions
- Use Pydantic models from `app/modelos` for request and response validation.
- Keep route logic slim; use `ClienteRepositorio` for database operations.
- The current database is local SQLite, initialized by `BancoDeDadosLocal.inicializar_banco()`.
- Routes use FastAPI `Depends` to inject `ClienteRepositorio`.

## Current implementation scope
- Implemented endpoints: `GET /`, `GET /front`, `GET /clientes`, `GET /clientes/{cliente_id}`.
- The project is in early MVP stage; missing POST/PUT/DELETE endpoints and complete error handling.
- No dedicated tests or Docker configuration in the repository.

## Guidance for code changes
- Prefer incremental improvements that keep the current app structure.
- Do not invent unrelated frameworks or complex architecture beyond FastAPI, Pydantic, and SQLite.
- Use the README for setup and verification instructions.

## References
- README: `README.MD`
