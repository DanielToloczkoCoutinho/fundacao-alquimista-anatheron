#!/bin/bash
echo "🗺️ MAPEAMENTO COMPLETO DOS MÓDULOS SRC..."

# Buscar TODOS os módulos na estrutura src
echo "📁 Procurando em ~/studio/src..."
find ~/studio/src -name "module*" -type d > ~/fundacao-definitiva/analise-modulos/modulos-src-completo.txt
find ~/studio/src -name "MODULO*" -type d >> ~/fundacao-definitiva/analise-modulos/modulos-src-completo.txt

# Buscar também em app
find ~/studio -path "*/app/module*" -type d >> ~/fundacao-definitiva/analise-modulos/modulos-src-completo.txt
find ~/studio -path "*/app/MODULO*" -type d >> ~/fundacao-definitiva/analise-modulos/modulos-src-completo.txt

# Contar total
TOTAL_SRC=$(wc -l < ~/fundacao-definitiva/analise-modulos/modulos-src-completo.txt)
echo "📊 MÓDULOS ENCONTRADOS NO SRC: $TOTAL_SRC"

# Analisar estrutura
echo "📋 Analisando estrutura dos módulos SRC..."
while IFS= read -r modulo; do
    echo "=== $modulo ===" >> ~/fundacao-definitiva/analise-modulos/estrutura-src-detalhada.txt
    find "$modulo" -name "*.tsx" -o -name "*.ts" -o -name "*.js" -o -name "*.json" | head -10 >> ~/fundacao-definitiva/analise-modulos/estrutura-src-detalhada.txt
    echo "" >> ~/fundacao-definitiva/analise-modulos/estrutura-src-detalhada.txt
done < ~/fundacao-definitiva/analise-modulos/modulos-src-completo.txt

echo "✅ MAPEAMENTO SRC CONCLUÍDO!"
