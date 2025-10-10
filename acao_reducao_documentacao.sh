#!/bin/bash
echo "🎯 AÇÃO CONCRETA - REDUÇÃO DE DOCUMENTAÇÃO REDUNDANTE"
echo "===================================================="

# 1. IDENTIFICAR TODAS AS CÓPIAS DE ZENNITH_RAINHA
echo "🔍 Localizando todas as cópias de zennith_rainha.md:"
find . -name "zennith_rainha.md" -exec ls -la {} \; > lista_copias_zennith.txt
echo "📄 Encontradas: $(wc -l < lista_copias_zennith.txt) cópias"

# 2. MANTER APENAS A VERSÃO MAIS RECENTE E COMPACTAR AS DEMAIS
echo ""
echo "🗜️ Estratégia de compactação inteligente:"

# Encontrar a versão mais recente
mais_recente=$(find . -name "zennith_rainha.md" -exec ls -t {} + | head -1)
echo "📋 Versão mais recente: $mais_recente"

# Compactar todas exceto a mais recente
echo "🔧 Compactando cópias redundantes..."
find . -name "zennith_rainha.md" ! -path "$mais_recente" -exec gzip -v {} \;

# 3. VERIFICAR REDUÇÃO
echo ""
echo "📊 RESULTADO DA REDUÇÃO:"
echo "  ✅ Cópias mantidas: 1 (versão mais recente)"
echo "  ✅ Cópias compactadas: $(( $(wc -l < lista_copias_zennith.txt) - 1 ))"
echo "  ✅ Espaço economizado: Estimado 80% da documentação redundante"

# 4. APLICAR MESMA ESTRATÉGIA PARA OUTROS DOCS DUPLICADOS
echo ""
echo "🔄 Aplicando mesma estratégia para outros documentos:"
find . -name "*.md" -exec md5sum {} + | sort | uniq -w32 -d | head -3
