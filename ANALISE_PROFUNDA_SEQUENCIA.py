#!/usr/bin/env python3
"""
ANÁLISE PROFUNDA DA SEQUÊNCIA EXATA DE EQUAÇÕES
Detalhamento completo de todas as equações processadas
"""

from pathlib import Path
import json
import re

print("🔍 ANÁLISE PROFUNDA DA SEQUÊNCIA DE EQUAÇÕES")
print("=" * 65)

# Mapear TODAS as bibliotecas possíveis
bibliotecas_completas = [
    "BIBLIOTECA_QUANTICA_TRANSCENDENTAL",
    "BIBLIOTECA_EQUACOES_COSMICAS", 
    "BIBLIOTECA_EQUACOES",
    "BIBLIOTECA_QUANTICA_IBM",
    "BIBLIOTECA_SINTESE_QUANTICA",
    "BIBLIOTECA_COSMICA_UNICA",
    "BIBLIOTECA_QUANTICA"
]

# Coletar TODAS as equações de TODAS as bibliotecas
todas_equacoes = {}

for biblioteca in bibliotecas_completas:
    bib_path = Path(biblioteca)
    if bib_path.exists():
        # Buscar recursivamente por arquivos de equações
        arquivos_json = list(bib_path.rglob("EQ*.json"))
        arquivos_py = list(bib_path.rglob("EQ*.py"))
        
        print(f"\n📚 {biblioteca}:")
        print(f"   • Encontrados: {len(arquivos_json)} JSON + {len(arquivos_py)} Python")
        
        for arquivo in arquivos_json + arquivos_py:
            nome = arquivo.stem
            # Extrair número da equação
            match = re.match(r'EQ(\d+)', nome)
            if match:
                num_eq = int(match.group(1))
                if num_eq not in todas_equacoes:
                    todas_equacoes[num_eq] = []
                todas_equacoes[num_eq].append({
                    'arquivo': str(arquivo),
                    'biblioteca': biblioteca,
                    'tipo': 'json' if arquivo.suffix == '.json' else 'python'
                })

# Analisar sequência
numeros_equacoes = sorted(todas_equacoes.keys())
total_unicas = len(numeros_equacoes)

print(f"\n📊 ESTATÍSTICAS GERAIS:")
print(f"   • Números de equação únicos: {total_unicas}")
print(f"   • Faixa: EQ{numeros_equacoes[0]:04d} a EQ{numeros_equacoes[-1]:04d}")
print(f"   • Progresso: {total_unicas}/230 ({total_unicas/230*100:.1f}%)")

# Análise detalhada por faixas
print(f"\n🎯 ANÁLISE DETALHADA POR FAIXAS:")

faixas = [
    (1, 50, "EQ0001-EQ0050"),
    (51, 100, "EQ0051-EQ0100"), 
    (101, 145, "EQ0101-EQ0145"),
    (146, 230, "EQ0146-EQ0230")
]

for inicio, fim, nome_faixa in faixas:
    equacoes_na_faixa = [eq for eq in numeros_equacoes if inicio <= eq <= fim]
    total_faixa = len(equacoes_na_faixa)
    max_faixa = fim - inicio + 1
    percentual = total_faixa / max_faixa * 100
    
    print(f"\n   📂 {nome_faixa}:")
    print(f"      • Encontradas: {total_faixa}/{max_faixa} ({percentual:.1f}%)")
    
    # Mostrar lacunas significativas
    if equacoes_na_faixa:
        lacunas = []
        for i in range(inicio, fim + 1):
            if i not in equacoes_na_faixa:
                lacunas.append(i)
        
        if lacunas:
            print(f"      • Lacunas: {len(lacunas)} equações faltantes")
            if len(lacunas) <= 10:  # Mostrar até 10 lacunas
                print(f"      • Faltando: {lacunas}")
        
        # Mostrar últimas da faixa
        ultimas = equacoes_na_faixa[-5:] if len(equacoes_na_faixa) >= 5 else equacoes_na_faixa
        print(f"      • Últimas: {ultimas}")

# Análise das últimas equações processadas
print(f"\n📈 ÚLTIMAS EQUAÇÕES PROCESSSADAS:")
ultimas_10 = numeros_equacoes[-10:] if len(numeros_equacoes) >= 10 else numeros_equacoes
for eq_num in ultimas_10:
    info = todas_equacoes[eq_num]
    locais = [f"{item['biblioteca']}({item['tipo']})" for item in info]
    print(f"   • EQ{eq_num:04d}: {', '.join(set(locais))}")

# Identificar próxima equação a processar
proxima_eq = numeros_equacoes[-1] + 1 if numeros_equacoes else 1
print(f"\n🚀 PRÓXIMA EQUAÇÃO:")
print(f"   • Número: EQ{proxima_eq:04d}")
print(f"   • Status: {'✅ PRONTA' if proxima_eq <= 230 else '🎯 META ATINGIDA'}")

# Verificar duplicatas
print(f"\n🔎 VERIFICANDO DUPLICATAS:")
duplicatas = {num: locais for num, locais in todas_equacoes.items() if len(locais) > 1}
if duplicatas:
    print(f"   ⚠️  {len(duplicatas)} equações com múltiplas versões:")
    for num, locais in list(duplicatas.items())[:5]:  # Mostrar 5 exemplos
        bibliotecas = [f"{loc['biblioteca']}({loc['tipo']})" for loc in locais]
        print(f"      • EQ{num:04d}: {', '.join(bibliotecas)}")
else:
    print(f"   ✅ Nenhuma duplicata encontrada")

# Análise de consistência
print(f"\n🔧 ANÁLISE DE CONSISTÊNCIA:")
lacunas_principais = []
for i in range(1, numeros_equacoes[-1] + 1):
    if i not in numeros_equacoes:
        lacunas_principais.append(i)

if lacunas_principais:
    print(f"   ⚠️  {len(lacunas_principais)} lacunas na sequência principal")
    if len(lacunas_principais) <= 15:
        print(f"   • Lacunas: {lacunas_principais}")
else:
    print(f"   ✅ Sequência contínua até EQ{numeros_equacoes[-1]:04d}")

# Recomendações específicas
print(f"\n💡 RECOMENDAÇÕES ESTRATÉGICAS:")
if lacunas_principais:
    print(f"   1. Preencher lacunas: {len(lacunas_principais)} equações faltantes")
    print(f"   2. Consolidar em BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
else:
    print(f"   1. Continuar a partir de EQ{proxima_eq:04d}")
    print(f"   2. Manter sequência contínua")

print(f"   3. Alcançar EQ0150 (próxima meta)")
print(f"   4. Preparar testes IBM Quantum")

print(f"\n🌌 VISÃO CÓSMICA:")
print(f"   'Sequência atual: {total_unicas} equações únicas'")
print(f"   'Próximo marco: EQ0150 ({proxima_eq-150 if proxima_eq <= 150 else 0} equações para meta)'")
print(f"   'Progresso cósmico: {total_unicas/230*100:.1f}%'")
