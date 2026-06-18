# Feature F3 — Cálculo de Frete

## Spec

### Objetivo
Expor endpoint REST que retorna o custo consolidado de frete por transportadora, com métricas de custo médio por entrega e custo por status.

### Requisitos

#### API
- `GET /api/tracking/{codigo}/frete`
- Retorna: custo total, custo médio por entrega, custo por status (entregue, em_transito, atrasada)
- Código inválido retorna 404

### Critérios de Aceitação
- [ ] `GET /api/tracking/TRANSP001/frete` retorna 200 com custos consolidados
- [ ] Custo médio calculado corretamente (total / quantidade)
- [ ] Custo por status agrupado corretamente
- [ ] Código inválido retorna 404

### Contrato da API

```
GET /api/tracking/{codigo}/frete
Response 200:
{
  "transportadora": "TRANSP001",
  "custo_total": 245800.50,
  "custo_medio_por_entrega": 1638.67,
  "custo_por_status": {
    "entregue": 180200.00,
    "em_transito": 40850.50,
    "atrasada": 24750.00
  },
  "total_entregas": 150
}
```

### Regras de Negócio
- Custo médio = custo_total / total_entregas (arredondado em 2 casas)
- Custo por status = soma dos `custo_frete` das entregas agrupadas por `status`
- Valores monetários sempre em BRL com 2 casas decimais

### Referências
- ADR-002: Persistência JSON
- F2 spec (entregas contêm `custo_frete` individual)
