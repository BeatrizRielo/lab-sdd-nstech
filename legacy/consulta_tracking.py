#!/usr/bin/env python3
"""
CLI Legada — Consulta de Tracking Logístico NSTECH
Uso: python consulta_tracking.py <CODIGO_TRANSPORTADORA>

Aplicação interna utilizada pelos times de operação e suporte.
Retorna dados consolidados de tracking de entregas via terminal.
"""

import json
import os
import sys
from pathlib import Path


def carregar_json(caminho: str) -> dict | list | None:
    if not os.path.exists(caminho):
        return None
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def exibir_dashboard(dados: dict) -> None:
    print("=" * 60)
    print(f"  DASHBOARD — {dados['nome']} ({dados['transportadora']})")
    print("=" * 60)
    print(f"  Total de Entregas:    {dados['total_entregas']}")
    print(f"  Taxa de SLA:          {dados['taxa_sla']}%")
    print(f"  Custo Total de Frete: R$ {dados['custo_total_frete']:,.2f}")
    print("-" * 60)
    print("  Distribuição por Status:")
    for status, qtd in dados["distribuicao_status"].items():
        label = status.replace("_", " ").title()
        print(f"    • {label}: {qtd}")
    print("-" * 60)
    print("  Evolução Mensal:")
    for item in dados["evolucao_mensal"]:
        print(f"    {item['mes']}: {item['entregas']} entregas")
    print("=" * 60)


def exibir_entregas(dados: dict) -> None:
    entregas = dados["entregas"]
    print(f"\n  ENTREGAS — {dados['transportadora']} ({len(entregas)} registros)")
    print("-" * 90)
    print(f"  {'ID':<10} {'Status':<14} {'Origem':<20} {'Destino':<20} {'Previsão':<12} {'Custo':>10}")
    print("-" * 90)
    for e in entregas:
        status_label = e["status"].replace("_", " ").title()
        custo = f"R$ {e['custo_frete']:,.2f}"
        print(f"  {e['id']:<10} {status_label:<14} {e['origem']:<20} {e['destino']:<20} {e['data_prevista']:<12} {custo:>10}")
    print("-" * 90)


def main():
    if len(sys.argv) < 2:
        print("Uso: python consulta_tracking.py <CODIGO_TRANSPORTADORA>")
        print("Exemplo: python consulta_tracking.py TRANSP001")
        sys.exit(1)

    codigo = sys.argv[1].upper()
    data_dir = Path(__file__).parent / "data" / codigo

    if not data_dir.exists():
        print(f"Erro: Transportadora '{codigo}' não encontrada.")
        print("Transportadoras disponíveis: TRANSP001, TRANSP002, TRANSP003")
        sys.exit(1)

    dashboard = carregar_json(str(data_dir / "dashboard.json"))
    entregas_data = carregar_json(str(data_dir / "entregas.json"))

    if dashboard:
        exibir_dashboard(dashboard)
    else:
        print(f"Aviso: Dados de dashboard não encontrados para {codigo}")

    if entregas_data:
        exibir_entregas(entregas_data)
    else:
        print(f"Aviso: Dados de entregas não encontrados para {codigo}")


if __name__ == "__main__":
    main()
