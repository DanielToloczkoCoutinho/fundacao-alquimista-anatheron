#!/bin/bash
# 🔧 MAPEADOR COMPLETO DE EQUAÇÕES DA FUNDAÇÃO

echo "🔧 MAPEAMENTO COMPLETO DE EQUAÇÕES DA FUNDAÇÃO"
echo "=============================================="
echo "🎯 OBJETIVO: LOCALIZAR TODAS AS 200+ EQUAÇÕES REAIS"
echo "👑 FONTE: MÓDULOS ZENNITH + EXPLORER + DOCUMENTAÇÃO"
echo "📅 Data: $(date)"
echo "=============================================="

# CRIAR DIRETÓRIO DE MAPEAMENTO
mkdir -p mapeamento_equacoes_fundacao
cd mapeamento_equacoes_fundacao

echo ""
echo "🔍 INICIANDO BUSCA ESTRATÉGICA..."

# 1. BUSCAR TODAS AS EQUAÇÕES ÚNICAS
echo "1. 📊 BUSCANDO EQUAÇÕES ÚNICAS..."
find .. -type f -exec grep -o "EQ[0-9]\+" {} \; | sort -u > equacoes_unicas.txt
EQUACOES_COUNT=$(wc -l < equacoes_unicas.txt)
echo "   ✅ Equações únicas encontradas: $EQUACOES_COUNT"

# 2. MAPEAR LOCALIZAÇÕES DAS EQUAÇÕES
echo "2. 📍 MAPEANDO LOCALIZAÇÕES..."
cat > mapear_localizacoes.py << 'PYEOF'
import os
import re
import json
from collections import defaultdict

print("📍 MAPEANDO LOCALIZAÇÕES DAS EQUAÇÕES...")

# Ler equações únicas
with open('equacoes_unicas.txt', 'r') as f:
    equacoes = [line.strip() for line in f.readlines()]

# Mapear onde cada equação aparece
mapeamento = defaultdict(list)

