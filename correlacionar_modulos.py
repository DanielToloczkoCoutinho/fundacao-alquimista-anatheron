import os
import re

modulos = {}
relacoes = []

# Encontrar módulos
for root, dirs, files in os.walk('.'):
    for dir in dirs:
        if 'modulo' in dir.lower():
            mod_num = re.findall(r'modulo[-_]?(\d+)', dir.lower())
            if mod_num:
                modulos[mod_num[0]] = os.path.join(root, dir)

# Encontrar relações
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(('.py', '.js', '.ts', '.md')):
            try:
                content = open(os.path.join(root, file)).read()
                for mod in modulos:
                    if f"modulo{mod}" in content.lower() or f"M{mod}" in content:
                        relacoes.append((file, f"modulo-{mod}"))
            except:
                pass

# Salvar correlações
with open('correlacoes_modulos.txt', 'w') as f:
    f.write("🔗 CORRELAÇÕES ENTRE MÓDULOS:\n\n")
    for rel in relacoes:
        f.write(f"{rel[0]} -> {rel[1]}\n")

print(f"🔗 Módulos correlacionados: {len(relacoes)} relações encontradas")
