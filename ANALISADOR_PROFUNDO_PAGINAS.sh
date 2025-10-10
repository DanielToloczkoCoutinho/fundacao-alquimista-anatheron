#!/bin/bash

echo "🔍 ANALISADOR PROFUNDO - PÁGINA POR PÁGINA"
echo "=========================================="
echo "📊 Analisando cada módulo antes do deploy..."
echo ""

# Função para análise detalhada
analisar_pagina() {
    local arquivo=$1
    local nome=$2
    
    echo "🎯 ANALISANDO: $nome"
    echo "   📁 Arquivo: $arquivo"
    
    if [ ! -f "$arquivo" ]; then
        echo "   ❌ ARQUIVO NÃO ENCONTRADO"
        return 1
    fi
    
    # Análise de conteúdo
    echo "   📊 ESTATÍSTICAS:"
    echo "      - Linhas: $(wc -l < "$arquivo")"
    echo "      - Tamanho: $(wc -c < "$arquivo") bytes"
    
    # Verificar componentes React
    echo "   ⚛️  COMPONENTES REACT:"
    echo "      - useState: $(grep -c "useState" "$arquivo")"
    echo "      - useEffect: $(grep -c "useEffect" "$arquivo")"
    echo "      - setInterval/setTimeout: $(grep -c "setInterval\|setTimeout" "$arquivo")"
    
    # Verificar problemas comuns
    echo "   🔧 VERIFICAÇÃO DE PROBLEMAS:"
    
    # Verificar se tem "use client"
    if grep -q "use client" "$arquivo"; then
        echo "      ✅ 'use client' presente"
    else
        echo "      ❌ 'use client' AUSENTE - Pode ser estático"
    fi
    
    # Verificar se tem export dynamic
    if grep -q "export const dynamic" "$arquivo"; then
        echo "      ✅ 'export const dynamic' presente"
    else
        echo "      ⚠️  'export const dynamic' ausente"
    fi
    
    # Verificar classes Tailwind problemáticas
    if grep -q "bg-.*-.*-.*" "$arquivo"; then
        echo "      ⚠️  Possíveis classes Tailwind dinâmicas (pode causar fundo branco)"
    fi
    
    # Verificar erros de sintaxe básica
    if node -c "$arquivo" 2>/dev/null; then
        echo "      ✅ Sintaxe JavaScript válida"
    else
        echo "      ❌ ERRO de sintaxe JavaScript"
    fi
    
    echo ""
}

# Analisar cada página crítica
echo "📋 PÁGINAS PRINCIPAIS:"
echo "======================"
analisar_pagina "app/central/page.js" "Portal Central"
analisar_pagina "app/modulo-303/page.js" "Módulo 303"
analisar_pagina "app/sistema-vivo/page.js" "Sistema Vivo"
analisar_pagina "app/status/page.js" "Status"
analisar_pagina "app/api/health/route.js" "API Health"
analisar_pagina "app/api/metrics/route.js" "API Metrics"

# Verificar configurações
echo "⚙️ CONFIGURAÇÕES DO SISTEMA:"
echo "============================"
echo "📄 Next Config:"
if [ -f "next.config.js" ]; then
    cat next.config.js
else
    echo "❌ next.config.js não encontrado"
fi

echo ""
echo "🎨 Tailwind Config:"
if [ -f "tailwind.config.js" ]; then
    grep -A10 "theme" tailwind.config.js | head -15
else
    echo "❌ tailwind.config.js não encontrado"
fi

echo ""
echo "📦 Package.json:"
grep -A5 '"dependencies"' package.json

