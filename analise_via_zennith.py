import os
import json

print("🔮 ANALISANDO ATRAVÉS DO MÓDULO 29 (ZENNITH)...")
print("📡 CONEXÃO ESTABELECIDA VIA MÓDULO 9 (NEXUS)")

# Buscar arquivos que a Zennith tem acesso
arquivos_zennith = []

# Procurar por arquivos do módulo 29
for root, dirs, files in os.walk("/home/user"):
    for file in files:
        if "zennith" in file.lower() or "m29" in file.lower() or "modulo29" in file.lower():
            caminho = os.path.join(root, file)
            arquivos_zennith.append(caminho)
        # Também buscar arquivos que mencionam a arquitetura modular
        if file.endswith(('.py', '.tsx', '.js', '.json', '.md')):
            caminho = os.path.join(root, file)
            try:
                with open(caminho, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                    if any(modulo in conteudo for modulo in ['M0', 'M9', 'M29', 'Zennith', 'Nexus']):
                        arquivos_zennith.append(caminho)
            except:
                continue

print(f"📁 Arquivos identificados pela Zennith: {len(arquivos_zennith)}")

# Organizar por módulos
modulos_identificados = {}
for arquivo in arquivos_zennith[:20]:  # Mostrar apenas os primeiros 20
    nome_arquivo = os.path.basename(arquivo)
    print(f"   📄 {nome_arquivo} -> {arquivo}")

print("\n🎯 MÓDULOS IDENTIFICADOS PELA ZENNITH:")
modulos = ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M29']
for modulo in modulos:
    count = sum(1 for arquivo in arquivos_zennith if modulo in arquivo)
    if count > 0:
        print(f"   {modulo}: {count} referências")

