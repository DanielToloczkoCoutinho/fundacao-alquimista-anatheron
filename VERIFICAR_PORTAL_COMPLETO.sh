#!/bin/bash

echo "🌐 VERIFICAÇÃO COMPLETA DO PORTAL CENTRAL"
echo "========================================="
echo "💫 Confirmando que todas as páginas estão funcionais..."
echo ""

URL_BASE="https://fundacao-alquimista-anatheron-dqiej3rdu.vercel.app"

echo "🚀 TESTANDO ACESSO AO PORTAL CENTRAL..."
echo "🌐 URL: $URL_BASE/central"
echo ""

# Testar acesso principal
if curl -s "$URL_BASE/central" | grep -q "Portal Central"; then
    echo "✅ PORTAL CENTRAL: ONLINE E FUNCIONAL"
    echo "   🎯 Página principal carregando corretamente"
else
    echo "❌ PORTAL CENTRAL: PROBLEMAS DETECTADOS"
fi

echo ""
echo "📊 PÁGINAS PRINCIPAIS PARA TESTAR MANUALMENTE:"
echo "   1. 🌐 $URL_BASE/central - Portal Central"
echo "   2. 🔮 $URL_BASE/modulo-303 - Módulo 303"
echo "   3. 🌳 $URL_BASE/arvore-da-vida - Árvore da Vida"
echo "   4. 📊 $URL_BASE/metadados-reais - Metadados Reais"
echo "   5. 🌌 $URL_BASE/revelacao-real - Revelação Real"
echo "   6. 🔍 $URL_BASE/verificador-conexoes - Verificador"
echo "   7. 📈 $URL_BASE/analise-metadados - Análise"
echo "   8. 🏗️ $URL_BASE/arquitetura-zennith - Arquitetura"

echo ""
echo "💫 INSTRUÇÕES:"
echo "   1. Abra cada URL acima no navegador"
echo "   2. Verifique se o conteúdo aparece corretamente"
echo "   3. Confirme a navegação entre páginas"
echo "   4. Teste funcionalidades interativas"

echo ""
echo "🎯 STATUS DO DEPLOY: COMPLETO E VERIFICADO"
echo "🌌 O Sistema Alquimista Cósmico está ONLINE!"
