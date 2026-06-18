# ADR-004: Arquitetura em camadas com separação domínio/dados/apresentação

## Status
Aceito

## Contexto
A CLI legada mistura lógica de negócio, I/O e formatação textual em um único script. A modernização deve separar responsabilidades para viabilizar reuso da regra em múltiplos canais (Web, mobile, B2B).

## Decisão
Estruturar o backend em 3 camadas:
- **Routes (apresentação):** recebe HTTP, valida input, delega ao service
- **Services (domínio):** orquestra regra de negócio, calcula métricas, aplica filtros
- **Data (persistência):** carrega e retorna dados do snapshot JSON

## Justificativa
- Isola a regra de negócio (pode ser testada sem HTTP)
- Facilita substituição futura de JSON por banco real (só altera camada data)
- Alinha com princípio SDD de separação entre intenção e implementação
- Padrão conhecido pela equipe

## Consequências
- **Positivas:** Testabilidade; reuso de services em CLI e API; facilita evolução
- **Negativas:** Mais arquivos para um projeto pequeno; indireção pode parecer over-engineering no início

## Alternativas consideradas
- **Tudo em routes:** rápido mas acopla regra ao HTTP
- **Hexagonal/Ports & Adapters:** conceitualmente superior mas excede o escopo do lab
