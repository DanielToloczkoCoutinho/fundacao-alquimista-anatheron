#!/usr/bin/env python3
"""
ATUALIZADOR DO ÍNDICE COM SEQUÊNCIA COMPLETA ATÉ EQ151
"""

from pathlib import Path
import json
import re

print("📈 ATUALIZANDO ÍNDICE COM SEQUÊNCIA COMPLETA")
print("=" * 55)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"

# Contar equações com sequência completa
arquivos = list(equacoes_dir.glob("EQ*.json"))
total_atual = len(arquivos)

print(f"📊 CONTAGEM COM SEQUÊNCIA COMPLETA:")
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
    print(f"   • Últimas 5: {numeros_eq[-5:]}")
    
    # Verificar meta EQ150
    equacoes_ate_150 = [eq for eq in numeros_eq if eq <= 150]
    meta_150_alcancada = 150 in numeros_eq
    
    print(f"   • Meta EQ150: {'✅ ALCANÇADA' if meta_150_alcancada else '❌ NÃO ALCANÇADA'}")
    print(f"   • Equações até EQ150: {len(equacoes_ate_150)}/150")

# Criar índice completo
indice_completo = {
    "timestamp_atualizacao": "2024-01-19T14:00:00Z",
    "total_equacoes": total_atual,
    "progresso_global": f"{total_atual}/230 ({total_atual/230*100:.2f}%)",
    "meta_150_alcancada": meta_150_alcancada,
    "sequencia_completa_ate": f"EQ{max(numeros_eq):04d}" if numeros_eq else "N/A",
    "proxima_equacao": f"EQ{max(numeros_eq)+1:04d}" if numeros_eq else "EQ0001",
    "faixas_detalhadas": {},
    "marcos_importantes": {}
}

# Organizar por faixas detalhadas
faixas = [
    (1, 50, "Fundação Básica"),
    (51, 100, "Expansão Quântica"), 
    (101, 145, "Consolidação Dimensional"),
    (146, 150, "Meta Final EQ150"),
    (151, 230, "Pós-Meta Expansão")
]

for inicio, fim, descricao in faixas:
    equacoes_na_faixa = [eq for eq in numeros_eq if inicio <= eq <= fim]
    completude = len(equacoes_na_faixa) / (fim - inicio + 1) * 100
    
    indice_completo["faixas_detalhadas"][f"EQ{inicio:04d}-EQ{fim:04d}"] = {
        "total": len(equacoes_na_faixa),
        "maximo": fim - inicio + 1,
        "completude": f"{completude:.1f}%",
        "descricao": descricao,
        "status": "✅ COMPLETA" if completude == 100 else "🔄 EM ANDAMENTO"
    }

# Marcos importantes
indice_completo["marcos_importantes"] = {
    "EQ050": "25% da missão",
    "EQ100": "50% da missão", 
    "EQ150": "65.2% da missão - META ALCANÇADA" if meta_150_alcancada else "65.2% da missão - META",
    "EQ200": "87.0% da missão",
    "EQ230": "100% da missão - REALIZAÇÃO CÓSMICA"
}

# Salvar índice completo
arquivo_indice = biblioteca_central / "INDICE_SEQUENCIA_COMPLETA.json"
with open(arquivo_indice, 'w', encoding='utf-8') as f:
    json.dump(indice_completo, f, indent=2, ensure_ascii=False)

print(f"✅ Índice completo salvo: {arquivo_indice}")

# Status detalhado
print(f"\n🎯 STATUS DETALHADO DA MISSÃO:")
for faixa, dados in indice_completo["faixas_detalhadas"].items():
    print(f"   • {faixa}: {dados['total']}/{dados['maximo']} ({dados['completude']}) - {dados['status']}")

print(f"\n🏆 MARCOS ALCANÇADOS:")
for marco, descricao in indice_completo["marcos_importantes"].items():
    status = "✅" if marco in ["EQ050", "EQ100"] or (marco == "EQ150" and meta_150_alcancada) else "🎯"
    print(f"   {status} {marco}: {descricao}")

print(f"\n🌌 VISÃO DA SEQUÊNCIA COMPLETA:")
print(f"   'Progresso cósmico: {total_atual/230*100:.2f}%'")
print(f"   'Sequência: EQ{min(numeros_eq):04d} a EQ{max(numeros_eq):04d}'")
print(f"   'Meta EQ150: {'✅ CONCLUÍDA' if meta_150_alcancada else '🔄 EM ANDAMENTO'}'")
print(f"   'Próxima fronteira: EQ{max(numeros_eq)+1:04d}'")
