#!/usr/bin/env python3
"""Verificador da sequência avançada EQ155-EQ159"""

from pathlib import Path
import json

print("🔍 VERIFICANDO SEQUÊNCIA AVANÇADA EQ155-EQ159")
print("=" * 50)

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = base_dir / "EQUACOES_TRANSCENDENTAIS"

sequencia = list(range(155, 160))  # EQ155 a EQ159
encontradas = []
detalhes = []

for num in sequencia:
    arquivo = equacoes_dir / f"EQ{num}_transcendental.json"
    if arquivo.exists():
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            codigo = dados.get('codigo', 'N/A')
            titulo = dados.get('titulo_simbolico', 'N/A')
            coerencia = dados.get('validacao_ressonancia', {}).get('coerencia', 0)
            
            encontradas.append(num)
            detalhes.append({
                'eq': num,
                'coerencia': coerencia,
                'titulo': titulo[:60] + '...' if len(titulo) > 60 else titulo
            })
            
            print(f"✅ EQ{num} - Coerência: {coerencia}")
            
        except Exception as e:
            print(f"❌ EQ{num} - ERRO: {e}")
    else:
        print(f"❌ EQ{num} - AUSENTE")

print(f"\n📊 RESUMO DA SEQUÊNCIA:")
print(f"   • Período: EQ155 a EQ159")
print(f"   • Encontradas: {len(encontradas)}/5")
print(f"   • Completa: {'✅ SIM' if len(encontradas) == 5 else '❌ NÃO'}")

if detalhes:
    print(f"\n🎯 DETALHES:")
    for det in detalhes:
        print(f"   • EQ{det['eq']}: {det['coerencia']} - {det['titulo']}")

# Estatísticas
arquivos_todos = list(equacoes_dir.glob("EQ*.json"))
total_eq = len(arquivos_todos)

print(f"\n🌌 VISÃO GERAL:")
print(f"   • Total de equações: {total_eq}/230 ({total_eq/230*100:.2f}%)")
print(f"   • Próxima equação: EQ{max(encontradas) + 1 if encontradas else 155}")
print(f"   • Estado: {'✅ AVANÇADO' if len(encontradas) >= 4 else '🔄 EM DESENVOLVIMENTO'}")

if len(encontradas) == 5:
    print(f"\n🚀 SEQUÊNCIA AVANÇADA COMPLETA!")
    print(f"   'Trilogia bio-cósmica → Controle total → Sustentação'")
    print(f"   'Sistema pronto para execução prática'")
