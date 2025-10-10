#!/bin/bash

echo "🔍 VERIFICAÇÃO DETALHADA DAS PÁGINAS ESTÁTICAS"
echo "=============================================="

# Verificar o conteúdo real das páginas
echo "📄 CONTEÚDO DAS PÁGINAS PRINCIPAIS:"
echo "-----------------------------------"

for pagina in central modulo-303 sistema-vivo status; do
    echo ""
    echo "🎯 $pagina/page.js:"
    echo "------------------"
    if [ -f "app/$pagina/page.js" ]; then
        # Verificar se tem 'use client'
        if grep -q "use client" "app/$pagina/page.js"; then
            echo "✅ 'use client' presente"
        else
            echo "❌ 'use client' AUSENTE"
        fi
        
        # Verificar se tem 'export const dynamic'
        if grep -q "export const dynamic" "app/$pagina/page.js"; then
            echo "✅ 'export const dynamic' presente"
            grep "export const dynamic" "app/$pagina/page.js"
        else
            echo "❌ 'export const dynamic' AUSENTE"
        fi
        
        # Verificar se tem useState/useEffect
        if grep -q "useState\|useEffect" "app/$pagina/page.js"; then
            echo "✅ React Hooks presentes"
        else
            echo "❌ React Hooks AUSENTES"
        fi
        
        # Mostrar primeiras linhas
        echo "📝 Primeiras linhas:"
        head -10 "app/$pagina/page.js"
    else
        echo "❌ Arquivo não encontrado"
    fi
done

echo ""
echo "🔧 PROBLEMA IDENTIFICADO:"
echo "-------------------------"
echo "As páginas têm 'export const dynamic' mas ainda estão sendo pré-renderizadas como estáticas."
echo "Isso pode acontecer porque:"
echo "1. Next.js está otimizando automaticamente"
echo "2. Não há dados dinâmicos suficientes"
echo "3. Configuração do build está forçando estático"

