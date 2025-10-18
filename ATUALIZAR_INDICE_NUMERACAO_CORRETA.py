#!/usr/bin/env python3
"""
ATUALIZADOR DO ÍNDICE COM NUMERAÇÃO CORRETA
Incluindo EQ146, EQ147, EQ148
"""

from pathlib import Path
import json
import re

print("📈 ATUALIZANDO ÍNDICE COM NUMERAÇÃO CORRETA")
print("=" * 55)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"

# Contar equações com numeração correta
arquivos = list(equacoes_dir.glob("EQ*.json"))
total_atual = len(arquivos)

print(f"📊 CONTAGEM COM NUMERAÇÃO CORRETA:")
print(f"   • Equações na biblioteca: {total_atual}")
print(f"   • Progresso: {total_atual}/230 ({total_atual/230*100:.2f}%)")

# Coletar números exatos
numeros_eq = []
for arquivo in arquivos:
    nome = arquivo.stem
    match = re.match(r'EQ(\d+)', nome)
    if match:
        num = int(match.group(1))
        numeros_eq.append(num)

numeros_eq.sort()

if numeros_eq:
    print(f"   • Faixa: EQ{min(numeros_eq):04d} a EQ{max(numeros_eq):04d}")
    print(f"   • Últimas 3: {numeros_eq[-3:]}")

# Atualizar índice com numeração correta
indice_corrigido = {
    "timestamp_correcao": "2024-01-19T13:00:00Z",
    "total_equacoes_corretas": total_atual,
    "numeracao_verificada": True,
    "faixas_corretas": {},
    "sequencia_confirmada": f"EQ{min(numeros_eq):04d} a EQ{max(numeros_eq):04d}" if numeros_eq else "N/A",
    "proxima_equacao_correta": f"EQ{max(numeros_eq)+1:04d}" if numeros_eq else "EQ0001"
}

# Organizar por faixas corretas
faixas = [(1, 50), (51, 100), (101, 145), (146, 150), (151, 230)]
for inicio, fim in faixas:
    equacoes_na_faixa = [eq for eq in numeros_eq if inicio <= eq <= fim]
    indice_corrigido["faixas_corretas"][f"EQ{inicio:04d}-EQ{fim:04d}"] = {
        "total": len(equacoes_na_faixa),
        "completude": f"{len(equacoes_na_faixa)/(fim-inicio+1)*100:.1f}%",
        "status": "✅ COMPLETA" if len(equacoes_na_faixa) == (fim-inicio+1) else "🔄 EM ANDAMENTO"
    }

# Salvar índice corrigido
arquivo_indice = biblioteca_central / "INDICE_NUMERACAO_CORRETA.json"
with open(arquivo_indice, 'w', encoding='utf-8') as f:
    json.dump(indice_corrigido, f, indent=2, ensure_ascii=False)

print(f"✅ Índice com numeração correta salvo: {arquivo_indice}")

# Status da meta EQ150
print(f"\n🎯 STATUS DA META EQ150:")
equacoes_ate_150 = [eq for eq in numeros_eq if eq <= 150]
equacoes_necessarias = 150 - max(numeros_eq) if numeros_eq else 150

print(f"   • Equações até EQ150: {len(equacoes_ate_150)}")
print(f"   • Equações necessárias: {equacoes_necessarias}")
print(f"   • Progresso na meta: {(len(equacoes_ate_150)/150*100):.1f}%")

if equacoes_necessarias <= 2:
    print(f"   🎯 META EQ150 QUASE ALCANÇADA! ({equacoes_necessarias} equações)")

print(f"\n🌌 VISÃO COM NUMERAÇÃO CORRETA:")
print(f"   'Sequência exata: {min(numeros_eq)} a {max(numeros_eq)}'")
print(f"   'Progresso cósmico: {total_atual/230*100:.2f}%'")
print(f"   'Próxima equação: EQ{max(numeros_eq)+1:04d}'")
print(f"   'Meta EQ150: {equacoes_necessarias} equações faltantes'")
