#!/bin/bash
echo "🚀 INICIANDO BUILD OTIMIZADO ZENNITH..."

# Limpar cache do Next.js
rm -rf .next

# Build com análise
ANALYZE=true npm run build

# Verificar tamanho do build
echo "📊 ANALISANDO TAMANHO DO BUILD:"
du -sh .next/ | awk '{print "Tamanho do build: " $1}'

# Verificar se há bundle analysis
if [ -d ".next/analyze" ]; then
    echo "✅ Análise de bundle disponível em .next/analyze/"
else
    echo "⚠️  Execute: ANALYZE=true npm run build para análise detalhada"
fi

echo "🎉 BUILD OTIMIZADO CONCLUÍDO!"
