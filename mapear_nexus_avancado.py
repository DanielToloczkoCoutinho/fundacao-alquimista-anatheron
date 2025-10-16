import os
import json
import re

print("🔍 MAPEAMENTO AVANÇADO DOS NEXUS MESTRES")

# Estratégia mais precisa para encontrar módulos
def encontrar_modulos_por_numero(numero):
    modulos = []
    
    # Buscar em diretórios de módulos
    modulos_dir = [d for d in os.listdir('.') if 'modulos' in d]
    
    for base_dir in modulos_dir:
        if os.path.isdir(base_dir):
            for item in os.listdir(base_dir):
                # Padrões mais específicos
                padroes = [
                    f"modulo-{numero}",      # modulo-29
                    f"modulo{numero}",       # modulo29  
                    f"m{numero}",            # m29
                    f"mod-{numero}",         # mod-29
                    f"{numero}-",            # 29-zennith
                ]
                
                if any(padrao in item.lower() for padrao in padroes):
                    caminho = os.path.join(base_dir, item)
                    if os.path.isdir(caminho):
                        modulos.append({
                            'caminho': caminho,
                            'nome': item,
                            'tipo': 'diretorio'
                        })
    
    return modulos

# Módulos mestres específicos
nexus_especificos = {
    "M29": {"nome": "Zennith", "alias": ["zenith", "rainha", "zennith"]},
    "M9": {"nome": "Organograma Vivo", "alias": ["organograma", "nexus", "mapa"]},
    "M0": {"nome": "Fonte", "alias": ["fonte", "origem", "zero"]},
    "MΩ": {"nome": "Omega", "alias": ["omega", "fim", "completo"]}
}

resultados = {}

for nexus, info in nexus_especificos.items():
    print(f"\n🌌 BUSCANDO {nexus} - {info['nome']}:")
    
    # Extrair número do nexus
    numero = nexus.replace('M', '').replace('Ω', 'omega')
    
    if numero.isdigit():
        modulos = encontrar_modulos_por_numero(numero)
    else:
        # Para Omega, buscar por nome
        modulos = []
        for root, dirs, files in os.walk('.'):
            for item in dirs + files:
                if any(alias in item.lower() for alias in info['alias']):
                    caminho = os.path.join(root, item)
                    modulos.append({
                        'caminho': caminho,
                        'nome': item,
                        'tipo': 'diretorio' if os.path.isdir(caminho) else 'arquivo'
                    })
    
    resultados[nexus] = {
        'nome': info['nome'],
        'modulos': modulos,
        'total': len(modulos)
    }
    
    for modulo in modulos[:10]:  # Mostrar primeiros 10
        print(f"   📍 {modulo['caminho']}")
    if len(modulos) > 10:
        print(f"   ... e mais {len(modulos) - 10}")

# Salvar resultados refinados
with open('nexus_mapeamento_refinado.json', 'w') as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)

print(f"\n🎯 MAPEAMENTO REFINADO SALVO!")
print(f"📊 RESUMO:")
for nexus, data in resultados.items():
    print(f"   {nexus}: {data['total']} módulos encontrados")
