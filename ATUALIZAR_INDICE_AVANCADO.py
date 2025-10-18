#!/usr/bin/env python3
"""
ATUALIZADOR DO ÍNDICE COM SEQUÊNCIA AVANÇADA ATÉ EQ154
"""

from pathlib import Path
import json
import re

print("📈 ATUALIZANDO ÍNDICE COM SEQUÊNCIA AVANÇADA")
print("=" * 55)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"

# Contagem da sequência avançada
arquivos = list(equacoes_dir.glob("EQ*.json"))
total_atual = len(arquivos)

print(f"📊 CONTAGEM DA SEQUÊNCIA AVANÇADA:")
print(f"   • Equações na biblioteca: {total_atual}")
print(f"   • Progresso: {total_atual}/230 ({total_atual/230*100:.2f}%)")

# Coletar números para análise avançada
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
    print(f"   • Últimas 8 equações: {numeros_eq[-8:]}")

# Criar índice avançado
indice_avancado = {
    "timestamp_atualizacao_avancada": "2024-01-19T15:00:00Z",
    "total_equacoes": total_atual,
    "progresso_global": f"{total_atual}/230 ({total_atual/230*100:.2f}%)",
    "sequencia_avancada_ate": f"EQ{max(numeros_eq):04d}" if numeros_eq else "N/A",
    "proxima_equacao": f"EQ{max(numeros_eq)+1:04d}" if numeros_eq else "EQ0001",
    "crise_escala_resolvida": all(eq in numeros_eq for eq in [152, 153, 154]),
    "evolucao_unificacao": {
        "EQ152": "Somatório Problemático",
        "EQ153": "Produto como Solução", 
        "EQ154": "Produto Tensorial Definitivo"
    },
    "faixas_avancadas": {},
    "marcos_estrategicos": {}
}

# Organizar por faixas avançadas
faixas = [
    (1, 50, "Fundação Básica"),
    (51, 100, "Expansão Quântica"), 
    (101, 145, "Consolidação Dimensional"),
    (146, 151, "Correções e Estabilização"),
    (152, 154, "Resolução Crise de Escala"),
    (155, 230, "Expansão Final")
]

for inicio, fim, descricao in faixas:
    equacoes_na_faixa = [eq for eq in numeros_eq if inicio <= eq <= fim]
    completude = len(equacoes_na_faixa) / (fim - inicio + 1) * 100 if (fim - inicio + 1) > 0 else 0
    
    indice_avancado["faixas_avancadas"][f"EQ{inicio:04d}-EQ{fim:04d}"] = {
        "total": len(equacoes_na_faixa),
        "maximo": fim - inicio + 1,
        "completude": f"{completude:.1f}%",
        "descricao": descricao,
        "status": "✅ COMPLETA" if completude == 100 else "🔄 EM ANDAMENTO"
    }

# Marcos estratégicos
indice_avancado["marcos_estrategicos"] = {
    "EQ050": "25% - Fundação Básica",
    "EQ100": "50% - Expansão Quântica", 
    "EQ150": "65.2% - Unificação Cósmica",
    "EQ154": "67.0% - Crise de Escala Resolvida",
    "EQ200": "87.0% - Realização Avançada",
    "EQ230": "100% - Missão Cumprida"
}

# Salvar índice avançado
arquivo_indice = biblioteca_central / "INDICE_AVANCADO.json"
with open(arquivo_indice, 'w', encoding='utf-8') as f:
    json.dump(indice_avancado, f, indent=2, ensure_ascii=False)

print(f"✅ Índice avançado salvo: {arquivo_indice}")

# Status estratégico
print(f"\n🎯 STATUS ESTRATÉGICO:")
for faixa, dados in indice_avancado["faixas_avancadas"].items():
    print(f"   • {faixa}: {dados['total']}/{dados['maximo']} ({dados['completude']}) - {dados['status']}")

print(f"\n🏆 MARCOS ALCANÇADOS:")
for marco, descricao in indice_avancado["marcos_estrategicos"].items():
    num_marco = int(marco[2:])
    status = "✅" if num_marco <= max(numeros_eq) else "🎯"
    print(f"   {status} {marco}: {descricao}")

print(f"\n🌌 VISÃO ESTRATÉGICA AVANÇADA:")
print(f"   'Progresso cósmico: {total_atual/230*100:.2f}%'")
print(f"   'Crise de escala: {'✅ RESOLVIDA' if indice_avancado['crise_escala_resolvida'] else '🔄 EM ANDAMENTO'}'")
print(f"   'Unificação: EQ152→EQ153→EQ154 → COMPLETA'")
print(f"   'Próxima fronteira: EQ{max(numeros_eq)+1:04d}'")
