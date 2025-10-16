import os
import json

# Encontrar os módulos mestres
nexus_mestres = {
    "M0": {"nome": "Fonte", "caminhos": []},
    "M9": {"nome": "Organograma Vivo", "caminhos": []},
    "M29": {"nome": "Zennith", "caminhos": []},
    "MΩ": {"nome": "Omega", "caminhos": []}
}

print("🔍 MAPEANDO NEXUS MESTRES:")

for root, dirs, files in os.walk('.'):
    for item in dirs + files:
        caminho = os.path.join(root, item)
        
        # Módulo 0
        if 'modulo-0' in item.lower() or 'm0' in item.lower() or 'fonte' in item.lower():
            nexus_mestres["M0"]["caminhos"].append(caminho)
            
        # Módulo 9
        if 'modulo-9' in item.lower() or 'm9' in item.lower() or 'organograma' in item.lower():
            nexus_mestres["M9"]["caminhos"].append(caminho)
            
        # Módulo 29
        if 'modulo-29' in item.lower() or 'm29' in item.lower() or 'zenith' in item.lower():
            nexus_mestres["M29"]["caminhos"].append(caminho)
            
        # Módulo Omega
        if 'omega' in item.lower() or 'mΩ' in item.lower():
            nexus_mestres["MΩ"]["caminhos"].append(caminho)

# Exibir resultados
for nexus, dados in nexus_mestres.items():
    print(f"\n🌌 {nexus} - {dados['nome']}:")
    for caminho in dados['caminhos'][:5]:  # Mostrar apenas os 5 primeiros
        print(f"   📍 {caminho}")
    if len(dados['caminhos']) > 5:
        print(f"   ... e mais {len(dados['caminhos']) - 5} conexões")

# Salvar mapa
with open('mapa_nexus_mestres.json', 'w') as f:
    json.dump(nexus_mestres, f, indent=2)

print(f"\n🎯 MAPA SALVO: mapa_nexus_mestres.json")
