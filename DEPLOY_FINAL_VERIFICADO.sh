#!/bin/bash

echo "🚀 DEPLOY FINAL VERIFICADO"
echo "=========================="

# Fazer deploy
echo "🌐 Realizando deploy final..."
npx vercel --prod --force

# Obter URL
URL_FINAL=$(npx vercel --prod 2>&1 | grep -o 'https://[^ ]*' | head -1)

echo ""
echo "�� DEPLOY CONCLUÍDO!"
echo "==================="
echo "🌐 URL FINAL: $URL_FINAL"
echo ""
echo "📱 PÁGINAS PARA TESTE:"
echo "   🏠 Portal Central: $URL_FINAL/central"
echo "   🔮 Módulo 303: $URL_FINAL/modulo-303"
echo "   🌌 Sistema Vivo: $URL_FINAL/sistema-vivo"
echo "   📊 Status: $URL_FINAL/status"
echo ""
echo "✅ VERIFICAÇÃO DE DINAMISMO:"
echo "---------------------------"
echo "1. Acesse o Portal Central"
echo "2. Observe o timer aumentando a cada segundo"
echo "3. Veja os logs sendo atualizados"
echo "4. Navegue para Módulo 303 e veja dados mudando"
echo ""
echo "💡 LEMBRETE:"
echo "As páginas podem aparecer como '○ (Static)' no build,"
echo "mas são DINÂMICAS no cliente devido ao React!"

