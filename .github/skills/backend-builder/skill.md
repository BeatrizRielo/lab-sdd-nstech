# Backend Builder Skill

## Descrição
Skill para construir componentes do backend FastAPI seguindo a arquitetura em camadas.

## Instruções

Ao construir um componente backend:

1. **Identifique a camada:** route, service ou data
2. **Leia a spec** correspondente antes de implementar
3. **Siga o padrão de cada camada:**

### Camada Data (`backend/app/data/`)
```python
# Responsabilidade: carregar dados do snapshot JSON
# Não contém lógica de negócio
# Retorna None se dado não existe

def carregar_RECURSO(codigo: str) -> dict | None:
    caminho = Path(__file__).parent.parent.parent.parent / "legacy" / "data" / codigo / "ARQUIVO.json"
    if not caminho.exists():
        return None
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
```

### Camada Service (`backend/app/services/`)
```python
# Responsabilidade: lógica de negócio e orquestração
# Recebe dados do loader, processa e retorna
# Levanta exceção para casos de erro

from fastapi import HTTPException

def obter_RECURSO(codigo: str) -> dict:
    dados = carregar_RECURSO(codigo)
    if dados is None:
        raise HTTPException(status_code=404, detail="Transportadora não encontrada")
    return dados
```

### Camada Routes (`backend/app/routes/`)
```python
# Responsabilidade: receber HTTP, validar input, delegar ao service
# Não contém lógica de negócio
# Segue exatamente o contrato da spec

from fastapi import APIRouter
router = APIRouter()

@router.get("/api/tracking/{codigo}/RECURSO")
def RECURSO(codigo: str):
    return obter_RECURSO(codigo)
```

4. **Registre o router** no `main.py`
5. **Valide o contrato** contra a spec
