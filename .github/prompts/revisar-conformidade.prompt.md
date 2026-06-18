# Prompt: Revisar Conformidade SDD

Revise a implementação da feature **${{FEATURE}}** contra a spec:

1. Leia a spec em `docs/3-features/${{FEATURE}}/spec.md`
2. Leia o código implementado em `backend/app/` e `frontend/`
3. Para cada critério de aceitação, verifique se está atendido
4. Para cada campo do contrato da API, verifique se está correto
5. Classifique divergências como EXCESSO, FALTA ou DIVERGÊNCIA

Gere um relatório no formato definido no agent `sdd-reviewer.md`.
