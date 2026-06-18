# Prompt: Implementar Feature SDD

Implemente a feature **${{FEATURE}}** seguindo o workflow SDD:

1. Leia a spec em `docs/3-features/${{FEATURE}}/spec.md`
2. Leia as tasks em `docs/3-features/${{FEATURE}}/tasks.md`
3. Verifique os ADRs referenciados na spec
4. Implemente cada task na ordem definida
5. Ao final, valide contra os critérios de aceitação

Cite a spec e task em cada arquivo criado.
Siga a arquitetura em camadas (ADR-004): routes → services → data.
Respeite exatamente os contratos da API definidos na spec.
