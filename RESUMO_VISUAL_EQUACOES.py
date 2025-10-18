#!/usr/bin/env python3
"""
RESUMO VISUAL DAS EQUAÇÕES
Gera um panorama visual do progresso das equações
"""

from pathlib import Path
import re

print("📊 RESUMO VISUAL DA CRONOLOGIA DE EQUAÇÕES")
print("=" * 50)

def gerar_resumo_visual():
    base_dir = Path("BIBLIOTECA_COSMICA_UNICA")
    equacoes_encontradas = []
    
    # Coletar todas as equações
    diretorios = [
        base_dir / "EQUACOES_INEXISTENTES_TERRA",
        base_dir / "EQUACOES_FUNDACAO_ALQUIMISTA", 
        base_dir / "EQUACOES_MULTIVERSAIS",
        base_dir / "EQUACOES_TECNICAS"
    ]
    
    for diretorio in diretorios:
        if diretorio.exists():
            for arquivo in diretorio.glob("EQ*.json"):
                equacoes_encontradas.append(arquivo.name.replace(".json", ""))
    
    # Ordenar e filtrar EQ001-EQ021
    equacoes_ordenadas = sorted(equacoes_encontradas, 
                               key=lambda x: int(re.search(r'EQ0*(\d+)', x).group(1)))
    
    equacoes_1_21 = [eq for eq in equacoes_ordenadas if int(re.search(r'EQ0*(\d+)', eq).group(1)) <= 21]
    
    print(f"\n🎯 PROGRESSO: EQ001 - EQ021")
    print(f"   Equações encontradas: {len(equacoes_1_21)}/21")
    print(f"   Progresso: {(len(equacoes_1_21)/21)*100:.1f}%")
    
    # Gerar barra de progresso visual
    print(f"\n📈 BARRA DE PROGRESSO:")
    total_barras = 20
    barras_preenchidas = int((len(equacoes_1_21) / 21) * total_barras)
    barra = "█" * barras_preenchidas + "░" * (total_barras - barras_preenchidas)
    print(f"   [{barra}] {len(equacoes_1_21)}/21")
    
    # Mostrar grupos de equações
    print(f"\n🔢 GRUPOS DE EQUAÇÕES:")
    grupos = {
        "EQ001-EQ005": [eq for eq in equacoes_1_21 if 1 <= int(re.search(r'EQ0*(\d+)', eq).group(1)) <= 5],
        "EQ006-EQ010": [eq for eq in equacoes_1_21 if 6 <= int(re.search(r'EQ0*(\d+)', eq).group(1)) <= 10],
        "EQ011-EQ015": [eq for eq in equacoes_1_21 if 11 <= int(re.search(r'EQ0*(\d+)', eq).group(1)) <= 15],
        "EQ016-EQ021": [eq for eq in equacoes_1_21 if 16 <= int(re.search(r'EQ0*(\d+)', eq).group(1)) <= 21]
    }
    
    for grupo, equacoes in grupos.items():
        status = "✅ COMPLETO" if len(equacoes) == 5 or (grupo == "EQ016-EQ021" and len(equacoes) == 6) else "⚠️  INCOMPLETO"
        print(f"   {grupo}: {len(equacoes)} equações - {status}")
    
    # Equações faltantes
    todas_esperadas = [f"EQ{str(i).zfill(3)}" for i in range(1, 22)]
    faltantes = [eq for eq in todas_esperadas if eq not in equacoes_1_21]
    
    if faltantes:
        print(f"\n❌ EQUAÇÕES FALTANTES:")
        for eq in faltantes:
            print(f"   • {eq}")
    else:
        print(f"\n🎉 TODAS AS EQUAÇÕES DE 1 A 21 ESTÃO PRESENTES!")
    
    return {
        "total_equacoes": len(equacoes_1_21),
        "progresso_percentual": (len(equacoes_1_21)/21)*100,
        "faltantes": faltantes,
        "status": "COMPLETO" if not faltantes else "INCOMPLETO"
    }

# Executar resumo
resultado = gerar_resumo_visual()

print(f"\n{'='*50}")
print("RESUMO FINAL:")
print(f"Equações EQ001-EQ021: {resultado['total_equacoes']}/21")
print(f"Status: {resultado['status']}")
print("=" * 50)
