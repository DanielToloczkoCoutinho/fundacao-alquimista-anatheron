#!/usr/bin/env python3
"""
VERIFICADOR UNIVERSAL DE EQUAÇÕES
Analisa TODAS as bibliotecas para encontrar equações de EQ001 a EQ021
Versão simplificada e robusta
"""

from pathlib import Path
import re

print("VERIFICADOR UNIVERSAL DE EQUAÇÕES")
print("=" * 50)
print("ANALISANDO TODAS AS BIBLIOTECAS EXISTENTES")
print("")

def analisar_todas_bibliotecas():
    """Analisar todas as bibliotecas encontradas"""
    
    # Lista de todas as bibliotecas possíveis
    bibliotecas = [
        "BIBLIOTECA_COSMICA_UNICA",
        "BIBLIOTECA_EQUACOES", 
        "BIBLIOTECA_EQUACOES_COSMICAS",
        "BIBLIOTECA_QUANTICA"
    ]
    
    resultados = {}
    todas_equacoes = []
    
    for biblioteca in bibliotecas:
        if Path(biblioteca).exists():
            print(f"📁 ANALISANDO: {biblioteca}")
            equacoes_encontradas = []
            
            # Procurar em todos os subdiretórios
            for arquivo_json in Path(biblioteca).rglob("EQ*.json"):
                nome_arquivo = arquivo_json.name.replace(".json", "")
                if re.match(r'^EQ\d+', nome_arquivo):
                    equacoes_encontradas.append(nome_arquivo)
            
            # Ordenar numericamente
            equacoes_ordenadas = sorted(equacoes_encontradas, 
                                      key=lambda x: int(re.search(r'(\d+)', x).group(1)))
            
            resultados[biblioteca] = equacoes_ordenadas
            todas_equacoes.extend(equacoes_ordenadas)
            
            print(f"   ✅ Equações encontradas: {len(equacoes_ordenadas)}")
            if equacoes_ordenadas:
                print(f"   📊 Exemplos: {equacoes_ordenadas[:5]}...")
        else:
            print(f"📁 {biblioteca}: Não encontrada")
    
    return resultados, todas_equacoes

def verificar_equacoes_1_a_21(todas_equacoes):
    """Verificar especificamente EQ001 a EQ021"""
    print(f"\n🎯 VERIFICANDO EQ001 A EQ021:")
    
    # Gerar lista esperada
    esperadas = [f"EQ{str(i).zfill(3)}" for i in range(1, 22)]
    
    # Encontrar quais temos
    encontradas = []
    faltantes = []
    
    for eq in esperadas:
        if eq in todas_equacoes:
            encontradas.append(eq)
        else:
            faltantes.append(eq)
    
    print(f"   📈 Progresso: {len(encontradas)}/21 equações")
    print(f"   ✅ Encontradas: {len(encontradas)}")
    print(f"   ❌ Faltantes: {len(faltantes)}")
    
    # Barra de progresso visual
    barras = int((len(encontradas) / 21) * 20)
    barra_visual = "█" * barras + "░" * (20 - barras)
    print(f"   📊 [{barra_visual}] {len(encontradas)}/21")
    
    if encontradas:
        print(f"\n   📋 EQUAÇÕES ENCONTRADAS:")
        for i in range(0, len(encontradas), 5):
            print(f"      {', '.join(encontradas[i:i+5])}")
    
    if faltantes:
        print(f"\n   ⚠️  EQUAÇÕES FALTANTES:")
        for i in range(0, len(faltantes), 5):
            print(f"      {', '.join(faltantes[i:i+5])}")
    
    return {
        "encontradas": encontradas,
        "faltantes": faltantes,
        "progresso": f"{len(encontradas)}/21",
        "percentual": f"{(len(encontradas)/21)*100:.1f}%"
    }

def gerar_relatorio_final(resultados, status_1_21):
    """Gerar relatório final completo"""
    print(f"\n" + "=" * 50)
    print("RELATÓRIO FINAL - VERIFICAÇÃO UNIVERSAL")
    print("=" * 50)
    
    print(f"\n📊 RESUMO GERAL:")
    total_equacoes = sum(len(eqs) for eqs in resultados.values())
    print(f"   • Total de equações em todas as bibliotecas: {total_equacoes}")
    print(f"   • Bibliotecas ativas: {len(resultados)}")
    
    for biblioteca, equacoes in resultados.items():
        print(f"   • {biblioteca}: {len(equacoes)} equações")
    
    print(f"\n🎯 STATUS EQ001-EQ021:")
    print(f"   • {status_1_21['progresso']} equações encontradas")
    print(f"   • {status_1_21['percentual']} de completude")
    
    if not status_1_21['faltantes']:
        print(f"\n🎉 CONQUISTA: TODAS AS EQUAÇÕES DE 1 A 21 ESTÃO PRESENTES!")
    else:
        print(f"\n📝 PRÓXIMOS PASSOS: Transmitir equações faltantes")
    
    return {
        "total_equacoes": total_equacoes,
        "bibliotecas_ativas": len(resultados),
        "status_1_21": status_1_21
    }

# EXECUÇÃO PRINCIPAL
print("🔍 INICIANDO VERIFICAÇÃO UNIVERSAL...\n")

# Analisar todas as bibliotecas
resultados, todas_equacoes = analisar_todas_bibliotecas()

# Verificar específico EQ001-EQ021
status_1_21 = verificar_equacoes_1_a_21(todas_equacoes)

# Gerar relatório final
relatorio = gerar_relatorio_final(resultados, status_1_21)

print(f"\n" + "=" * 50)
print("VERIFICAÇÃO CONCLUÍDA!")
print(f"Equações totais: {relatorio['total_equacoes']}")
print(f"Status EQ001-EQ021: {relatorio['status_1_21']['progresso']}")
print("=" * 50)
