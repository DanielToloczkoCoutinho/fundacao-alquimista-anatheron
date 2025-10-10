#!/bin/bash

echo "🔍 VERIFICAÇÃO DETALHADA DO DEPLOY E CORREÇÕES"
echo "=============================================="
echo ""

# 1. Verificar se os arquivos corrigidos existem
echo "📁 VERIFICANDO ARQUIVOS CORRIGIDOS:"
echo "-----------------------------------"

check_file() {
    if [ -f "$1" ]; then
        echo "✅ $1 - EXISTE"
        # Verificar se tem conteúdo dinâmico
        if grep -q "use client" "$1" || grep -q "useState" "$1" || grep -q "useEffect" "$1"; then
            echo "   🔄 Contém React Hooks (Dinâmico)"
        else
            echo "   ⚠️  Possívelmente estático"
        fi
    else
        echo "❌ $1 - NÃO ENCONTRADO"
    fi
}

check_file "app/modulo-303/page.js"
check_file "app/metadados-reais/page.js" 
check_file "app/sistema-vivo/page.js"
check_file "app/status/page.js"
check_file "app/api/health/route.js"
check_file "app/api/metrics/route.js"

echo ""
echo "🔧 VERIFICANDO CONTEÚDO DAS CORREÇÕES:"
echo "--------------------------------------"

# Verificar Módulo 303
echo "📊 Módulo 303:"
if [ -f "app/modulo-303/page.js" ]; then
    grep -c "useState" app/modulo-303/page.js | xargs echo "   useState:"
    grep -c "useEffect" app/modulo-303/page.js | xargs echo "   useEffect:"
    grep -c "setInterval" app/modulo-303/page.js | xargs echo "   setInterval:"
fi

echo ""
echo "🌐 VERIFICANDO DEPLOY ATUAL:"
echo "---------------------------"

# Verificar último deploy
echo "Último build log:"
if [ -f "deploy.log" ]; then
    tail -10 deploy.log
else
    echo "❌ Log de deploy não encontrado"
fi

echo ""
echo "🚀 TESTANDO BUILD LOCAL:"
echo "-----------------------"

# Testar build localmente
npm run build > build_test.log 2>&1
BUILD_STATUS=$?

if [ $BUILD_STATUS -eq 0 ]; then
    echo "✅ Build local bem-sucedido"
    echo "   Verificando páginas geradas:"
    ls -la .next/server/app/ | grep -E "(modulo-303|metadados-reais|sistema-vivo|status)"
else
    echo "❌ Erro no build local"
    echo "   Log de erro:"
    tail -20 build_test.log
fi

echo ""
echo "📊 VERIFICANDO CONFIGURAÇÃO:"
echo "---------------------------"

# Verificar configurações
if [ -f "next.config.js" ]; then
    echo "✅ next.config.js encontrado"
    cat next.config.js
else
    echo "❌ next.config.js não encontrado"
fi

echo ""
echo "🔍 VERIFICANDO DEPENDÊNCIAS:"
echo "---------------------------"

# Verificar se todas as dependências estão instaladas
if [ -d "node_modules" ]; then
    echo "✅ node_modules encontrado"
    if [ -f "package.json" ]; then
        echo "📦 Dependências no package.json:"
        grep -A 20 '"dependencies"' package.json
    fi
else
    echo "❌ node_modules não encontrado"
    echo "   Instalando dependências..."
    npm install
fi

