# Tasks — F3: Cálculo de Frete

## Task 3.1 — Criar service de frete
- Criar `backend/app/services/frete_service.py`
- Função `calcular_frete(codigo: str) -> dict`
- Carrega entregas via loader
- Calcula custo total, custo médio e custo por status
- Arredonda valores monetários em 2 casas decimais

## Task 3.2 — Criar route de frete
- Adicionar `GET /api/tracking/{codigo}/frete` em `tracking.py` ou novo router
- Delegar ao frete_service
- Handler de 404 para código inválido

## Task 3.3 — Validar contrato
- Testar endpoint com `curl`
- Validar que custo_medio = custo_total / total_entregas
- Validar agrupamento por status está correto
- Testar código inválido retorna 404
