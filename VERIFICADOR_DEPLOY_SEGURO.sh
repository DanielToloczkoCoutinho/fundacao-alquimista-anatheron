#!/bin/bash

echo "🛡️ VERIFICADOR DE DEPLOY SEGURO"
echo "==============================="
echo "🔍 Executando verificações antes do deploy..."
echo ""

PASSOS=0
ERROS=0

verificar_passo() {
    local passo=$1
    local comando=$2
    
    ((PASSOS++))
    echo "🔍 Passo $PASSOS: $passo"
    
    if eval "$comando" 2>/dev/null; then
        echo "   ✅ OK"
        return 0
    else
        echo "   ❌ FALHOU"
        ((ERROS++))
        return 1
    fi
}

# Verificações críticas
verificar_passo "Sintaxe do Next.js Config" "node -c next.config.js"
verificar_passo "Sintaxe do Layout" "node -c app/layout.js"
verificar_passo "Sintaxe do Portal Central" "node -c app/central/page.js"
verificar_passo "Sintaxe do Módulo 303" "node -c app/modulo-303/page.js"
verificar_passo "Sintaxe do Sistema Vivo" "node -c app/sistema-vivo/page.js"
verificar_passo "Sintaxe do Status" "node -c app/status/page.js"
verificar_passo "Arquivo CSS Global" "[ -f app/styles/globals.css ] || [ -f app/globals.css ]"
verificar_passo "Package.json válido" "node -e \"require('./package.json')\""

# Verificar se todas as páginas têm 'use client'
echo ""
echo "🔎 VERIFICANDO COMPONENTES CLIENTE:"
for page in app/central/page.js app/modulo-303/page.js app/sistema-vivo/page.js app/status/page.js; do
    if [ -f "$page" ] && grep -q "use client" "$page"; then
        echo "   ✅ $(basename $(dirname $page)) - use client presente"
    else
        echo "   ❌ $(basename $(dirname $page)) - use client AUSENTE"
        ((ERROS++))
    fi
done

# Verificação final
echo ""
if [ $ERROS -eq 0 ]; then
    echo "🎉 TODAS AS VERIFICAÇÕES PASSARAM!"
    echo "🚀 PRONTO PARA DEPLOY SEGURO"
    
    # Build de teste
    echo ""
    echo "🔨 EXECUTANDO BUILD DE TESTE..."
    if npm run build; then
        echo "✅ BUILD BEM-SUCEDIDO"
        echo ""
        echo "🌐 INICIANDO DEPLOY..."
        npx vercel --prod --force
    else
        echo "❌ ERRO NO BUILD - Verifique os logs acima"
        exit 1
    fi
else
    echo "❌ ENCONTRADOS $ERROS ERROS"
    echo "⚠️  CORRIJA OS ERROS ANTES DO DEPLOY"
    exit 1
fi

