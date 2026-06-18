# Feature F4 — Alertas de SLA

## Spec

### Objetivo
Expor endpoint REST que retorna entregas com SLA violado (atrasadas) e indicadores de risco para a transportadora.

### Requisitos

#### API
- `GET /api/tracking/{codigo}/alertas-sla`
- Retorna: total de alertas, taxa de violação (%), lista de entregas atrasadas com dias de atraso
- Código inválido retorna 404

### Critérios de Aceitação
- [ ] `GET /api/tracking/TRANSP001/alertas-sla` retorna 200 com alertas
- [ ] Apenas entregas com status "atrasada" aparecem na lista
- [ ] Dias de atraso calculados como diferença entre `data_entrega` (ou data atual) e `data_prevista`
- [ ] Taxa de violação = (atrasadas / total) * 100, arredondada em 1 casa
- [ ] Código inválido retorna 404

### Contrato da API

```
GET /api/tracking/{codigo}/alertas-sla
Response 200:
{
  "transportadora": "TRANSP001",
  "total_alertas": 15,
  "taxa_violacao": 10.0,
  "total_entregas": 150,
  "entregas_atrasadas": [
    {
      "id": "ENT-042",
      "origem": "Curitiba, PR",
      "destino": "Florianópolis, SC",
      "data_prevista": "2025-03-05",
      "dias_atraso": 3,
      "custo_frete": 1890.00
    }
  ]
}
```

### Regras de Negócio
- Entrega atrasada: `status == "atrasada"`
- Dias de atraso: se `data_entrega` existe, `data_entrega - data_prevista`; senão, `data_atual - data_prevista`
- Taxa de violação = (total_alertas / total_entregas) * 100

### Referências
- ADR-002: Persistência JSON
- F2 spec (estrutura de entregas)