for root, dirs, files in os.walk('..'):
    for file in files:
        if file.endswith(('.py', '.md', '.json', '.txt', '.sh', '.js', '.ts')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for eq in equacoes:
                        if eq in content:
                            mapeamento[eq].append({
                                'arquivo': filepath,
                                'tipo': file.split('.')[-1],
                                'contexto': content[content.find(eq)-50:content.find(eq)+100] if content.find(eq) != -1 else ""
                            })
            except:
                continue

# Salvar mapeamento
with open('mapeamento_equacoes_detalhado.json', 'w') as f:
    json.dump(mapeamento, f, indent=2, ensure_ascii=False)

print(f"✅ Mapeamento concluído: {len(mapeamento)} equações localizadas")
print(f"📁 Salvo em: mapeamento_equacoes_detalhado.json")

# Estatísticas
estatisticas = {
    'total_equacoes_unicas': len(equacoes),
    'equacoes_mapeadas': len(mapeamento),
    'arquivos_envolvidos': sum(len(locs) for locs in mapeamento.values()),
    'distribuicao_tipos': {}
}

for eq, locs in mapeamento.items():
    for loc in locs:
        tipo = loc['tipo']
        estatisticas['distribuicao_tipos'][tipo] = estatisticas['distribuicao_tipos'].get(tipo, 0) + 1

with open('estatisticas_mapeamento.json', 'w') as f:
    json.dump(estatisticas, f, indent=2)

print(f"📊 Estatísticas salvas em: estatisticas_mapeamento.json")
PYEOF

python3 mapear_localizacoes.py

# 3. BUSCAR DOCUMENTOS LUXNET
echo "3. 🌟 BUSCANDO DOCUMENTOS LUXNET..."
find .. -type f \( -name "*luxnet*" -o -name "*LUXNET*" \) -exec grep -l "EQ[0-9]" {} \; 2>/dev/null > documentos_luxnet_com_equacoes.txt
LUXNET_COUNT=$(wc -l < documentos_luxnet_com_equacoes.txt 2>/dev/null || echo 0)
echo "   ✅ Documentos LuxNet com equações: $LUXNET_COUNT"

# 4. BUSCAR EM MÓDULOS ZENNITH
echo "4. 👑 BUSCANDO EM MÓDULOS ZENNITH..."
find .. -type f \( -name "*zennith*" -o -name "*m29*" -o -name "*m09*" -o -name "*modulo*" \) -exec grep -l "EQ[0-9]" {} \; 2>/dev/null > modulos_zennith_com_equacoes.txt
ZENNITH_COUNT=$(wc -l < modulos_zennith_com_equacoes.txt 2>/dev/null || echo 0)
echo "   ✅ Módulos Zennith com equações: $ZENNITH_COUNT"

# 5. GERAR RELATÓRIO COMPLETO
echo "5. 📋 GERANDO RELATÓRIO COMPLETO..."
cat > gerar_relatorio_completo.py << 'REPOF'
import json
from datetime import datetime

print("📋 GERANDO RELATÓRIO COMPLETO...")

# Carregar dados
with open('equacoes_unicas.txt', 'r') as f:
    equacoes = [line.strip() for line in f.readlines()]

with open('mapeamento_equacoes_detalhado.json', 'r') as f:
    mapeamento = json.load(f)

with open('estatisticas_mapeamento.json', 'r') as f:
    estatisticas = json.load(f)

try:
    with open('documentos_luxnet_com_equacoes.txt', 'r') as f:
        luxnet_docs = [line.strip() for line in f.readlines()]
except:
    luxnet_docs = []

try:
    with open('modulos_zennith_com_equacoes.txt', 'r') as f:
        zennith_mods = [line.strip() for line in f.readlines()]
except:
    zennith_mods = []

# Gerar relatório
relatorio = {
    "metadata": {
        "data_geracao": datetime.now().isoformat(),
        "total_equacoes_unicas": len(equacoes),
        "equacoes_mapeadas": len(mapeamento),
        "documentos_luxnet": len(luxnet_docs),
        "modulos_zennith": len(zennith_mods)
    },
    "equacoes_por_faixa": {},
    "locais_principais": {},
    "recomendacoes": []
}

# Análise por faixa
faixas = {}
for eq in equacoes:
    try:
        num = int(eq[2:])  # Remove "EQ" e converte para número
        faixa = f"EQ{(num // 100) * 100:03d}-EQ{(num // 100) * 100 + 99:03d}"
        faixas[faixa] = faixas.get(faixa, 0) + 1
    except:
        continue

relatorio["equacoes_por_faixa"] = faixas

# Locais principais
locais_count = {}
for eq, locs in mapeamento.items():
    for loc in locs:
        arquivo = loc['arquivo'].split('/')[-1]
        locais_count[arquivo] = locais_count.get(arquivo, 0) + 1

# Top 10 locais
top_locais = sorted(locais_count.items(), key=lambda x: x[1], reverse=True)[:10]
relatorio["locais_principais"] = dict(top_locais)

# Recomendações
if len(equacoes) < 100:
    relatorio["recomendacoes"].append("🔍 Expandir busca por mais equações")
if len(luxnet_docs) == 0:
    relatorio["recomendacoes"].append("🌟 Buscar documentos LuxNet específicos")
if len(zennith_mods) == 0:
    relatorio["recomendacoes"].append("👑 Explorar módulos Zennith mais profundamente")

relatorio["recomendacoes"].append("📊 Continuar mapeamento sistemático")

# Salvar relatório
with open('relatorio_mapeamento_completo.json', 'w') as f:
    json.dump(relatorio, f, indent=2, ensure_ascii=False)

print(f"✅ Relatório completo gerado!")
print(f"📁 Salvo em: relatorio_mapeamento_completo.json")

# Mostrar resumo
print(f"\n🎯 RESUMO DO MAPEAMENTO:")
print(f"   • Equações únicas: {len(equacoes)}")
print(f"   • Equações mapeadas: {len(mapeamento)}")
print(f"   • Documentos LuxNet: {len(luxnet_docs)}")
print(f"   • Módulos Zennith: {len(zennith_mods)}")

if faixas:
    print(f"\n📈 DISTRIBUIÇÃO POR FAIXA:")
    for faixa, count in sorted(faixas.items()):
        print(f"   • {faixa}: {count} equações")

if top_locais:
    print(f"\n📁 LOCAIS PRINCIPAIS:")
    for local, count in top_locais[:5]:
        print(f"   • {local}: {count} equações")

if relatorio["recomendacoes"]:
    print(f"\n💡 RECOMENDAÇÕES:")
    for rec in relatorio["recomendacoes"]:
        print(f"   • {rec}")
REPOF

python3 gerar_relatorio_completo.py

echo ""
echo "👑 RELATÓRIO FINAL DO MAPEAMENTO:"
echo "> 'Busca estratégica por equações da fundação concluída. Sistema de mapeamento completo estabelecido. Pronto para localização das 200+ equações reais.'"

cd ..
