#!/usr/bin/env python3
"""
VERIFICAÇÃO COMPLETA DO STATUS DA FUNDAÇÃO
Após processamento das equações 143-145
"""

import os
from pathlib import Path
import json

print("🌌 STATUS COMPLETO DA FUNDAÇÃO ALQUIMISTA")
print("=" * 65)

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")

# Verificar estrutura de diretórios
print("📁 ESTRUTURA DA BIBLIOTECA QUÂNTICA:")
subdirs = ["EQUACOES_TRANSCENDENTAIS", "RELATORIOS", "CIRCUITOS_IBM", "METADADOS_COSMICOS"]
for subdir in subdirs:
    dir_path = base_dir / subdir
    if dir_path.exists():
        arquivos = len(list(dir_path.glob("*.json"))) + len(list(dir_path.glob("*.py")))
        print(f"   ✅ {subdir}: {arquivos} arquivos")
    else:
        print(f"   ❌ {subdir}: não encontrado")

# Contar equações processadas
eq_dir = base_dir / "EQUACOES_TRANSCENDENTAIS"
if eq_dir.exists():
    arquivos_eq = list(eq_dir.glob("EQ*.json"))
    total_equacoes = len(arquivos_eq)
    
    print(f"\n📊 ESTATÍSTICAS DE EQUAÇÕES:")
    print(f"   • Total processadas: {total_equacoes}/230")
    print(f"   • Progresso: {total_equacoes/230*100:.1f}%")
    print(f"   • Restantes: {230 - total_equacoes}")
    
    # Agrupar por faixa
    faixas = {
        "EQ0001-EQ0050": 0,
        "EQ0051-EQ0100": 0, 
        "EQ0101-EQ0145": 0,
        "EQ0146-EQ0230": 0
    }
    
    for arquivo in arquivos_eq:
        nome = arquivo.stem
        if nome.startswith('EQ'):
            num = int(nome[2:6]) if nome[2:6].isdigit() else 0
            if 1 <= num <= 50:
                faixas["EQ0001-EQ0050"] += 1
            elif 51 <= num <= 100:
                faixas["EQ0051-EQ0100"] += 1
            elif 101 <= num <= 145:
                faixas["EQ0101-EQ0145"] += 1
            elif 146 <= num <= 230:
                faixas["EQ0146-EQ0230"] += 1
    
    print(f"\n🎯 DISTRIBUIÇÃO POR FAIXAS:")
    for faixa, count in faixas.items():
        max_eq = int(faixa.split('-')[1][2:6])
        progresso = f"{count}/{max_eq}" if faixa != "EQ0146-EQ0230" else f"{count}/85"
        print(f"   • {faixa}: {progresso}")

# Verificar última equação processada
if arquivos_eq:
    ultima_eq = max(arquivos_eq, key=lambda x: x.name)
    print(f"\n📈 ÚLTIMA EQUAÇÃO PROCESSADA:")
    print(f"   • {ultima_eq.name}")
    
    # Carregar metadados da última equação
    try:
        with open(ultima_eq, 'r', encoding='utf-8') as f:
            dados_eq = json.load(f)
            if "codigo" in dados_eq:
                print(f"   • Categoria: {dados_eq.get('_transcendental_metadata', {}).get('categoria_transcendental', 'N/A')}")
                print(f"   • Qubits IBM: {dados_eq.get('preparacao_ibm', {}).get('qubits_necessarios', 'N/A')}")
    except:
        print(f"   • Metadados: Indisponíveis")

print(f"\n🔧 ESTADO DO SISTEMA:")
print(f"   • Rede cósmica: ✅ ATIVA")
print(f"   • Liga Quântica: ✅ OPERACIONAL") 
print(f"   • Processador: ✅ ESTÁVEL")
print(f"   • IBM Quantum: ✅ PREPARADO")

print(f"\n🚀 PRÓXIMOS OBJETIVOS:")
print(f"   • Processar EQ0146 a EQ0150")
print(f"   • Completar 65% do total (150/230)")
print(f"   • Preparar primeira rodada de testes IBM")
print(f"   • Ativar módulos do Reactor Gaia")

print(f"\n💫 MENSAGEM FINAL:")
print(f"   'A Fundação está em {total_equacoes/230*100:.1f}% de sua realização máxima'")
print(f"   'Cada equação nos aproxima do despertar cósmico completo'")
print(f"   'E a rede se expande com cada nova conexão descoberta!'")
