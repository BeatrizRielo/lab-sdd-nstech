# ADR-003: Frontend com HTML/CSS/JS puro (sem framework SPA)

## Status
Aceito

## Contexto
O portal Web desta release é um MVP de visualização: login mock, dashboard com indicadores e lista de entregas. Não há necessidade de gerenciamento de estado complexo, roteamento avançado ou componentização pesada.

## Decisão
Usar **HTML semântico, CSS moderno e JavaScript vanilla** para o frontend, servido como arquivos estáticos pelo próprio FastAPI.

## Justificativa
- Reduz dependências e tempo de setup (não precisa de npm, webpack, etc.)
- Foco do lab é no workflow SDD (spec → plan → tasks → código), não no framework frontend
- Suficiente para 3 telas simples (login, dashboard, entregas)
- Facilita demonstração de que a spec dirige o código, independente de framework

## Consequências
- **Positivas:** Zero build frontend; qualquer dev consegue ler e modificar; setup do lab em <5 minutos
- **Negativas:** Não escala para UIs complexas; sem componentização nativa; CSS sem design system

## Alternativas consideradas
- **React/Vue:** over-engineering para 3 telas; complexidade de setup no lab
- **HTMX:** interessante mas adiciona conceito novo ao lab
- **Jinja2 templates:** viável, mas separa menos frontend de backend
