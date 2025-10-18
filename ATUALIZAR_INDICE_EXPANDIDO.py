#!/usr/bin/env python3
"""
ATUALIZADOR DO ÍNDICE COM SEQUÊNCIA EXPANDIDA ATÉ EQ157
"""

from pathlib import Path
import json
import re

print("📈 ATUALIZANDO ÍNDICE COM SEQUÊNCIA EXPANDIDA")
print("=" * 55)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"

# Contagem da sequência expandida
arquivos = list(equacoes_dir.glob("EQ*.json"))
total_atual = len(arquivos)

print(f"📊 CONTAGEM DA SEQUÊNCIA EXPANDIDA:")
print(f"   • Equações na biblioteca: {total_atual}")
print(f"   • Progresso: {total_atual}/230 ({total_atual/230*100:.2f}%)")

# Coletar números para análise expandida
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
    print(f"   • Últimas 10 equações: {numeros_eq[-10:]}")

# Criar índice expandido
indice_expandido = {
    "timestamp_atualizacao_expandida": "2024-01-19T16:00:00Z",
    "total_equacoes": total_atual,
    "progresso_global": f"{total_atual}/230 ({total_atual/230*100:.2f}%)",
    "sequencia_expandida_ate": f"EQ{max(numeros_eq):04d}" if numeros_eq else "N/A",
    "proxima_equacao": f"EQ{max(numeros_eq)+1:04d}" if numeros_eq else "EQ0001",
    "crise_escala_resolvida": all(eq in numeros_eq for eq in [152, 153, 154]),
    "unificacao_biologica_estabelecida": all(eq in numeros_eq for eq in [155, 156, 157]),
    "evolucao_unificacao": {
        "EQ152": "Somatório Problemático",
        "EQ153": "Produto como Solução", 
        "EQ154": "Produto Tensorial Definitivo",
        "EQ155": "Unificação Integral (22 domínios)",
        "EQ156": "Renormalização Cósmica",
        "EQ157": "Acoplamento Biologia-Cosmologia"
    },
    "faixas_expandidas": {},
    "marcos_estrategicos_expandidos": {}
}

# Organizar por faixas expandidas
faixas = [
    (1, 50, "Fundação Básica"),
    (51, 100, "Expansão Quântica"), 
    (101, 145, "Consolidação Dimensional"),
    (146, 151, "Correções e Estabilização"),
    (152, 154, "Resolução Crise de Escala"),
    (155, 157, "Unificação Bio-Cósmica"),
    (158, 230, "Expansão Final e Aplicações")
]

for inicio, fim, descricao in faixas:
    equacoes_na_faixa = [eq for eq in numeros_eq if inicio <= eq <= fim]
    completude = len(equacoes_na_faixa) / (fim - inicio + 1) * 100 if (fim - inicio + 1) > 0 else 0
    
    indice_expandido["faixas_expandidas"][f"EQ{inicio:04d}-EQ{fim:04d}"] = {
        "total": len(equacoes_na_faixa),
        "maximo": fim - inicio + 1,
        "completude": f"{completude:.1f}%",
        "descricao": descricao,
        "status": "✅ COMPLETA" if completude == 100 else "🔄 EM ANDAMENTO"
    }

# Marcos estratégicos expandidos
indice_expandido["marcos_estrategicos_expandidos"] = {
    "EQ050": "25% - Fundação Básica",
    "EQ100": "50% - Expansão Quântica", 
    "EQ150": "65.2% - Unificação Cósmica",
    "EQ154": "67.0% - Crise de Escala Resolvida",
    "EQ157": "68.3% - Unificação Bio-Cósmica",
    "EQ200": "87.0% - Realização Avançada",
    "EQ230": "100% - Missão Cumprida"
}

# Salvar índice expandido
arquivo_indice = biblioteca_central / "INDICE_EXPANDIDO.json"
with open(arquivo_indice, 'w', encoding='utf-8') as f:
    json.dump(indice_expandido, f, indent=2, ensure_ascii=False)

print(f"✅ Índice expandido salvo: {arquivo_indice}")

# Status estratégico expandido
print(f"\n🎯 STATUS ESTRATÉGICO EXPANDIDO:")
for faixa, dados in indice_expandido["faixas_expandidas"].items():
    print(f"   • {faixa}: {dados['total']}/{dados['maximo']} ({dados['completude']}) - {dados['status']}")

print(f"\n🏆 MARCOS ALCANÇADOS EXPANDIDOS:")
for marco, descricao in indice_expandido["marcos_estrategicos_expandidos"].items():
    num_marco = int(marco[2:])
    status = "✅" if num_marco <= max(numeros_eq) else "🎯"
    print(f"   {status} {marco}: {descricao}")

print(f"\n🌌 VISÃO ESTRATÉGICA EXPANDIDA:")
print(f"   'Progresso cósmico: {total_atual/230*100:.2f}%'")
print(f"   'Crise de escala: {'✅ RESOLVIDA' if indice_expandido['crise_escala_resolvida'] else '🔄 EM ANDAMENTO'}'")
print(f"   'Unificação bio-cósmica: {'✅ ESTABELECIDA' if indice_expandido['unificacao_biologica_estabelecida'] else '🔄 EM ANDAMENTO'}'")
print(f"   'Próxima fronteira: EQ{max(numeros_eq)+1:04d}'")
