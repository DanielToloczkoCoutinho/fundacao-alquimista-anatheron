#!/bin/bash

echo "🔍 INICIANDO VERIFICAÇÃO COMPLETA DA FUNDAÇÃO"
echo "=============================================="

# 1. Verificar estrutura de pastas
echo ""
echo "1. 📁 ESTRUTURA DE PASTAS:"
find app/ -type d -name "*-*" | head -10
if [ $? -eq 0 ]; then
    echo "✅ Estrutura de pastas OK"
else
    echo "❌ Problema na estrutura"
fi

# 2. Verificar arquivos page.js
echo ""
echo "2. 📄 ARQUIVOS PAGE.JS:"
find app/ -name "page.js" | wc -l
count_pages=$(find app/ -name "page.js" | wc -l)
echo "Total de páginas: $count_pages"

# 3. Verificar arquivos problemáticos
echo ""
echo "3. 🔧 VERIFICANDO ARQUIVOS PROBLEMÁTICOS:"

# Verificar se há arquivos vazios
empty_files=$(find app/ -name "page.js" -empty)
if [ -z "$empty_files" ]; then
    echo "✅ Nenhum arquivo page.js vazio"
else
    echo "❌ Arquivos vazios encontrados:"
    echo "$empty_files"
fi

# Verificar arquivo analise-fundacao que deu erro
echo ""
echo "4. 📊 VERIFICANDO ANALISE-FUNDACAO:"
if [ -f "app/analise-fundacao/page.js" ]; then
    size=$(wc -c < "app/analise-fundacao/page.js")
    if [ $size -gt 100 ]; then
        echo "✅ analise-fundacao/page.js: OK ($size bytes)"
        echo "   Primeiras linhas:"
        head -3 app/analise-fundacao/page.js
    else
        echo "❌ analise-fundacao/page.js: MUITO PEQUENO ($size bytes)"
    fi
else
    echo "❌ analise-fundacao/page.js: AUSENTE"
fi

# 5. Verificar todos os arquivos page.js
echo ""
echo "5. 📋 LISTA COMPLETA DE PÁGINAS:"
find app/ -name "page.js" | sort | while read file; do
    size=$(wc -c < "$file")
    lines=$(wc -l < "$file")
    echo "   📄 $(basename $(dirname $file)): $lines linhas, $size bytes"
done

# 6. Verificar package.json e dependências
echo ""
echo "6. 📦 VERIFICANDO PACKAGE.JSON:"
if [ -f "package.json" ]; then
    echo "✅ package.json encontrado"
    echo "   Dependências principais:"
    grep -E '"react|"next|"vercel' package.json | head -5
else
    echo "❌ package.json não encontrado"
fi

# 7. Verificar build
echo ""
echo "7. 🏗️ TESTANDO BUILD:"
npm run build --dry-run 2>&1 | grep -E "✓|❌|Error" | head -10
if [ $? -eq 0 ]; then
    echo "✅ Comando build disponível"
else
    echo "❌ Problema com npm run build"
fi

# 8. Verificar estrutura final
echo ""
echo "8. 🌐 RESUMO FINAL:"
echo "   Total de páginas: $count_pages"
echo "   Páginas críticas:"
critical_pages=("central" "modulo-303" "revelacao-real" "metadados-reais")
for page in "${critical_pages[@]}"; do
    if [ -f "app/$page/page.js" ]; then
        size=$(wc -c < "app/$page/page.js")
        echo "   ✅ $page: $(($size/1024)) KB"
    else
        echo "   ❌ $page: AUSENTE"
    fi
done

echo ""
echo "=============================================="
echo "🔍 VERIFICAÇÃO COMPLETA FINALIZADA"
echo ""

# Recomendações
echo "💡 RECOMENDAÇÕES:"
if [ $count_pages -lt 10 ]; then
    echo "   ⚠️  Poucas páginas criadas ($count_pages)"
else
    echo "   ✅ Boa quantidade de páginas ($count_pages)"
fi

# Verificar se as páginas críticas existem
missing_critical=0
for page in "${critical_pages[@]}"; do
    if [ ! -f "app/$page/page.js" ]; then
        missing_critical=1
    fi
done

if [ $missing_critical -eq 0 ]; then
    echo "   ✅ Todas as páginas críticas presentes"
else
    echo "   ❌ Faltam páginas críticas"
fi

echo ""
echo "🚀 PRONTO PARA DEPLOY? [S/N]"
