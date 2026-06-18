# Copilot Instructions — Lab SDD NSTECH

## Contexto do Projeto

Este é um projeto de modernização de uma CLI Python legada de tracking logístico para uma API REST + Portal Web.

**Domínio:** Logística e supply chain — tracking de entregas, SLA, custos de frete.

**Cliente:** NSTECH — maior empresa de tecnologia para logística da América Latina.

## Metodologia: Spec-Driven Development (SDD)

Este projeto segue SDD. Toda implementação deve ser dirigida por specs documentadas.

### Regras Fundamentais

1. **Specs antes de código:** nunca implemente sem uma spec correspondente em `docs/3-features/`
2. **ADRs para decisões:** decisões arquiteturais significativas devem ter ADR em `docs/architecture/decisions/`
3. **Contratos explícitos:** endpoints REST devem seguir exatamente o contrato definido na spec
4. **Rastreabilidade:** todo código deve ser rastreável a uma task, que aponta para uma spec

### Estrutura de Documentação

```
docs/
├── 1-envisioning/     # Visão do produto e personas
├── 2-kickoff/         # Plano de release e dependências
├── 3-features/        # Specs e tasks por feature
│   ├── f1-scaffolding-projeto/
│   ├── f2-consulta-tracking/
│   ├── f3-calculo-frete/
│   └── f4-alertas-sla/
└── architecture/
    └── decisions/     # ADRs (Architecture Decision Records)
```

## Stack Técnica

- **Backend:** Python 3.11+ com FastAPI (ADR-001)
- **Frontend:** HTML/CSS/JS vanilla (ADR-003)
- **Dados:** Arquivos JSON estáticos em `legacy/data/` (ADR-002)
- **Arquitetura:** Camadas routes → services → data (ADR-004)

## Convenções de Código

- Código e comentários em **português** (domínio logístico brasileiro)
- Nomes de variáveis e funções em **português** (snake_case)
- Docstrings em português
- Valores monetários em BRL, 2 casas decimais
- Status de entrega: `entregue`, `em_transito`, `atrasada`

## Workflow de Implementação

Para cada feature, siga esta ordem:
1. Ler a spec em `docs/3-features/fN-*/spec.md`
2. Ler as tasks em `docs/3-features/fN-*/tasks.md`
3. Implementar seguindo a ordem das tasks
4. Validar contra os critérios de aceitação da spec
5. Verificar que o contrato da API está sendo respeitado

## Dados de Referência

Transportadoras disponíveis no snapshot de homologação:
- `TRANSP001` — TransLog Express (150 entregas, SLA 87.3%)
- `TRANSP002` — RodoVia Cargas (89 entregas, SLA 92.1%)
- `TRANSP003` — AgroFrete Brasil (210 entregas, SLA 78.6%)
