#!/bin/bash

echo "🚀 DEPLOY MANUAL VERIFICADO DAS CORREÇÕES"
echo "========================================="
echo ""

# 1. Parar qualquer processo Next.js
echo "🛑 Parando processos Next.js..."
pkill -f "next" || true

# 2. Limpar cache
echo "🧹 Limpando cache..."
rm -rf .next
rm -rf node_modules/.cache

# 3. Reinstalar dependências se necessário
echo "📦 Verificando dependências..."
if [ ! -d "node_modules" ]; then
    npm install
else
    npm ci
fi

# 4. Build detalhado
echo "🔨 Executando build detalhado..."
npm run build 2>&1 | tee build_detailed.log

# Verificar se o build foi bem-sucedido
if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo "✅ Build bem-sucedido!"
    
    # Verificar páginas construídas
    echo "📄 Páginas construídas:"
    find .next -name "*.html" -o -name "*.js" | grep -E "(modulo-303|metadados-reais|sistema-vivo|status)" | head -10
    
else
    echo "❌ Erro no build!"
    echo "📋 Últimos erros:"
    tail -30 build_detailed.log
    exit 1
fi

# 5. Deploy forçado
echo "🌐 Realizando deploy..."
npx vercel --prod --force 2>&1 | tee deploy_detailed.log

# 6. Verificar deploy
if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo "�� Deploy realizado com sucesso!"
    
    # Extrair URL do deploy
    DEPLOY_URL=$(grep -o 'https://[^ ]*' deploy_detailed.log | head -1)
    echo "🌍 URL do deploy: $DEPLOY_URL"
    
    # Criar arquivo com URLs de teste
    cat > URLS_TESTE.txt << URLS_EOF
🌐 URLs para teste das correções:

📊 Portal Central: $DEPLOY_URL/central
🔮 Módulo 303 (Dinâmico): $DEPLOY_URL/modulo-303  
📝 Metadados Reais (Captura): $DEPLOY_URL/metadados-reais
🌌 Sistema Vivo (Dashboard): $DEPLOY_URL/sistema-vivo
📈 Status (Monitoramento): $DEPLOY_URL/status
🔧 Health Check: $DEPLOY_URL/api/health
📊 Métricas: $DEPLOY_URL/api/metrics

⏰ Teste imediatamente - as páginas devem estar dinâmicas!
URLS_EOF
    
    cat URLS_TESTE.txt
    
else
    echo "❌ Erro no deploy!"
    echo "📋 Últimos erros:"
    tail -30 deploy_detailed.log
fi

