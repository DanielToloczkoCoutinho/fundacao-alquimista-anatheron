#!/bin/bash

echo "🛡️ VERIFICADOR FINAL MELHORADO - DEPLOY SEGURO"
echo "=============================================="
echo "🔍 Verificações sem validação de sintaxe Node.js..."
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

# Verificações seguras (sem validação de sintaxe)
verificar_passo "Arquivo next.config.js existe" "[ -f next.config.js ]"
verificar_passo "Arquivo package.json existe" "[ -f package.json ]"
verificar_passo "Arquivo layout.js existe" "[ -f app/layout.js ]"
verificar_passo "Arquivo CSS Global existe" "[ -f app/globals.css ] || [ -f app/styles/globals.css ]"

# Verificar páginas principais
echo ""
echo "📄 VERIFICANDO PÁGINAS PRINCIPAIS:"
for page in central modulo-303 sistema-vivo status; do
    if [ -f "app/$page/page.js" ]; then
        echo "   ✅ $page/page.js - EXISTE"
        # Verificar se tem 'use client'
        if grep -q "use client" "app/$page/page.js"; then
            echo "      ✅ 'use client' presente"
        else
            echo "      ❌ 'use client' AUSENTE"
            ((ERROS++))
        fi
        # Verificar se tem 'export const dynamic'
        if grep -q "export const dynamic" "app/$page/page.js"; then
            echo "      ✅ 'export const dynamic' presente"
        else
            echo "      ⚠️  'export const dynamic' ausente"
        fi
    else
        echo "   ❌ $page/page.js - NÃO ENCONTRADO"
        ((ERROS++))
    fi
done

# Verificar APIs
echo ""
echo "�� VERIFICANDO APIs:"
for api in health metrics; do
    if [ -f "app/api/$api/route.js" ]; then
        echo "   ✅ api/$api/route.js - EXISTE"
    else
        echo "   ❌ api/$api/route.js - NÃO ENCONTRADO"
        ((ERROS++))
    fi
done

# Verificar configuração do package.json
echo ""
echo "📦 VERIFICANDO PACKAGE.JSON:"
if grep -q '"type": "module"' package.json; then
    echo "   ✅ ES modules configurado"
else
    echo "   ❌ ES modules NÃO configurado"
    ((ERROS++))
fi

# Verificação final
echo ""
if [ $ERROS -eq 0 ]; then
    echo "🎉 TODAS AS VERIFICAÇÕES PASSARAM!"
    echo "🚀 SISTEMA PRONTO PARA DEPLOY SEGURO"
    
    echo ""
    echo "🔨 EXECUTANDO BUILD..."
    if npm run build; then
        echo "✅ BUILD BEM-SUCEDIDO"
        echo ""
        echo "🌐 INICIANDO DEPLOY..."
        npx vercel --prod --force
    else
        echo "❌ ERRO NO BUILD"
        exit 1
    fi
else
    echo "❌ ENCONTRADOS $ERROS ERROS"
    echo "⚠️  CORRIJA OS ERROS ANTES DO DEPLOY"
    exit 1
fi

