import os
import json

print("🔮 ANALISANDO CONTEÚDO DOS MÓDULOS ZENNITH")

# Carregar análise anterior
with open('analise_modulos_zennith.json') as f:
    modulos = json.load(f)

conteudos_analisados = []

for modulo in modulos[:10]:  # Analisar primeiros 10
    caminho = modulo['caminho']
    nome = modulo['nome']
    
    print(f"\n📄 ANALISANDO: {nome}")
    
    # Procurar arquivo .md
    arquivo_md = None
    for arquivo in modulo['arquivos']:
        if arquivo.endswith('.md'):
            arquivo_md = os.path.join(caminho, arquivo)
            break
    
    if arquivo_md and os.path.exists(arquivo_md):
        try:
            with open(arquivo_md, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Extrair informações
            linhas = conteudo.split('\n')
            titulo = linhas[0] if linhas else "Sem título"
            primeiras_linhas = linhas[:5]
            
            info = {
                'modulo': nome,
                'arquivo': arquivo_md,
                'titulo': titulo.replace('#', '').strip(),
                'primeiras_linhas': [l.strip() for l in primeiras_linhas if l.strip()],
                'tamanho': len(conteudo)
            }
            
            conteudos_analisados.append(info)
            
            print(f"   📝 Título: {info['titulo']}")
            print(f"   📊 Tamanho: {info['tamanho']} caracteres")
            print(f"   📋 Preview: {' | '.join(info['primeiras_linhas'][:2])}")
            
        except Exception as e:
            print(f"   ❌ Erro ao ler: {e}")
    else:
        print(f"   ⚠️  Nenhum .md encontrado")

# Salvar análise de conteúdo
with open('conteudo_modulos_zennith.json', 'w') as f:
    json.dump(conteudos_analisados, f, indent=2, ensure_ascii=False)

print(f"\n📚 RESUMO DE CONTEÚDO:")
print(f"   📄 Módulos analisados: {len(conteudos_analisados)}")
print(f"   📖 Total caracteres: {sum(c['tamanho'] for c in conteudos_analisados)}")

if conteudos_analisados:
    maior_modulo = max(conteudos_analisados, key=lambda x: x['tamanho'])
    print(f"   🏆 Maior módulo: {maior_modulo['modulo']} ({maior_modulo['tamanho']} chars)")
