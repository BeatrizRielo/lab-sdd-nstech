# Tasks — F4: Alertas de SLA

## Task 4.1 — Criar service de alertas SLA
- Criar `backend/app/services/sla_service.py`
- Função `obter_alertas_sla(codigo: str) -> dict`
- Filtra entregas com status "atrasada"
- Calcula dias de atraso para cada entrega
- Calcula taxa de violação

## Task 4.2 — Criar route de alertas SLA
- Adicionar `GET /api/tracking/{codigo}/alertas-sla` no router
- Delegar ao sla_service
- Handler de 404 para código inválido

## Task 4.3 — Validar contrato
- Testar endpoint com `curl`
- Validar que apenas entregas atrasadas aparecem
- Validar cálculo de dias_atraso
- Validar taxa_violacao
- Testar código inválido retorna 404
