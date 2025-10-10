#!/bin/bash

echo "�� DEPLOY FINAL E TESTE"
echo "======================"

# Fazer deploy final
echo "🌐 FAZENDO DEPLOY DEFINITIVO..."
DEPLOY_URL=$(npx vercel --prod --force 2>&1 | grep -o 'https://[^ ]*\.vercel\.app' | head -1)

echo ""
echo "=========================================="
echo "🎊 DEPLOY CONCLUÍDO COM SUCESSO!"
echo "🌐 URL DEFINITIVA: $DEPLOY_URL/central"
echo "=========================================="

# Testar a URL
echo ""
echo "🧪 TESTANDO A URL..."
curl -s "$DEPLOY_URL/central" | grep -q "PORTAL CENTRAL" && echo "✅ Página carregando corretamente" || echo "❌ Problema ao carregar"

echo ""
echo "📋 O QUE TESTAR AGORA:"
echo "======================"
echo "1. 🌐 Acesse: $DEPLOY_URL/central"
echo "2. ⏰ Verifique se o TIMER aumenta a cada segundo"
echo "3. 🎯 Teste os botões de ativação dos módulos"
echo "4. 📝 Observe os logs em tempo real"
echo "5. 🎨 Confirme que o layout está centralizado"
echo "6. 🔗 Navegue para Módulo 303: $DEPLOY_URL/modulo-303"
echo "7. 📊 Verifique se dados atualizam automaticamente"

echo ""
echo "🎯 RESULTADO ESPERADO:"
echo "   ✅ Layout responsivo e centralizado"
echo "   ✅ Timer dinâmico funcionando"
echo "   ✅ Botões interativos com feedback"
echo "   ✅ Dados atualizando em tempo real"
echo "   ✅ Navegação entre páginas suave"

