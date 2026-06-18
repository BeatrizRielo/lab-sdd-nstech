# Feature F1 — Scaffolding do Projeto

## Spec

### Objetivo
Criar a estrutura base do backend (FastAPI) e do frontend (HTML/CSS/JS), incluindo health check e configuração de CORS.

### Requisitos

#### Backend
- Projeto Python com FastAPI
- Endpoint `GET /health` retornando `{ "status": "healthy", "service": "tracking-api" }`
- CORS habilitado para `http://localhost:*`
- Estrutura de diretórios: `backend/app/routes/`, `backend/app/services/`, `backend/app/data/`
- Arquivo `requirements.txt` com dependências

#### Frontend
- Estrutura de diretórios: `frontend/`
- Arquivo `index.html` com página de login mock
- Login mock: campo para código da transportadora, salva em `sessionStorage`, redireciona para dashboard
- Sidebar com navegação: Dashboard, Entregas, Sair

### Critérios de Aceitação
- [ ] `GET /health` retorna 200 com JSON esperado
- [ ] Frontend servido como arquivo estático acessível no navegador
- [ ] Login mock persiste código da transportadora em `sessionStorage`
- [ ] Sidebar presente com links funcionais

### Contrato da API

```
GET /health
Response 200:
{
  "status": "healthy",
  "service": "tracking-api"
}
```

### Referências
- ADR-001: Python com FastAPI
- ADR-003: Frontend vanilla
- ADR-004: Arquitetura em camadas
