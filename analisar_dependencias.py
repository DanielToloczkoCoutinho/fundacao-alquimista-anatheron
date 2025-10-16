import json
import re
from pathlib import Path

print("📦 ANÁLISE DE DEPENDÊNCIAS DAS INTERFACES")

# Carregar package.json
with open('package.json', 'r') as f:
    package_data = json.load(f)

dependencias = package_data.get('dependencies', {})
dev_dependencias = package_data.get('devDependencies', {})

print(f"\n📊 DEPENDÊNCIAS PRINCIPAIS:")
for dep, versao in list(dependencias.items())[:15]:
    print(f"   📦 {dep}: {versao}")

print(f"\n🔧 DEPENDÊNCIAS DE DESENVOLVIMENTO:")
for dep, versao in list(dev_dependencias.items())[:10]:
    print(f"   🛠️ {dep}: {versao}")

# Analisar imports nas interfaces
print(f"\n🔍 IMPORTS MAIS COMUNS NAS INTERFACES:")

imports_comuns = {}
caminhos_analisados = 0

for caminho in Path('src').rglob('*.tsx'):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Encontrar imports
        imports = re.findall(r'import\s+.*?from\s+[\'"]([^\'"]+)[\'"]', conteudo)
        
        for imp in imports:
            if imp.startswith('@/'):
                imp = imp[2:]
            imports_comuns[imp] = imports_comuns.get(imp, 0) + 1
            
        caminhos_analisados += 1
        
    except Exception as e:
        continue

# Mostrar imports mais comuns
print(f"   📁 Arquivos analisados: {caminhos_analisados}")
for imp, count in sorted(imports_comuns.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(f"   📥 {imp}: {count} usos")

# Salvar análise de dependências
analise_deps = {
    'dependencias_principais': dict(list(dependencias.items())[:20]),
    'dev_dependencias': dict(list(dev_dependencias.items())[:15]),
    'imports_comuns': dict(sorted(imports_comuns.items(), key=lambda x: x[1], reverse=True)[:20])
}

with open('analise_dependencias.json', 'w') as f:
    json.dump(analise_deps, f, indent=2)

print(f"\n💾 Análise de dependências salva: analise_dependencias.json")
