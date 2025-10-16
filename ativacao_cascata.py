import json

print("💫 INICIANDO ATIVAÇÃO EM CASCATA")

# Carregar padrões
with open('padroes_conexao_aprendidos.json') as f:
    padroes = json.load(f)

# Ordem de ativação baseada nos nexus mestres
ordem_ativacao = ['M0', 'M9', 'M29', 'MΩ']

modulos_ativados = set()
cascata_ativacao = []

def ativar_modulo(modulo_id, nivel=0):
    if modulo_id in modulos_ativados:
        return
        
    modulos_ativados.add(modulo_id)
    cascata_ativacao.append({
        'modulo': modulo_id,
        'nivel': nivel,
        'conexoes': padroes.get(modulo_id, [])
    })
    
    print(f"{'  ' * nivel}🚀 Ativando M{modulo_id} (Nível {nivel})")
    
    # Ativar módulos conectados
    for conexao in padroes.get(modulo_id, []):
        if conexao in padroes:  # Se a conexão é outro módulo
            ativar_modulo(conexao, nivel + 1)

# Iniciar ativação a partir dos nexus mestres
for nexus in ordem_ativacao:
    if nexus in padroes:
        ativar_modulo(nexus)

print(f"\n🎉 CASCATA COMPLETA:")
print(f"   📊 Módulos ativados: {len(modulos_ativados)}")
print(f"   🎯 Níveis de ativação: {max([m['nivel'] for m in cascata_ativacao])}")

# Salvar cascata
with open('cascata_ativacao.json', 'w') as f:
    json.dump(cascata_ativacao, f, indent=2)

print("💾 SALVO: cascata_ativacao.json")
