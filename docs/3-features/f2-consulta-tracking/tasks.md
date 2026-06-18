# Tasks — F2: Consulta Tracking

## Task 2.1 — Criar camada de dados
- Criar `backend/app/data/loader.py`
- Função `carregar_dashboard(codigo: str) -> dict | None`
- Função `carregar_entregas(codigo: str) -> list | None`
- Carrega de `legacy/data/{codigo}/dashboard.json` e `entregas.json`
- Retorna `None` se transportadora não existir

## Task 2.2 — Criar service de tracking
- Criar `backend/app/services/tracking_service.py`
- Função `obter_dashboard(codigo: str) -> dict`
- Função `obter_entregas(codigo: str) -> dict`
- Delega ao loader; levanta exceção se código inválido

## Task 2.3 — Criar routes de tracking
- Criar `backend/app/routes/tracking.py` com APIRouter
- `GET /api/tracking/{codigo}/dashboard` → delega ao service
- `GET /api/tracking/{codigo}/entregas` → delega ao service
- Handler de 404 para código inválido
- Registrar router no `main.py`

## Task 2.4 — Implementar Dashboard Web
- Editar `frontend/dashboard.html`
- Fetch `GET /api/tracking/{codigo}/dashboard` usando código do `sessionStorage`
- Renderizar cards: total entregas, taxa SLA, custo total frete
- Renderizar distribuição por status com badges coloridos
- Renderizar evolução mensal

## Task 2.5 — Implementar Entregas Web
- Editar `frontend/entregas.html`
- Fetch `GET /api/tracking/{codigo}/entregas`
- Renderizar tabela com colunas: ID, Status, Origem, Destino, Previsão, Entrega, Custo
- Badges de cor por status (verde=entregue, amarelo=em_transito, vermelho=atrasada)

## Task 2.6 — Validar contratos
- Testar todos os endpoints com `curl` ou navegador
- Validar que resposta segue exatamente o contrato da spec
- Testar código inválido retorna 404
