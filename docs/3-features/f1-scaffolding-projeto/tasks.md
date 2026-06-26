# Tasks — F1: Scaffolding do Projeto

## Task 1.1 — Criar estrutura backend
- Criar `backend/app/__init__.py`
- Criar `backend/app/main.py` com FastAPI app, CORS e health endpoint
- Criar diretórios `routes/`, `services/`, `data/` dentro de `backend/app/`
- Criar `backend/requirements.txt` com `fastapi` e `uvicorn`

## Task 1.2 — Criar estrutura frontend
- Criar `frontend/index.html` com tela de login mock
- Criar `frontend/dashboard.html` (placeholder)
- Criar `frontend/entregas.html` (placeholder)
- Criar `frontend/css/style.css` com tema RieloTECH
- Criar `frontend/js/app.js` com lógica de login e navegação

## Task 1.3 — Configurar servimento de estáticos
- Configurar FastAPI para servir `frontend/` como arquivos estáticos
- Validar acesso via navegador em `http://localhost:8000`

## Task 1.4 — Validar health check
- Executar `uvicorn backend.app.main:app --reload`
- Testar `GET /health` retorna `{ "status": "healthy", "service": "tracking-api" }`
