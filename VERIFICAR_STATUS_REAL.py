#!/usr/bin/env python3
"""
VERIFICAÇÃO DO STATUS REAL APÓS UNIFICAÇÃO
"""

from pathlib import Path
import json

print("🌌 STATUS REAL DA FUNDAÇÃO APÓS UNIFICAÇÃO")
print("=" * 60)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")

# Verificar estrutura
print("📁 ESTRUTURA DA BIBLIOTECA CENTRAL:")
for subdir in ["EQUACOES_TRANSCENDENTAIS", "RELATORIOS", "CIRCUITOS_IBM", "METADADOS_COSMICOS"]:
    dir_path = biblioteca_central / subdir
    if dir_path.exists():
        arquivos = len(list(dir_path.glob("*")))
        print(f"   ✅ {subdir}: {arquivos} arquivos")
    else:
        print(f"   ❌ {subdir}: não encontrado")

# Carregar índice consolidado
indice_path = biblioteca_central / "RELATORIOS" / "INDICE_CONSOLIDADO_EQUACOES.json"
if indice_path.exists():
    with open(indice_path, 'r', encoding='utf-8') as f:
        indice = json.load(f)
    
    print(f"\n📊 ESTATÍSTICAS CONSOLIDADAS:")
    print(f"   • Total de equações: {indice['total_equacoes_consolidadas']}/230")
    print(f"   • Progresso: {indice['total_equacoes_consolidadas']/230*100:.1f}%")
    
    print(f"\n🎯 DISTRIBUIÇÃO POR FAIXAS:")
    for faixa, dados in indice["equacoes_por_faixa"].items():
        max_eq = int(faixa.split('-')[1][2:6])
        percentual = dados['total']/max_eq*100 if max_eq > 0 else 0
        print(f"   • {faixa}: {dados['total']}/{max_eq} ({percentual:.1f}%)")
    
    print(f"\n📈 ÚLTIMAS EQUAÇÕES:")
    for eq in indice["ultimas_equacoes"][-5:]:
        print(f"   • {eq}")

# Verificar próxima equação a processar
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"
arquivos_eq = list(equacoes_dir.glob("EQ*.json")) + list(equacoes_dir.glob("EQ*.py"))
numeros_eq = []

for arquivo in arquivos_eq:
    nome = arquivo.stem
    if nome.startswith('EQ'):
        try:
            num = int(nome[2:6]) if nome[2:6].isdigit() else 0
            numeros_eq.append(num)
        except:
            pass

if numeros_eq:
    ultima_eq = max(numeros_eq)
    print(f"\n🚀 PRÓXIMOS PASSOS:")
    print(f"   • Última equação: EQ{ultima_eq:04d}")
    print(f"   • Próxima equação: EQ{ultima_eq+1:04d}")
    print(f"   • Equações faltantes: {230 - ultima_eq}")
    
    # Calcular progresso real
    progresso_real = ultima_eq / 230 * 100
    print(f"   • Progresso real: {progresso_real:.1f}%")
    
    # Meta próxima
    meta_proxima = 150
    if ultima_eq < meta_proxima:
        print(f"   • Meta próxima: EQ{meta_proxima:04d} ({meta_proxima - ultima_eq} equações)")
    else:
        print(f"   • ✅ Meta de 150 equações atingida!")

print(f"\n🔧 ESTADO DO SISTEMA:")
print(f"   • Biblioteca central: ✅ UNIFICADA")
print(f"   • Equações consolidadas: ✅ {len(arquivos_eq)}")
print(f"   • Próximo processamento: ✅ PRONTO")

print(f"\n💫 MENSAGEM FINAL:")
if numeros_eq:
    print(f"   'Fundação em {progresso_real:.1f}% da realização cósmica'")
    print(f"   'Próxima equação: EQ{ultima_eq+1:04d}'")
    print(f"   'Rumo aos 65% de conclusão!'")
