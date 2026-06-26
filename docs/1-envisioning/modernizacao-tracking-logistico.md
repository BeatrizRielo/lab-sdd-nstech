# Envisioning: Modernização do Tracking Logístico

> **Status:** Aprovado  
> **Última atualização:** 2026-06-18  
> **Versão:** 1.0

---

| Aspecto            | Informação                                         |
| ------------------ | -------------------------------------------------- |
| **Empresa/Time**   | RieloTECH — Time de Modernização do Tracking           |
| **Domínio**        | Logística e supply chain — tracking de entregas     |
| **Escala do time** | Pequeno (squad dedicado, <10 devs)                  |
| **Canais**         | CLI legada (estado atual) e Web + API REST (alvo)   |

| Aspecto                        | Informação                                                                                                 |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Perfil**                     | Operador logístico que consulta status de entregas, SLA e custos de frete por transportadora               |
| **Volume esperado**            | Alto (milhares de consultas diárias quando integrado à plataforma Open Logistics)                          |
| **Volume atual desta release** | Baixo — primeira versão consome snapshot curado de homologação (3 transportadoras representativas)          |
| **Contexto de uso**            | Consulta on-demand a partir de código de transportadora                                                     |

---

## 1. Contexto

Existe uma aplicação interna em Python que recebe um código de transportadora via linha de comando e retorna, em formato textual, dados consolidados de tracking logístico (entregas em andamento, SLA, custos de frete, rotas ativas). Essa ferramenta é utilizada por times internos de operação e suporte da RieloTECH.

A modernização visa transformar essa experiência em um **Portal Web (Frontend + Backend + API REST)**, preservando a regra de negócio e expondo contratos explícitos para reuso em outros canais (mobile, integrações B2B, parceiros).

> **Observação sobre dados:** os payloads exibidos nas specs e o conteúdo dos arquivos `data/<transportadora>/dashboard.json` e `data/<transportadora>/entregas.json` representam um **snapshot curado de dados de homologação**, fornecido pelo time de produto, válido apenas para esta primeira release.

---

## 2. Problema e Oportunidade

A regra de consulta de tracking logístico está acoplada a uma ferramenta CLI procedural, sem contrato explícito, sem reuso e sem experiência visual. Modernizar significa expor essa regra como **API REST** e oferecer **experiência Web** para operadores e gestores.

| Aspecto                          | Decisão                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Foco escolhido**               | Reconstruir a experiência de tracking como Web (Dashboard + Entregas), com API REST e contratos versionados   |
| **Justificativa**                | Habilita reuso em outros canais, reduz dependência da CLI legada e melhora experiência do operador             |
| **Escopo desta release**         | Dashboard (resumo consolidado), Tela Entregas (lista de entregas com status), API REST com 2 endpoints + health |
| **Fora do escopo desta release** | Autenticação real (login mock), integração com TMS/WMS reais, paginação, exportação, deploy em produção        |

---

## 3. Personas

### 3.1 Operador logístico (usuário principal)

Profissional de operações que monitora entregas e performance de transportadoras.

**Necessidades principais:**
- Visualizar total de entregas e taxa de SLA
- Entender distribuição por status (em trânsito, entregue, atrasada)
- Acompanhar custos de frete consolidados
- Consultar entregas detalhadas por transportadora

### 3.2 Gestor de supply chain

Líder que precisa de visão gerencial sobre a operação logística.

**Necessidades principais:**
- Acesso à mesma informação em formato visual
- Indicadores de performance (SLA, custo médio)
- Continuidade temporária com a CLI durante a transição

---

## 4. Diagnóstico: Dores Conhecidas

| Problema                          | Impacto                                                               | Fonte          |
| --------------------------------- | --------------------------------------------------------------------- | -------------- |
| Experiência limitada a terminal   | Inviável para gestores; baixa adoção entre canais digitais            | Operação atual |
| Sem contrato explícito de dados   | Cada novo canal reimplementa a regra do zero                          | Operação atual |
| Lógica acoplada a I/O textual     | Mudança de UI ou de canal exige tocar a regra de negócio              | Operação atual |
| Sem rastreabilidade de decisões   | Decisões arquiteturais perdidas quando devs saem do time              | Operação atual |

---

## 5. Jornada do Usuário

### 5.1 Fase: Login (Mock)
| Momento                                                  | Canal |
| -------------------------------------------------------- | ----- |
| Acessa portal Web                                        | Web   |
| Informa código da transportadora                         | Web   |
| Sessão iniciada com código persistido em `sessionStorage` | Web   |

### 5.2 Fase: Dashboard
| Momento                                         | Canal |
| ------------------------------------------------ | ----- |
| Visualiza total de entregas e SLA                | Web   |
| Visualiza distribuição por status                | Web   |
| Visualiza custo de frete consolidado             | Web   |
| Visualiza evolução mensal de entregas            | Web   |
| Navega para Entregas                             | Web   |

### 5.3 Fase: Consulta Entregas
| Momento                                                      | Canal |
| ------------------------------------------------------------ | ----- |
| Visualiza lista de entregas com status, origem e destino     | Web   |
| Volta para Dashboard pela sidebar                            | Web   |
| Sai da sessão                                                | Web   |

---

## 6. Objetivos Estratégicos

Disponibilizar, em canal Web, a mesma informação consolidada hoje obtida via CLI, com qualidade visual adequada ao operador logístico e contratos reaproveitáveis pelos demais canais.

Entregar uma versão web composta por:
- Backend Python (FastAPI) com 2 endpoints REST + health
- Frontend Web composto por página de login (mock), Dashboard e Entregas
- Camada de dados isolada, baseada em snapshot curado de homologação
- **Estrutura de specs e ADRs versionada que documenta as decisões de arquitetura**

| KPI                                                  | Meta          | Baseline Atual       |
| ---------------------------------------------------- | ------------- | -------------------- |
| Disponibilidade da API em homologação                | ≥ 99%         | N/A (não existe API) |
| Tempo de resposta P95 dos endpoints                  | < 500 ms      | N/A                  |
| Aderência da implementação aos contratos da API Spec | 100%          | N/A                  |

---

## 7. Restrições e Considerações

- **Reaproveitamento da linguagem do legado:** o time já mantém Python; mudar de stack aumentaria custo sem ganho proporcional.
- **Nenhuma dependência de cloud nesta release:** ambiente de homologação local.
- **Códigos sintéticos no snapshot de homologação:** TRANSP001, TRANSP002, TRANSP003.

### Princípios Não-Negociáveis

- **Specs antes de código:** toda implementação parte de uma spec versionada
- **Contratos explícitos:** API Spec define request/response antes da implementação
- **Decisões registradas:** toda decisão arquitetural significativa deve ter um ADR
- **Separação de camadas:** domínio, dados e apresentação isolados desde a primeira release

---

**Cliente:** RieloTECH — Time de Modernização do Tracking  
**Equipe técnica:** Squad de modernização
