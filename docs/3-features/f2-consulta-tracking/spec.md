# Feature F2 — Consulta Tracking

## Spec

### Objetivo
Expor via API REST os dados de tracking logístico por transportadora (dashboard consolidado e lista de entregas) e renderizar no portal Web.

### Requisitos

#### API — Dashboard
- `GET /api/tracking/{codigo}/dashboard`
- Retorna resumo consolidado: total de entregas, taxa de SLA, distribuição por status, custo total de frete, evolução mensal
- Código inválido retorna 404 com mensagem explicativa

#### API — Entregas
- `GET /api/tracking/{codigo}/entregas`
- Retorna lista de entregas com: id, status, origem, destino, data prevista, data entrega, custo frete
- Código inválido retorna 404

#### Frontend — Dashboard
- Exibe cards com: total entregas, taxa SLA (%), custo total frete (R$)
- Exibe distribuição por status (em_transito, entregue, atrasada)
- Exibe evolução mensal (tabela ou lista)

#### Frontend — Entregas
- Exibe tabela com colunas: ID, Status, Origem, Destino, Previsão, Entrega, Custo
- Badge de cor por status (verde=entregue, amarelo=em_transito, vermelho=atrasada)

### Critérios de Aceitação
- [ ] `GET /api/tracking/TRANSP001/dashboard` retorna 200 com dados consolidados
- [ ] `GET /api/tracking/TRANSP001/entregas` retorna 200 com lista de entregas
- [ ] `GET /api/tracking/INVALIDO/dashboard` retorna 404
- [ ] Dashboard Web renderiza cards e distribuição por status
- [ ] Entregas Web renderiza tabela com badges de cor

### Contrato da API

```
GET /api/tracking/{codigo}/dashboard
Response 200:
{
  "transportadora": "TRANSP001",
  "nome": "TransLog Express",
  "total_entregas": 150,
  "taxa_sla": 87.3,
  "distribuicao_status": {
    "entregue": 110,
    "em_transito": 25,
    "atrasada": 15
  },
  "custo_total_frete": 245800.50,
  "evolucao_mensal": [
    { "mes": "2025-01", "entregas": 45 },
    { "mes": "2025-02", "entregas": 52 },
    { "mes": "2025-03", "entregas": 53 }
  ]
}

GET /api/tracking/{codigo}/entregas
Response 200:
{
  "transportadora": "TRANSP001",
  "entregas": [
    {
      "id": "ENT-001",
      "status": "entregue",
      "origem": "São Paulo, SP",
      "destino": "Campinas, SP",
      "data_prevista": "2025-03-10",
      "data_entrega": "2025-03-09",
      "custo_frete": 1250.00
    }
  ]
}

Response 404:
{
  "detail": "Transportadora não encontrada"
}
```

### Referências
- ADR-002: Persistência JSON
- ADR-004: Arquitetura em camadas
- docs/1-envisioning/modernizacao-tracking-logistico.md (seção 5 — Jornada do Usuário)
