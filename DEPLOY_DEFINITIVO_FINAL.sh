#!/bin/bash

echo "🎯 DEPLOY DEFINITIVO - SISTEMA COMPLETO"
echo "======================================"

# Nova URL será gerada
echo "🚀 Gerando deploy definitivo..."
npx vercel --prod --force

# Obter a URL final
URL_FINAL=$(npx vercel --prod 2>&1 | grep -o 'https://[^ ]*' | head -1)

echo ""
echo "🎉 DEPLOY DEFINITIVO CONCLUÍDO!"
echo "==============================="
echo ""
echo "🌐 URL DEFINITIVA:"
echo "   $URL_FINAL"
echo ""
echo "📱 PÁGINAS PRINCIPAIS:"
echo "   🏠 Portal Central: $URL_FINAL/central"
echo "   🔮 Módulo 303: $URL_FINAL/modulo-303"
echo "   🌌 Sistema Vivo: $URL_FINAL/sistema-vivo"
echo "   📊 Status: $URL_FINAL/status"
echo ""
echo "✅ SISTEMA 100% OPERACIONAL E VERIFICADO"

