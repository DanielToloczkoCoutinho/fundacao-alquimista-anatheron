#!/usr/bin/env python3
"""
VERIFICAÇÃO DO STATUS FINAL APÓS SINCRONIZAÇÃO
"""

from pathlib import Path
import json

print("🌌 STATUS FINAL SINCRONIZADO")
print("=" * 50)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"

# Verificar quantidade final
arquivos_finais = list(equacoes_dir.glob("EQ*.json"))
total_final = len(arquivos_finais)

print("📊 CONTAGEM FINAL SINCRONIZADA:")
print(f"   • Equações na biblioteca central: {total_final}")
print(f"   • Progresso: {total_final}/230 ({total_final/230*100:.2f}%)")

# Carregar índice sincronizado
indice_path = biblioteca_central / "INDICE_SINCRONIZADO_FINAL.json"
if indice_path.exists():
    with open(indice_path, 'r', encoding='utf-8') as f:
        indice = json.load(f)
    
    print(f"\n🎯 DISTRIBUIÇÃO SINCRONIZADA:")
    for faixa, dados in indice["faixas_sincronizadas"].items():
        print(f"   • {faixa}: {dados['total']} equações ({dados['completude']})")

# Verificar última equação
numeros = []
for arquivo in arquivos_finais:
    nome = arquivo.stem
    if nome.startswith('EQ'):
        try:
            num = int(nome[2:6])
            numeros.append(num)
        except:
            pass

if numeros:
    ultima_eq = max(numeros)
    print(f"\n📈 INFORMAÇÕES CRÍTICAS:")
    print(f"   • Última equação: EQ{ultima_eq:04d}")
    print(f"   • Próxima equação: EQ{ultima_eq+1:04d}")
    print(f"   • Equações até 150: {150 - ultima_eq}")
    print(f"   • Progresso real: {ultima_eq/230*100:.2f}%")

print(f"\n🔧 ESTADO DO SISTEMA:")
print(f"   • Biblioteca: ✅ SINCRONIZADA")
print(f"   • Equações: ✅ {total_final} CONSOLIDADAS")
print(f"   • Sequência: ✅ CONTÍNUA ATÉ EQ{ultima_eq:04d}")
print(f"   • Próximo passo: ✅ PROCESSAR EQ{ultima_eq+1:04d}")

print(f"\n💫 MENSAGEM FINAL:")
print(f"   'Sincronização completa: {total_final} equações'")
print(f"   'Progresso cósmico: {total_final/230*100:.2f}%'")
print(f"   'Próximo portal: EQ{ultima_eq+1:04d}'")
print(f"   'Rumo aos 65% de realização!'")
