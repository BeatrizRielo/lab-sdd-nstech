# Lab Guide — Spec-Driven Development com GitHub Copilot

> **Duração:** ~30 minutos  
> **Pré-requisitos:** Python 3.11+, VS Code com GitHub Copilot (Agent mode), Git  
> **Cenário:** Modernizar CLI de tracking logístico da RieloTECH para API REST + Portal Web

---

## Bloco 00 — Setup do Ambiente (3 min)

### Objetivo
Clonar o repositório, verificar a CLI legada e entender a estrutura do projeto.

### Passos

1. **Abra o terminal e clone o repositório:** https://github.com/BeatrizRielo/lab-sdd-nstech.git
   ```bash
   git clone <url-do-repo> lab-sdd-nstech
   cd lab-sdd-nstech
   ```

2. **Teste a CLI legada:**
   ```bash
   python legacy/consulta_tracking.py TRANSP001
   ```
   Você deve ver o dashboard e a lista de entregas da TransLog Express.

3. **Explore a estrutura do projeto:**
   ```
   lab-sdd-nstech/
   ├── .github/         ← Agents, skills, prompts e instructions do Copilot
   ├── docs/            ← Envisioning, ADRs, specs e tasks
   ├── legacy/          ← CLI Python legada + dados JSON
   ├── lab-guide/       ← Este roteiro
   ├── backend/         ← (vazio — será criado no lab)
   └── frontend/        ← (vazio — será criado no lab)
   ```

4. **Abra o projeto no VS Code:**
   ```bash
   code .
   ```

### ✅ Checkpoint
- [ ] CLI legada funciona com `TRANSP001`
- [ ] Projeto aberto no VS Code
- [ ] Copilot habilitado em Agent mode

---

## Bloco 01 — Entender a Intenção (5 min)

### Objetivo
Ler os artefatos de intenção (envisioning + ADRs) e entender o que será construído e por quê.

### Passos

1. **Leia o documento de envisioning:**
   Abra `docs/1-envisioning/modernizacao-tracking-logistico.md` e identifique:
   - Qual o problema que estamos resolvendo?
   - Quem são as personas?
   - Quais são os princípios não-negociáveis?

2. **Leia o plano de release:**
   Abra `docs/2-kickoff/plan.md` e entenda as 4 features planejadas.

3. **Leia os ADRs:**
   Abra `docs/architecture/decisions/` e leia os 4 ADRs:
   - ADR-001: Por que FastAPI?
   - ADR-002: Por que JSON ao invés de banco?
   - ADR-003: Por que frontend vanilla?
   - ADR-004: Por que arquitetura em camadas?

4. **Use o Copilot para resumir:**
   No Copilot Chat, pergunte:
   ```
   Resuma o documento de envisioning e os ADRs deste projeto.
   Quais são as decisões arquiteturais e por quê?
   ```

### 💡 Conceito SDD
> No SDD, o código não começa pela implementação. Começa pela **intenção documentada**.
> Os ADRs registram o "por quê" das decisões. As specs registram o "o quê". O código é apenas o "como".

### ✅ Checkpoint
- [ ] Entendeu o cenário de modernização
- [ ] Leu os 4 ADRs e compreendeu as decisões
- [ ] Copilot respondeu com contexto do projeto (prova que `.github/copilot-instructions.md` funciona)

---

## Bloco 02 — Ler a Spec e Implementar F1 (5 min)

### Objetivo
Implementar o scaffolding do projeto usando o Agent mode do Copilot, guiado pela spec.

### Passos

1. **Leia a spec da feature F1:**
   Abra `docs/3-features/f1-scaffolding-projeto/spec.md`

2. **Use o prompt template para implementar:**
   No Copilot Chat (Agent mode), use:
   ```
   @workspace /implementar-feature f1-scaffolding-projeto
   ```
   Ou peça diretamente:
   ```
   Implemente a feature F1 (Scaffolding do Projeto) seguindo a spec em
   docs/3-features/f1-scaffolding-projeto/spec.md e as tasks correspondentes.
   Siga a arquitetura definida nos ADRs.
   ```

3. **Observe como o Copilot:**
   - Lê a spec antes de gerar código
   - Segue a arquitetura em camadas (ADR-004)
   - Cria a estrutura de diretórios conforme spec
   - Implementa o health check com o contrato exato

4. **Teste o health check:**
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
   Em outro terminal:
   ```bash
   curl http://localhost:8000/health
   ```

### 💡 Feature do Copilot: `copilot-instructions.md`
> O arquivo `.github/copilot-instructions.md` dá contexto permanente ao Copilot sobre o projeto.
> Ele sabe que este é um projeto SDD, conhece a stack e as convenções.

### ✅ Checkpoint
- [ ] Backend FastAPI rodando
- [ ] `GET /health` retorna `{ "status": "healthy", "service": "tracking-api" }`
- [ ] Estrutura de diretórios criada conforme spec

---

## Bloco 03 — Implementar F2 com Agent SDD (8 min)

### Objetivo
Implementar a feature principal (Consulta Tracking) usando o agent `sdd-implementer`.

### Passos

1. **Leia a spec de F2:**
   Abra `docs/3-features/f2-consulta-tracking/spec.md` e observe:
   - 2 endpoints com contratos detalhados
   - Critérios de aceitação explícitos
   - Referências a ADRs

2. **Acione o agent sdd-implementer:**
   ```
   @sdd-implementer Implemente a feature F2 (Consulta Tracking).
   Leia a spec e as tasks antes de começar.
   ```

3. **Observe o agent:**
   - Ele lê spec e tasks antes de codificar
   - Cita a spec e task em cada arquivo
   - Segue as camadas: data → service → route
   - Respeita o contrato da API

