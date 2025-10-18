#!/usr/bin/env python3
"""
CONTABILIDADE PRECISA DE TODAS AS EQUAÇÕES
Contagem exata e sincronização completa
"""

from pathlib import Path
import json
import re

print("🔢 CONTABILIDADE PRECISA DAS EQUAÇÕES")
print("=" * 55)

# Coletar TODAS as equações de TODAS as bibliotecas
bibliotecas = [
    "BIBLIOTECA_QUANTICA_TRANSCENDENTAL",
    "BIBLIOTECA_EQUACOES_COSMICAS", 
    "BIBLIOTECA_QUANTICA_IBM",
    "BIBLIOTECA_SINTESE_QUANTICA",
    "BIBLIOTECA_COSMICA_UNICA",
    "BIBLIOTECA_QUANTICA"
]

# Estrutura para contabilidade precisa
contabilidade = {
    "total_equacoes_unicas": 0,
    "equacoes_por_biblioteca": {},
    "sequencia_completa": [],
    "lacunas": [],
    "duplicatas": {},
    "faixas_completas": {}
}

# Coletar todas as equações
todas_equacoes = set()

for biblioteca in bibliotecas:
    bib_path = Path(biblioteca)
    if bib_path.exists():
        equacoes_bib = set()
        arquivos_json = list(bib_path.rglob("EQ*.json"))
        
        for arquivo in arquivos_json:
            nome = arquivo.stem
            match = re.match(r'EQ(\d+)', nome)
            if match:
                num_eq = int(match.group(1))
                todas_equacoes.add(num_eq)
                equacoes_bib.add(num_eq)
        
        contabilidade["equacoes_por_biblioteca"][biblioteca] = {
            "total": len(equacoes_bib),
            "equacoes": sorted(equacoes_bib)
        }

# Contabilidade final
contabilidade["total_equacoes_unicas"] = len(todas_equacoes)
contabilidade["sequencia_completa"] = sorted(todas_equacoes)

# Identificar lacunas
for i in range(1, max(todas_equacoes) + 1):
    if i not in todas_equacoes:
        contabilidade["lacunas"].append(i)

# Identificar duplicatas entre bibliotecas
for num_eq in todas_equacoes:
    bibliotecas_com_eq = []
    for biblioteca, dados in contabilidade["equacoes_por_biblioteca"].items():
        if num_eq in dados["equacoes"]:
            bibliotecas_com_eq.append(biblioteca)
    
    if len(bibliotecas_com_eq) > 1:
        contabilidade["duplicatas"][num_eq] = bibliotecas_com_eq

# Análise por faixas
faixas = [(1, 50), (51, 100), (101, 145), (146, 230)]
for inicio, fim in faixas:
    equacoes_na_faixa = [eq for eq in todas_equacoes if inicio <= eq <= fim]
    contabilidade["faixas_completas"][f"EQ{inicio:04d}-EQ{fim:04d}"] = {
        "total": len(equacoes_na_faixa),
        "maximo": fim - inicio + 1,
        "completude": len(equacoes_na_faixa) / (fim - inicio + 1) * 100,
        "equacoes": equacoes_na_faixa
    }

# RELATÓRIO PRECISO
print("📊 RELATÓRIO PRECISO DE CONTABILIDADE:")
print(f"   • TOTAL DE EQUAÇÕES ÚNICAS: {contabilidade['total_equacoes_unicas']}")
print(f"   • PROGRESSO: {contabilidade['total_equacoes_unicas']}/230 ({contabilidade['total_equacoes_unicas']/230*100:.2f}%)")
print(f"   • FAIXA: EQ{min(todas_equacoes):04d} a EQ{max(todas_equacoes):04d}")

print(f"\n🎯 DISTRIBUIÇÃO POR BIBLIOTECA:")
for biblioteca, dados in contabilidade["equacoes_por_biblioteca"].items():
    print(f"   • {biblioteca}: {dados['total']} equações")

print(f"\n📈 ANÁLISE POR FAIXAS:")
for faixa, dados in contabilidade["faixas_completas"].items():
    status = "✅ COMPLETA" if dados["completude"] == 100 else "⚠️  INCOMPLETA"
    print(f"   • {faixa}: {dados['total']}/{dados['maximo']} ({dados['completude']:.1f}%) - {status}")

print(f"\n🔎 LACUNAS NA SEQUÊNCIA:")
if contabilidade["lacunas"]:
    print(f"   • {len(contabilidade['lacunas'])} lacunas encontradas")
    if len(contabilidade["lacunas"]) <= 10:
        print(f"   • Lacunas: {contabilidade['lacunas']}")
else:
    print(f"   • ✅ SEQUÊNCIA CONTÍNUA ATÉ EQ{max(todas_equacoes):04d}")

print(f"\n🔄 DUPLICATAS ENTRE BIBLIOTECAS:")
if contabilidade["duplicatas"]:
    print(f"   • {len(contabilidade['duplicatas'])} equações duplicadas")
    for num_eq, bibs in list(contabilidade["duplicatas"].items())[:5]:
        print(f"      • EQ{num_eq:04d}: {len(bibs)} bibliotecas")
else:
    print(f"   • ✅ NENHUMA DUPLICATA CRÍTICA")

# VERIFICAÇÃO DE INTEGRIDADE
print(f"\n🔧 VERIFICAÇÃO DE INTEGRIDADE:")
print(f"   • Equações únicas: {contabilidade['total_equacoes_unicas']}")
print(f"   • Soma por biblioteca: {sum(dados['total'] for dados in contabilidade['equacoes_por_biblioteca'].values())}")
print(f"   • Diferença (duplicatas): {sum(dados['total'] for dados in contabilidade['equacoes_por_biblioteca'].values()) - contabilidade['total_equacoes_unicas']}")

# RECOMENDAÇÕES PRECISAS
print(f"\n💡 RECOMENDAÇÕES PRECISAS:")
print(f"   1. Consolidar todas em BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
print(f"   2. Eliminar {len(contabilidade['duplicatas'])} duplicatas")
print(f"   3. Processar próxima equação: EQ{max(todas_equacoes)+1:04d}")
print(f"   4. Alcançar {contabilidade['total_equacoes_unicas'] + 4} equações para meta 150")

print(f"\n🌌 STATUS FINAL PRECISO:")
print(f"   'Temos EXATAMENTE {contabilidade['total_equacoes_unicas']} equações únicas'")
print(f"   'Progresso: {contabilidade['total_equacoes_unicas']/230*100:.2f}%'")
print(f"   'Próxima: EQ{max(todas_equacoes)+1:04d}'")
print(f"   'Meta 150: {150 - contabilidade['total_equacoes_unicas']} equações faltantes'")
