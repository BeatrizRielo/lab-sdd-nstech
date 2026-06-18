# Plan — Modernização do Tracking Logístico

## Macro-Fases

| Seq | Feature                     | Descrição                                                                         |
| --- | --------------------------- | --------------------------------------------------------------------------------- |
| F1  | Scaffolding do projeto      | Setup backend (FastAPI) + frontend (HTML/CSS/JS), health check, CI local          |
| F2  | Consulta Tracking           | API + portal Web para dashboard de tracking e lista de entregas                   |
| F3  | Cálculo de Frete            | Endpoint de consulta de custo consolidado por transportadora                      |
| F4  | Alertas de SLA              | Endpoint que retorna entregas com SLA violado e indicadores de risco              |

## Estratégia de Release

Esta primeira release é **local** (sem deploy em cloud). O objetivo é validar:
1. Aderência da implementação à spec
2. Experiência do operador na consulta de tracking
3. Viabilidade de expansão para mobile e B2B

## Dependências entre Features

```
F1 (Scaffolding) → F2 (Consulta Tracking)
                 → F3 (Cálculo de Frete)
                 → F4 (Alertas de SLA)
```

F2, F3 e F4 são independentes entre si, mas todas dependem de F1.
