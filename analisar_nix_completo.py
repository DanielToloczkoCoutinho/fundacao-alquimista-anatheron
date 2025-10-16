import os
import json
import re
from pathlib import Path

print("�� ANÁLISE COMPLETA DO SISTEMA NIX")

# Buscar arquivos Nix
nix_files = list(Path('.').rglob('*.nix'))
shell_files = list(Path('.').rglob('*.sh'))
nix_configs = []

print("📁 Buscando configurações Nix...")

for nix_file in nix_files:
    try:
        with open(nix_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        nix_configs.append({
            'arquivo': str(nix_file),
            'tamanho': len(content),
            'linhas': content.count('\n') + 1,
            'tipo': 'nix',
            'pacotes': re.findall(r'pkgs\.(\w+)', content)
        })
    except Exception as e:
        print(f"❌ Erro ao ler {nix_file}: {e}")

# Analisar scripts shell relacionados a Nix
for shell_file in shell_files:
    try:
        with open(shell_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'nix' in content.lower() or 'nix-env' in content or 'nix-shell' in content:
            nix_configs.append({
                'arquivo': str(shell_file),
                'tamanho': len(content),
                'linhas': content.count('\n') + 1,
                'tipo': 'shell_nix',
                'comandos_nix': re.findall(r'nix-[a-z-]+', content)
            })
    except Exception as e:
        continue

# Estatísticas
print(f"\n📊 ESTATÍSTICAS NIX:")
print(f"   📄 Arquivos .nix: {len([x for x in nix_configs if x['tipo'] == 'nix'])}")
print(f"   🐚 Scripts relacionados: {len([x for x in nix_configs if x['tipo'] == 'shell_nix'])}")

# Extrair pacotes únicos
all_packages = []
for config in nix_configs:
    if 'pacotes' in config:
        all_packages.extend(config['pacotes'])

unique_packages = list(set(all_packages))

print(f"   📦 Pacotes Nix referenciados: {len(unique_packages)}")
if unique_packages:
    print(f"   🎯 Pacotes: {', '.join(unique_packages[:10])}")

# Salvar análise
with open('analise_nix_completa.json', 'w', encoding='utf-8') as f:
    json.dump({
        'configuracoes_nix': nix_configs,
        'pacotes_unicos': unique_packages,
        'total_arquivos': len(nix_configs)
    }, f, indent=2, ensure_ascii=False)

print(f"\n💾 Análise Nix salva: analise_nix_completa.json")

# Verificar ambiente Nix atual
print(f"\n🔍 AMBIENTE NIX ATUAL:")
import subprocess
try:
    # Verificar se estamos em ambiente Nix
    result = subprocess.run(['nix-env', '--version'], capture_output=True, text=True)
    if result.returncode == 0:
        print("   ✅ Ambiente Nix detectado")
        print(f"   📋 Versão: {result.stdout.strip()}")
    else:
        print("   ❌ Ambiente Nix não detectado")
except:
    print("   ❌ Comando nix-env não disponível")

# Verificar channels
try:
    result = subprocess.run(['nix-channel', '--list'], capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.strip():
        print("   📡 Channels configurados:")
        for line in result.stdout.strip().split('\n'):
            print(f"      📺 {line}")
except:
    print("   ❌ Não foi possível verificar channels")
