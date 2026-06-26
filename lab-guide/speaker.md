# Speaker Notes — Lab SDD NSTECH

> Roteiro para condução técnica e narrativa do lab de modernização (CLI legada → API REST + Portal Web) usando Spec-Driven Development (SDD) com GitHub Copilot Agents.

---

## 1) Mensagem central do lab (abertura)

### O que dizer em 30–60 segundos

"Este lab não é sobre gerar código rápido. É sobre gerar **software alinhado à intenção de negócio**. A regra é: primeiro documentamos o *porquê* e o *o quê* (envisioning, ADRs, specs e tasks), depois implementamos o *como*."

### Motivo técnico

- Evita implementação ad-hoc e regressões de contrato.
- Cria rastreabilidade entre requisito, decisão e código.
- Facilita manutenção e evolução para novos canais (mobile/B2B).

### Motivo semântico (proposta do lab)

- A modernização não é só trocar tecnologia: é transformar conhecimento tácito do legado em conhecimento explícito e versionado.
- O time passa de “dependência de pessoas” para “dependência de artefatos de decisão”.

---

## 2) Como montar cada documentação SDD (guia prático)

## 2.1 Envisioning (`docs/1-envisioning/...`)

### Propósito

Definir contexto, problema, personas, objetivos, escopo, restrições e princípios não-negociáveis.

### Como montar

1. Contexto atual (estado legado e dores).
2. Problema/oportunidade com impacto de negócio.
3. Personas e jornada.
4. Objetivos estratégicos com KPIs mensuráveis.
5. Escopo e fora de escopo.
6. Princípios não-negociáveis (ex.: spec antes de código).

### Resultado esperado

- Alinhamento de negócio e tecnologia.
- Critério para decidir o que entra na release.

---

## 2.2 Plano de release (`docs/2-kickoff/plan.md`)

### Propósito

Sequenciar features e explicitar dependências.

### Como montar

1. Listar features macro (F1, F2, F3, F4).
2. Definir valor de cada uma.
3. Mapear dependências (grafo simples).
4. Definir estratégia da release (neste lab: local, sem cloud).

### Resultado esperado

- Time sabe o que fazer primeiro e por quê.
- Reduz bloqueio por ordem errada de implementação.

---

## 2.3 ADRs (`docs/architecture/decisions/`)

### Propósito

Registrar decisões arquiteturais com contexto, escolha, trade-offs e consequências.

### Como montar

Para cada ADR:
1. **Status** (aceito/proposto/substituído).
2. **Contexto** (qual dor técnica motivou a decisão).
3. **Decisão** (o que foi escolhido).
4. **Justificativa** (por que essa opção vence as alternativas).
5. **Consequências** (positivas e negativas).
6. **Alternativas consideradas**.

### Resultado esperado

- Menos debate repetido.
- Onboarding técnico mais rápido.
- Decisões auditáveis ao longo do tempo.

---

## 2.4 Specs por feature (`docs/3-features/fN-*/spec.md`)

### Propósito

Definir o comportamento esperado da feature de forma verificável.

### Como montar

Cada spec deve conter:
1. **Objetivo da feature** (1 parágrafo).
2. **Requisitos funcionais** (API/UI/regras).
3. **Critérios de aceitação** (checklist testável).
4. **Contrato explícito** (request/response e erros).
5. **Regras de negócio** (fórmulas, arredondamento, filtros).
6. **Referências** (ADRs e envisioning).

### Resultado esperado

- Código implementado contra contrato claro.
- Revisão orientada por conformidade, não por opinião.

---

## 2.5 Tasks por feature (`docs/3-features/fN-*/tasks.md`)

### Propósito

Quebrar a spec em passos executáveis por camada (data/service/route/frontend/teste).

### Como montar

1. Decompor por responsabilidades técnicas.
2. Nomear arquivos e funções explicitamente.
3. Incluir validação de contrato e casos de erro.
4. Preservar ordem de implementação.

### Resultado esperado

- Execução incremental com baixo risco.
- Facilidade de delegação (humano ou agent).

---

## 3) Roteiro técnico por bloco do lab (00 → 06)

## Bloco 00 — Setup do ambiente

### Explicação técnica

- Clonar repositório, validar CLI legada e abrir no VS Code.
- A CLI serve como baseline funcional da regra de negócio atual.

### Por que este passo existe

