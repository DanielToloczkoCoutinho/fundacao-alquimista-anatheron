#!/bin/bash
echo "📊 ANALISANDO BUNDLE DA FUNDAÇÃO..."

# Build com análise
ANALYZE=true npm run build

echo " "
echo "🎯 BUNDLE ANALYSIS COMPLETA!"
echo "📈 Verifique os relatórios em: .next/analyze/"
echo "🌐 Abra no navegador:"
echo "   - .next/analyze/client.html"
echo "   - .next/analyze/server.html"
