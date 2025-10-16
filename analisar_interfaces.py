import os
import json

# Contar módulos existentes
modulos = []
for root, dirs, files in os.walk('.'):
    for dir in dirs:
        if 'modulo' in dir.lower():
            modulos.append(os.path.join(root, dir))

# Contar interfaces (arquivos React/Next)
interfaces = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(('.js', '.jsx', '.ts', '.tsx')):
            if any(comp in file.lower() for comp in ['page', 'component', 'layout']):
                interfaces.append(os.path.join(root, file))

print(f"🏗️  MÓDULOS ENCONTRADOS: {len(modulos)}")
print(f"🎨 INTERFACES ENCONTRADAS: {len(interfaces)}")
print(f"🔴 INTERFACES A CRIAR: {max(0, len(modulos) - len(interfaces))}")

# Salvar análise
with open('analise_interfaces.json', 'w') as f:
    json.dump({
        'modulos': len(modulos),
        'interfaces': len(interfaces),
        'ausentes': max(0, len(modulos) - len(interfaces))
    }, f, indent=2)
