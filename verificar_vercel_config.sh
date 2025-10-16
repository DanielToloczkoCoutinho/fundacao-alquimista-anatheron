#!/bin/bash
echo "🌐 VERIFICAÇÃO COMPLETA DO VERCEL"
echo "================================"

# VERIFICAR CONFIGURAÇÃO DO VERCEL
echo "🔧 CONFIGURAÇÕES VERCEL:"
[ -f "vercel.json" ] && echo "✅ vercel.json: PRESENTE" || echo "❌ vercel.json: AUSENTE"
[ -d ".vercel" ] && echo "✅ .vercel/: PRESENTE" || echo "❌ .vercel/: AUSENTE"

# VERIFICAR META TAG GOOGLE
echo ""
echo "🔍 META TAG GOOGLE:"
if [ -f "app/layout.jsx" ]; then
    if grep -q "google-site-verification" app/layout.jsx; then
        echo "✅ Meta tag Google: PRESENTE"
        grep "google-site-verification" app/layout.jsx | head -1
    else
        echo "❌ Meta tag Google: AUSENTE"
    fi
else
    echo "❌ app/layout.jsx: AUSENTE"
fi

# VERIFICAR ARQUIVO DE VERIFICAÇÃO GOOGLE
echo ""
echo "📄 ARQUIVO DE VERIFICAÇÃO GOOGLE:"
[ -f "public/google865a57633873f213.html" ] && echo "✅ Arquivo verificação: PRESENTE" || echo "❌ Arquivo verificação: AUSENTE"

# VERIFICAR DOMÍNIO CONFIGURADO
echo ""
echo "🌐 DOMÍNIO VERCEL:"
if [ -f "vercel.json" ]; then
    grep -A5 -B5 "domain\|production" vercel.json
fi
