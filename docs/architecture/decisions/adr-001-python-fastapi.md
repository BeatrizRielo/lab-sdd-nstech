# ADR-001: Uso de Python com FastAPI para o backend

## Status
Aceito

## Contexto
O time mantém a CLI legada em Python e possui fluência nessa linguagem. A modernização precisa de um framework web que ofereça performance adequada, tipagem explícita e geração automática de documentação OpenAPI — alinhado com o princípio SDD de contratos explícitos.

## Decisão
Adotar **Python 3.11+ com FastAPI** para o backend REST.

## Justificativa
- Reaproveitamento de competência Python do time
- FastAPI gera documentação OpenAPI automaticamente (spec-first por design)
- Tipagem via Pydantic reforça contratos entre camadas
- Ecossistema maduro para integração com TMS/WMS no futuro

## Consequências
- **Positivas:** Curva de aprendizado mínima; geração automática de specs OpenAPI; alta performance (async)
- **Negativas:** Equipe precisará aprender Pydantic e async patterns

## Alternativas consideradas
- **Django REST Framework:** mais pesado, ORM desnecessário nesta release
- **Flask:** sem tipagem nativa, sem geração automática de OpenAPI
- **Node.js/Express:** mudança de stack sem ganho proporcional