4. **Teste os endpoints:**
   ```bash
   curl http://localhost:8000/api/tracking/TRANSP001/dashboard
   curl http://localhost:8000/api/tracking/TRANSP001/entregas
   curl http://localhost:8000/api/tracking/INVALIDO/dashboard
   ```

5. **Teste o frontend:**
   Abra `http://localhost:8000` no navegador, faça login com `TRANSP001` e navegue pelo Dashboard e Entregas.

### 💡 Features do Copilot: Agents + Prompt Templates
> - **AGENTS.md** define agents especializados (implementer, reviewer) com regras de comportamento
> - **Prompt templates** (`.github/prompts/`) padronizam como acionar cada workflow
> - **Skills** (`.github/skills/`) fornecem padrões de código por camada

### ✅ Checkpoint
- [ ] Dashboard retorna dados consolidados de TRANSP001
- [ ] Entregas retorna lista com 8 registros
- [ ] Código inválido retorna 404
- [ ] Frontend renderiza dashboard e entregas

---

## Bloco 04 — Revisar com o Agent SDD Reviewer (4 min)

### Objetivo
Usar o agent de revisão para validar conformidade da implementação com a spec.

### Passos

1. **Acione o agent sdd-reviewer:**
   ```
   @sdd-reviewer Revise a implementação de F2 (Consulta Tracking)
   contra a spec em docs/3-features/f2-consulta-tracking/spec.md
   ```

2. **Analise o relatório:**
   - Cada critério de aceitação está ✅ ou ❌?
   - Existem divergências (EXCESSO, FALTA, DIVERGÊNCIA)?
   - O contrato da API está sendo respeitado?

3. **Se houver divergências:**
   - Corrija com base no relatório
   - Reexecute a revisão

### 💡 Conceito SDD: A Spec como Juiz
> No SDD, quando há conflito entre código e spec, **a spec ganha**.
> O reviewer não avalia "qualidade de código" — avalia **conformidade com a intenção documentada**.

### ✅ Checkpoint
- [ ] Relatório de revisão gerado
- [ ] Todos os critérios ✅ ou divergências corrigidas
- [ ] Entendeu a diferença entre code review e SDD review

---

## Bloco 05 — Criar ADR e Spec para Nova Feature (3 min)

### Objetivo
Experimentar o ciclo completo: decisão → ADR → spec → code, criando artefatos para F3.

### Passos

1. **Crie um ADR para uma nova decisão:**
   Use o prompt template:
   ```
   @workspace /criar-adr "Usar arredondamento banker's rounding para valores monetários"
   ```
   Ou peça:
   ```
   Crie um ADR para a decisão de usar arredondamento padrão Python (round half to even)
   para todos os valores monetários do sistema. Siga o formato dos ADRs existentes.
   ```

2. **Leia a spec de F3:**
   Abra `docs/3-features/f3-calculo-frete/spec.md`

3. **Implemente F3 com o agent:**
   ```
   @sdd-implementer Implemente F3 (Cálculo de Frete) seguindo a spec.
   ```

4. **Teste:**
   ```bash
   curl http://localhost:8000/api/tracking/TRANSP001/frete
   ```

### 💡 Feature do Copilot: Memory + Knowledge Bases
> O Copilot usa `.github/copilot-instructions.md` como knowledge base local.
> Com **Memory**, ele lembra de padrões e convenções entre sessões.
> Com **Custom Instructions (Org)**, toda a organização segue as mesmas regras.

### ✅ Checkpoint
- [ ] ADR-005 criado com formato correto
- [ ] F3 implementada e endpoint funcionando
- [ ] Custo médio calculado corretamente

---

## Bloco 06 — Reflexão e Próximos Passos (2 min)

### O que praticamos

| Conceito SDD                | Feature do Copilot usada         |
| --------------------------- | -------------------------------- |
| Spec antes de código        | copilot-instructions.md          |
| Implementação guiada        | Agent mode + sdd-implementer     |
| Revisão de conformidade     | Agent mode + sdd-reviewer        |
| Decisões documentadas (ADR) | Prompt templates + criar-adr     |
| Padrões de código           | Skills (backend-builder)         |
| Workflow padronizado        | Prompt templates                 |

### Maturidade SDD

| Nível | Descrição                             | Onde estamos no lab        |
| ----- | ------------------------------------- | -------------------------- |
| 0     | Vibe Coding — sem spec               | CLI legada (antes do lab)  |
| 1     | Specs existem, código é rei           | —                          |
| 2     | Specs dirigem, code review valida     | Bloco 03-04                |
| 3     | Agents validam conformidade           | Bloco 04                   |
| 4     | Spec é a verdade, código é derivado   | Bloco 05 (ciclo completo)  |

### Próximos passos sugeridos
- Implementar F4 (Alertas de SLA) seguindo o mesmo workflow
- Explorar **Copilot Hooks** para validação automática pré-commit
- Configurar **MCP** para integrar Copilot com sistemas externos
- Adotar **Coding Agent** para PRs automatizados a partir de specs

---

## Troubleshooting

### "Copilot não reconhece o agent"
- Verifique se está usando **Agent mode** (não Chat mode)
- Confirme que `.github/agents/sdd-implementer.md` existe
- Reinicie o VS Code

### "Endpoint retorna 404 para transportadora válida"
- Verifique o caminho dos dados: `legacy/data/TRANSP001/`
- Confirme que o loader está apontando para `legacy/data/`
- Verifique se o código está em maiúsculas (TRANSP001)

### "FastAPI não inicia"
- Confirme: `pip install -r backend/requirements.txt`
- Execute de dentro do diretório raiz: `uvicorn backend.app.main:app --reload`

### "Frontend não carrega"
- Verifique se FastAPI está servindo arquivos estáticos
- Acesse diretamente: `http://localhost:8000/index.html`
