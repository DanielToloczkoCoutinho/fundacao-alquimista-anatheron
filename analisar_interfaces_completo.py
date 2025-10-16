import os
import json
import re
from pathlib import Path

print("🌌 ANÁLISE COMPLETA DAS INTERFACES DA FUNDAÇÃO")

# Configurações
BASE_DIR = Path('.')
INTERFACE_PATTERNS = [
    '**/*.tsx', '**/*.jsx', '**/*.ts', '**/*.js',
    '**/page.tsx', '**/layout.tsx', '**/component.tsx'
]

# Ignorar node_modules e outros diretórios
IGNORE_DIRS = {'node_modules', '.next', '.git', 'dist', 'build'}

interfaces_encontradas = {
    'paginas': [],
    'componentes': [],
    'layouts': [],
    'apis': [],
    'hooks': [],
    'utils': []
}

def analisar_arquivo(caminho):
    """Analisa um arquivo para extrair informações das interfaces"""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        info = {
            'caminho': str(caminho),
            'nome': caminho.name,
            'tamanho': len(conteudo),
            'linhas': conteudo.count('\n') + 1,
            'tipo': determinar_tipo(caminho, conteudo)
        }
        
        # Extrair componentes React
        componentes = re.findall(r'export\s+(default\s+)?(function|const)\s+(\w+)', conteudo)
        if componentes:
            info['componentes'] = [comp[2] for comp in componentes]
        
        # Verificar se é página Next.js
        if 'use client' in conteudo or 'useState' in conteudo:
            info['client_side'] = True
        if 'use server' in conteudo:
            info['server_side'] = True
            
        return info
        
    except Exception as e:
        return {'caminho': str(caminho), 'erro': str(e)}

def determinar_tipo(caminho, conteudo):
    """Determina o tipo de interface baseado no caminho e conteúdo"""
    caminho_str = str(caminho)
    
    if 'app/' in caminho_str and 'page.tsx' in caminho_str:
        return 'pagina'
    elif 'components/' in caminho_str:
        return 'componente'
    elif 'layout.tsx' in caminho_str:
        return 'layout'
    elif 'api/' in caminho_str:
        return 'api'
    elif 'hooks/' in caminho_str:
        return 'hook'
    elif 'utils/' in caminho_str or 'lib/' in caminho_str:
        return 'util'
    else:
        return 'outro'

# Buscar todas as interfaces
print("📁 Buscando interfaces em toda a estrutura...")

for pattern in INTERFACE_PATTERNS:
    for caminho in BASE_DIR.glob(pattern):
        # Ignorar diretórios não desejados
        if any(ignore in str(caminho) for ignore in IGNORE_DIRS):
            continue
            
        analise = analisar_arquivo(caminho)
        tipo = analise.get('tipo', 'outro')
        
        if tipo in interfaces_encontradas:
            interfaces_encontradas[tipo].append(analise)

# Estatísticas
print(f"\n📊 ESTATÍSTICAS DAS INTERFACES:")
print(f"   📄 Páginas: {len(interfaces_encontradas['paginas'])}")
print(f"   🔧 Componentes: {len(interfaces_encontradas['componentes'])}")
print(f"   🎨 Layouts: {len(interfaces_encontradas['layouts'])}")
print(f"   🌐 APIs: {len(interfaces_encontradas['apis'])}")
print(f"   🪝 Hooks: {len(interfaces_encontradas['hooks'])}")
print(f"   🛠️ Utils: {len(interfaces_encontradas['utils'])}")

# Salvar análise completa
with open('analise_interfaces_completa.json', 'w', encoding='utf-8') as f:
    json.dump(interfaces_encontradas, f, indent=2, ensure_ascii=False)

print(f"\n💾 Análise salva: analise_interfaces_completa.json")

# Mostrar exemplos de cada categoria
print(f"\n🔍 EXEMPLOS ENCONTRADOS:")

for categoria, itens in interfaces_encontradas.items():
    if itens:
        print(f"\n📂 {categoria.upper()}:")
        for item in itens[:3]:  # Mostrar apenas 3 exemplos
            print(f"   📍 {item['caminho']}")
            if 'componentes' in item:
                print(f"      🧩 Componentes: {', '.join(item['componentes'][:3])}")
