import os
import json

print("🔍 INVESTIGAÇÃO DOS MÓDULOS ZENNITH")

# Carregar análise anterior
with open('analise_modulos_zennith.json') as f:
    modulos = json.load(f)

modulos_vazios = []
modulos_com_conteudo = []

for modulo in modulos:
    caminho = modulo['caminho']
    nome = modulo['nome']
    
    # Verificar se é realmente vazio
    arquivo_md = None
    for arquivo in modulo['arquivos']:
        if arquivo.endswith('.md'):
            arquivo_md = os.path.join(caminho, arquivo)
            break
    
    if arquivo_md and os.path.exists(arquivo_md):
        with open(arquivo_md, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
        
        if conteudo == f"Módulo {nome.split('-')[1]}" or len(conteudo) < 20:
            modulos_vazios.append({
                'modulo': nome,
                'conteudo': conteudo,
                'tamanho': len(conteudo)
            })
        else:
            modulos_com_conteudo.append({
                'modulo': nome,
                'conteudo': conteudo[:100] + '...' if len(conteudo) > 100 else conteudo,
                'tamanho': len(conteudo)
            })

print(f"\n📊 RESULTADO DA INVESTIGAÇÃO:")
print(f"   🔴 Módulos vazios/básicos: {len(modulos_vazios)}")
print(f"   ✅ Módulos com conteúdo: {len(modulos_com_conteudo)}")

if modulos_vazios:
    print(f"\n📝 EXEMPLOS DE MÓDULOS VAZIOS:")
    for vazio in modulos_vazios[:5]:
        print(f"   ❌ {vazio['modulo']}: '{vazio['conteudo']}' ({vazio['tamanho']} chars)")

if modulos_com_conteudo:
    print(f"\n�� EXEMPLOS DE MÓDULOS COM CONTEÚDO:")
    for conteudo in modulos_com_conteudo[:3]:
        print(f"   ✅ {conteudo['modulo']}: {conteudo['conteudo']}")

# Salvar investigação
with open('investigacao_modulos_zennith.json', 'w') as f:
    json.dump({
        'vazios': modulos_vazios,
        'com_conteudo': modulos_com_conteudo,
        'total_vazios': len(modulos_vazios),
        'total_com_conteudo': len(modulos_com_conteudo)
    }, f, indent=2, ensure_ascii=False)

print(f"\n💡 RECOMENDAÇÃO:")
if len(modulos_vazios) > len(modulos_com_conteudo):
    print("   🎯 FOCAR NOS MÓDULOS COM CONTEÚDO PRIMEIRO")
else:
    print("   🎯 TODOS OS MÓDULOS TEM POTENCIAL")
