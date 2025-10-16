import os
import json

# Carregar dados dos nexus
with open('nexus_mapeamento_refinado.json') as f:
    nexus_data = json.load(f)

print("👑 EXPLORAÇÃO DOS MÓDULOS ZENNITH (M29)")

modulos_zennith = nexus_data.get('M29', {}).get('modulos', [])

# Analisar alguns módulos específicos
modulos_analisados = []

for modulo in modulos_zennith[:20]:  # Analisar primeiros 20
    caminho = modulo['caminho']
    nome = modulo['nome']
    
    print(f"\n🔮 ANALISANDO: {nome}")
    
    # Verificar se é um diretório de módulo real
    if os.path.isdir(caminho):
        arquivos = os.listdir(caminho)
        
        info_modulo = {
            'nome': nome,
            'caminho': caminho,
            'arquivos': arquivos[:10],  # Primeiros 10 arquivos
            'total_arquivos': len(arquivos),
            'tipos_arquivos': {}
        }
        
        # Contar tipos de arquivo
        for arquivo in arquivos:
            extensao = os.path.splitext(arquivo)[1]
            if extensao:
                info_modulo['tipos_arquivos'][extensao] = info_modulo['tipos_arquivos'].get(extensao, 0) + 1
        
        modulos_analisados.append(info_modulo)
        
        print(f"   📁 Arquivos: {len(arquivos)}")
        print(f"   📊 Tipos: {dict(list(info_modulo['tipos_arquivos'].items())[:5])}")
        
        # Verificar se tem arquivos Python (potenciais sistemas)
        if '.py' in info_modulo['tipos_arquivos']:
            print(f"   🐍 Python files: {info_modulo['tipos_arquivos']['.py']}")
        
        # Verificar se tem arquivos de configuração
        config_files = [f for f in arquivos if 'config' in f.lower() or 'settings' in f.lower()]
        if config_files:
            print(f"   ⚙️  Config: {config_files[:3]}")

# Salvar análise
with open('analise_modulos_zennith.json', 'w') as f:
    json.dump(modulos_analisados, f, indent=2)

print(f"\n📊 RESUMO ZENNITH:")
print(f"   🔮 Módulos analisados: {len(modulos_analisados)}")
print(f"   📁 Total módulos M29: {len(modulos_zennith)}")

# Encontrar módulos mais promissores
modulos_python = [m for m in modulos_analisados if m['tipos_arquivos'].get('.py', 0) > 0]
if modulos_python:
    print(f"   🐍 Módulos com Python: {len(modulos_python)}")
    print(f"   🎯 Mais promissor: {modulos_python[0]['nome']}")
