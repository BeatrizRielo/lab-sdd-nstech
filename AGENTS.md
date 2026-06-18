# Agents

Este projeto utiliza **GitHub Copilot Agents** customizados para o workflow SDD.

## Agents Disponíveis

### @sdd-implementer
Implementa código seguindo rigorosamente as specs e ADRs.
- Lê a spec antes de codificar
- Segue a ordem das tasks
- Respeita contratos da API
- Cita spec/task em cada arquivo criado

### @sdd-reviewer
Valida conformidade da implementação com as specs.
- Verifica cada critério de aceitação
- Classifica divergências (EXCESSO / FALTA / DIVERGÊNCIA)
- Gera relatório estruturado de conformidade

## Como Usar

```
# Implementar uma feature
@sdd-implementer Implemente a feature F2 (Consulta Tracking)

# Revisar conformidade
@sdd-reviewer Revise F2 contra a spec

# Criar ADR
Use o prompt template: /criar-adr "Descrição da decisão"
```

## Prompts Disponíveis

| Prompt                    | Uso                                      |
| ------------------------- | ---------------------------------------- |
| `/implementar-feature`    | Implementar feature seguindo spec+tasks  |
| `/revisar-conformidade`   | Validar conformidade com spec            |
| `/criar-adr`             | Criar novo Architecture Decision Record  |
