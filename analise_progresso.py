import json
import os

# Carregar dados
with open('total_arquivos.txt') as f:
    total_arquivos = int(f.read().strip())

with open('analise_interfaces.json') as f:
    interfaces_data = json.load(f)

# Calcular progresso
progresso = {
    'arquivos_totais': total_arquivos,
    'modulos_detectados': interfaces_data['modulos'],
    'interfaces_existentes': interfaces_data['interfaces'],
    'interfaces_ausentes': interfaces_data['ausentes'],
    'percentual_concluido': (interfaces_data['interfaces'] / max(1, interfaces_data['modulos'])) * 100
}

print("📊 PROGRESSO DA ATIVAÇÃO:")
print(f"   📁 Arquivos totais: {progresso['arquivos_totais']:,}")
print(f"   🏗️  Módulos detectados: {progresso['modulos_detectados']}")
print(f"   🎨 Interfaces existentes: {progresso['interfaces_existentes']}")
print(f"   🔴 Interfaces ausentes: {progresso['interfaces_ausentes']}")
print(f"   📈 Progresso: {progresso['percentual_concluido']:.1f}%")

# Salvar relatório
with open('relatorio_progresso.md', 'w') as f:
    f.write("# 📊 RELATÓRIO DE PROGRESSO - FUNDAÇÃO ALQUIMISTA\n\n")
    f.write("## 🎯 STATUS DA ATIVAÇÃO\n\n")
    for key, value in progresso.items():
        f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
    
    f.write(f"\n## 🚀 PRÓXIMOS PASSOS\n\n")
    if progresso['interfaces_ausentes'] > 0:
        f.write(f"1. Criar {progresso['interfaces_ausentes']} interfaces restantes\n")
    f.write("2. Implementar interconexões completas\n")
    f.write("3. Ativar sistemas quânticos\n")
    f.write("4. Expandir para dimensões superiores\n")
