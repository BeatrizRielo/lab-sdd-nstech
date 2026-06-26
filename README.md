# LAB — Spec-Driven Development com GitHub Copilot

> Modernização guiada por specs: de uma CLI Python legada para uma API REST de tracking logístico, com agents customizados do Copilot dirigindo a geração de código.

```
lab-sdd-nstech/
├── .github/         # agents, skills, instructions do Copilot
├── docs/            # envisioning, ADRs, plan, specs e tasks por feature
├── legacy/          # CLI Python legada (em produção) + snapshot data/
├── lab-guide/       # roteiro do lab (7 blocos: 00–06 + troubleshooting)
├── backend/         # ← criado pelo participante durante o lab
└── frontend/        # ← criado pelo participante durante o lab
```

## Pré-requisitos

- Python 3.11+
- Git
- VS Code com GitHub Copilot habilitado em **Agent mode**
- Navegador moderno (Chrome/Edge)

## Como executar a aplicação (local)

### 1) Criar e ativar ambiente virtual

```bash
# na raiz do repositório
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Linux/macOS (bash/zsh)
source .venv/bin/activate
```

### 2) Instalar dependências

```bash
pip install -r backend/requirements.txt
```

### 3) Subir a API + frontend estático

```bash
python -m uvicorn app.main:app --reload --app-dir backend
```

Após iniciar, acesse `http://127.0.0.1:8000/`.

## Endpoints para validação

Base URL local: `http://127.0.0.1:8000`

| Tipo | Endpoint | Exemplo de uso |
| --- | --- | --- |
| Health check | `/health` | `GET /health` |
| Swagger UI | `/docs` | Abrir no navegador |
| OpenAPI JSON | `/openapi.json` | Abrir no navegador ou usar em clients |
| Teste tracking (dashboard) | `/api/tracking/{codigo}/dashboard` | `GET /api/tracking/TRANSP001/dashboard` |
| Teste tracking (entregas) | `/api/tracking/{codigo}/entregas` | `GET /api/tracking/TRANSP001/entregas` |
| Teste tracking (frete) | `/api/tracking/{codigo}/frete` | `GET /api/tracking/TRANSP001/frete` |

## Lab local — sem operações remotas

Este repositório é cenário didático. Os agents e o participante **não** executam `git push`, `gh pr create`, `docker push` ou qualquer publicação. Commits locais são permitidos quando solicitados.

## Cenário

A **NSTECH** é a maior empresa de tecnologia para logística e supply chain da América Latina. Ela opera a plataforma **Open Logistics**, conectando embarcadores, transportadoras, motoristas e destinatários.

Existe uma aplicação interna em Python (CLI) que recebe um código de transportadora via linha de comando e retorna dados consolidados de tracking de entregas (status, SLA, rotas, custos de frete). Essa ferramenta é utilizada por times internos de operação e suporte. A modernização visa transformar essa experiência em uma **API REST + Portal Web**, preservando regras de negócio e expondo contratos para reuso em outros canais (mobile, integrações B2B).

Material didático interno — NSTECH · 2026
