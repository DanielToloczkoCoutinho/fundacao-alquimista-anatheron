import json
from pathlib import Path

print("🗺️ GERANDO MAPA VISUAL DAS INTERFACES")

# Carregar análise
with open('analise_interfaces_completa.json', 'r') as f:
    dados = json.load(f)

# Gerar mapa em Markdown
mapa_md = "# 🗺️ MAPA DAS INTERFACES DA FUNDAÇÃO ALQUIMISTA\n\n"

# Seção de Páginas
mapa_md += "## 📄 PÁGINAS NEXT.JS\n\n"
for pagina in dados['paginas']:
    caminho = pagina['caminho']
    # Extrair rota amigável
    rota = caminho.replace('src/app/', '').replace('/page.tsx', '').replace('/page.jsx', '')
    mapa_md += f"- **/{rota}** - `{caminho}`\n"
    if 'componentes' in pagina:
        mapa_md += f"  - Componentes: {', '.join(pagina['componentes'])}\n"
    mapa_md += f"  - Tamanho: {pagina['tamanho']} chars, {pagina['linhas']} linhas\n\n"

# Seção de Componentes
mapa_md += "## 🔧 COMPONENTES REACT\n\n"
for componente in dados['componentes'][:20]:  # Limitar para não ficar muito grande
    mapa_md += f"- **{componente['nome']}** - `{componente['caminho']}`\n"
    if 'componentes' in componente:
        mapa_md += f"  - Exporta: {', '.join(componente['componentes'][:3])}\n"
    mapa_md += f"  - Tamanho: {componente['tamanho']} chars\n\n"

if len(dados['componentes']) > 20:
    mapa_md += f"... e mais {len(dados['componentes']) - 20} componentes\n\n"

# Seção de APIs
if dados['apis']:
    mapa_md += "## 🌐 APIS E ENDPOINTS\n\n"
    for api in dados['apis']:
        rota = api['caminho'].replace('src/app/', '').replace('/route.ts', '').replace('/route.js', '')
        mapa_md += f"- **{rota}** - `{api['caminho']}`\n"

# Estatísticas
mapa_md += "\n## 📊 ESTATÍSTICAS GERAIS\n\n"
mapa_md += f"- **Total de Páginas**: {len(dados['paginas'])}\n"
mapa_md += f"- **Total de Componentes**: {len(dados['componentes'])}\n"
mapa_md += f"- **Total de Layouts**: {len(dados['layouts'])}\n"
mapa_md += f"- **Total de APIs**: {len(dados['apis'])}\n"
mapa_md += f"- **Total de Hooks**: {len(dados['hooks'])}\n"
mapa_md += f"- **Total de Utils**: {len(dados['utils'])}\n"

# Salvar mapa
with open('MAPA_INTERFACES.md', 'w', encoding='utf-8') as f:
    f.write(mapa_md)

print("✅ Mapa das interfaces criado: MAPA_INTERFACES.md")
