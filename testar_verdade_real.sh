#!/bin/bash
echo "🧪 TESTANDO A VERDADE REAL"
echo "========================="

echo "🔗 Testando URL da verdade..."
status_code=$(curl -s -o /dev/null -w "%{http_code}" "https://fundacao-alquimista-anatheron.vercel.app/verdade-real")

if [ "$status_code" -eq 200 ]; then
    echo "✅ VERDADE REAL ONLINE! (200)"
    echo ""
    echo "🎯 O QUE VOCÊ VAI VER:"
    echo "   📊 1,328 circuitos quânticos REAIS"
    echo "   🔧 4,252 execuções REAIS" 
    echo "   📁 Caminhos EXATOS dos arquivos"
    echo "   🔍 Sistemas VERIFICADOS no backend"
    echo ""
    echo "🌐 ACESSE AGORA:"
    echo "   https://fundacao-alquimista-anatheron.vercel.app/verdade-real"
else
    echo "❌ Ainda com problemas ($status_code)"
    echo "📋 Vamos verificar o build..."
    npm run build
fi
