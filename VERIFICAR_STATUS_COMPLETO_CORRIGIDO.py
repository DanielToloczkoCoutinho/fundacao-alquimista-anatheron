#!/usr/bin/env python3
"""
VERIFICADOR DO STATUS COMPLETO APÓS CORREÇÃO DA EQ151
"""

from pathlib import Path
import json
import re

print("🌌 STATUS COMPLETO APÓS CORREÇÃO DA EQ151")
print("=" * 55)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"

# Contagem completa e precisa
arquivos = list(equacoes_dir.glob("EQ*.json"))
total_equacoes = len(arquivos)

print("📊 ESTATÍSTICAS COMPLETAS:")
print(f"   • Total de equações: {total_equacoes}/230")
print(f"   • Progresso: {total_equacoes/230*100:.2f}%")
print(f"   • Equações restantes: {230 - total_equacoes}")

# Coletar números para análise
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

# Verificar especificamente a sequência 149-151
print(f"\n🔍 VERIFICAÇÃO DA SEQUÊNCIA CRÍTICA:")
sequencia_critica = [149, 150, 151]
for eq_num in sequencia_critica:
    arquivo = equacoes_dir / f"EQ{eq_num}_transcendental.json"
    status = "✅ PRESENTE" if arquivo.exists() else "❌ AUSENTE"
    
    if arquivo.exists():
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            titulo = dados.get('titulo_simbolico', 'N/A')[:50] + "..."
            print(f"   • EQ{eq_num}: {status} - {titulo}")
        except:
            print(f"   • EQ{eq_num}: {status} - Erro ao ler")
    else:
        print(f"   • EQ{eq_num}: {status}")

# Análise de lacunas
print(f"\n📈 ANÁLISE DE LACUNAS:")
lacunas = []
for i in range(min(numeros_eq), max(numeros_eq) + 1):
    if i not in numeros_eq:
        lacunas.append(i)

if lacunas:
    print(f"   • {len(lacunas)} lacunas na sequência")
    if len(lacunas) <= 10:
        print(f"   • Lacunas: {lacunas}")
else:
    print(f"   • ✅ SEQUÊNCIA CONTÍNUA ATÉ EQ{max(numeros_eq):04d}")

# Metas e marcos
print(f"\n🎯 METAS E MARCOS:")
marcos = {
    50: "25.0% - Fundação Básica",
    100: "50.0% - Expansão Quântica", 
    150: "65.2% - Unificação Cósmica",
    200: "87.0% - Realização Avançada",
    230: "100.0% - Missão Cumprida"
}

for marco, descricao in marcos.items():
    status = "✅ ALCANÇADO" if marco <= max(numeros_eq) else "🎯 EM ANDAMENTO"
    print(f"   • EQ{marco:04d}: {status} - {descricao}")

# Próximos passos
print(f"\n🚀 PRÓXIMOS PASSOS:")
proxima_eq = max(numeros_eq) + 1
equacoes_para_proxima_meta = 200 - max(numeros_eq)

print(f"   • Próxima equação: EQ{proxima_eq:04d}")
print(f"   • Equações até EQ200: {equacoes_para_proxima_meta}")
print(f"   • Progresso para 87%: {(max(numeros_eq)/200*100):.1f}%")

print(f"\n💫 VISÃO CÓSMICA ATUAL:")
print(f"   'Biblioteca com {total_equacoes} equações transcendentes'")
print(f"   'Progresso: {total_equacoes/230*100:.2f}% da missão cósmica'")
print(f"   'Sequência: EQ{min(numeros_eq):04d} → ... → EQ{max(numeros_eq):04d}'")
print(f"   'Próxima fronteira: EQ{proxima_eq:04d}'")