- Garante que o participante entenda o ponto de partida (sistema já gera valor, mas está acoplado ao terminal).
- Evita “modernizar no escuro”.

### Objetivo semântico

- Mostrar respeito ao legado: modernização é evolução, não descarte.

---

## Bloco 01 — Entender intenção (envisioning + plan + ADRs)

### Explicação técnica

- Ler `envisioning`, `plan` e ADRs antes de codificar.
- Fixar stack e arquitetura alvo:
  - FastAPI (ADR-001)
  - Persistência JSON snapshot (ADR-002)
  - Frontend vanilla (ADR-003)
  - Camadas routes/services/data (ADR-004)

### Por que este passo existe

- Evita decisões locais conflitantes com decisões globais.
- Evita retrabalho por desalinhamento arquitetural.

### Objetivo semântico

- Reforçar que “intenção documentada” é o contrato entre produto e engenharia.

---

## Bloco 02 — Implementar F1 (Scaffolding)

### Explicação técnica

- Criar estrutura mínima executável:
  - Backend FastAPI com CORS e `GET /health`
  - Frontend estático com login mock + navegação base
- Estabelecer base para as features de negócio.

### Por que este passo existe

- Sem F1, não há trilho técnico confiável para F2/F3/F4.
- O health check vira prova rápida de prontidão do backend.

### Objetivo semântico

- “Primeiro capacidade de entrega, depois complexidade de domínio.”

---

## Bloco 03 — Implementar F2 (Consulta Tracking)

### Explicação técnica

- Implementar fluxo principal da solução:
  - Data layer carrega snapshot por transportadora.
  - Service layer aplica regra de negócio e valida código.
  - Route layer expõe contratos REST de dashboard e entregas.
  - Frontend consome API e renderiza indicadores/tabela.

### Por que este passo existe

- Entrega valor de negócio visível (tracking operacional).
- Demonstra separação de camadas em caso real.

### Objetivo semântico

- Tornar o conhecimento da operação logística acessível e reutilizável por qualquer canal.

---

## Bloco 04 — Revisão com SDD Reviewer

### Explicação técnica

- Revisar implementação contra a spec de F2.
- Classificar divergências (excesso, falta, divergência de contrato).

### Por que este passo existe

- Em SDD, qualidade é **conformidade com intenção**.
- Evita “funciona aqui” mas quebra o contrato esperado.

### Objetivo semântico

- Consolidar disciplina: em conflito entre código e spec, a spec vence.

---

## Bloco 05 — Fechar ciclo (ADR + F3)

### Explicação técnica

- Criar nova decisão arquitetural/documental (ADR) e aplicar em nova feature (F3).
- Calcular custo total, custo médio e agrupamento por status com regras explícitas.

### Por que este passo existe

- Mostra o ciclo completo vivo: decisão → especificação → implementação → validação.

### Objetivo semântico

- Demonstrar governança técnica contínua, não pontual.

---

## Bloco 06 — Reflexão e próximos passos

### Explicação técnica

- Mapear maturidade SDD e identificar gap para próxima iteração (F4, automações, hooks).

### Por que este passo existe

- Sem retrospectiva, o processo não melhora.

### Objetivo semântico

- Transformar o lab em prática sustentável no dia a dia do time.

---

## 4) Objetivo final do lab (resumo para encerramento)

## Objetivo técnico final

- Evoluir de CLI legada para API REST + portal web com contratos explícitos.
- Garantir rastreabilidade entre documentação e implementação.
- Estabelecer arquitetura em camadas pronta para evolução.

## Objetivo semântico final

- Mudar o comportamento do time: sair de coding por impulso e adotar engenharia orientada por intenção.
- Criar linguagem comum entre produto, arquitetura e desenvolvimento.

## Frase de fechamento sugerida

"Neste lab, o código é consequência. O ativo principal é a clareza: decisões registradas, contratos explícitos e implementação verificável. Isso é SDD aplicado com propósito de negócio." 

---

## 5) Checklist rápido do apresentador

- [ ] Mostrei a CLI legada antes da modernização
- [ ] Expliquei por que cada ADR existe
- [ ] Conectei cada bloco a um objetivo técnico e semântico
- [ ] Mostrei contrato de API e critérios de aceitação
- [ ] Reforcei que spec é a fonte de verdade
- [ ] Encerrei com próximos passos (F4 + automação de conformidade)
