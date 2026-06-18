# ADR-002: Persistência baseada em arquivos JSON (snapshot de homologação)

## Status
Aceito

## Contexto
A primeira release não se conecta a banco de dados nem a APIs externas. Os dados são um snapshot curado de homologação fornecido pelo time de produto, representando 3 transportadoras com entregas, custos e indicadores de SLA.

## Decisão
Armazenar dados como arquivos JSON estáticos no diretório `data/<codigo_transportadora>/`, com dois arquivos por transportadora:
- `dashboard.json` — resumo consolidado (KPIs, distribuição por status, evolução mensal)
- `entregas.json` — lista detalhada de entregas

## Justificativa
- Zero dependência de infraestrutura (sem banco, sem cloud)
- Foco no contrato da API, não na camada de persistência
- Facilita setup do lab em qualquer máquina
- Dados isolados por transportadora simulam particionamento real

## Consequências
- **Positivas:** Setup instantâneo; foco na lógica de domínio e contratos; dados versionáveis no Git
- **Negativas:** Não escala para produção; sem queries complexas; dados estáticos

## Alternativas consideradas
- **SQLite:** adicionaria complexidade de setup sem ganho nesta release
- **PostgreSQL:** over-engineering para snapshot de homologação
- **API mock (json-server):** adiciona dependência de Node.js ao stack Python
