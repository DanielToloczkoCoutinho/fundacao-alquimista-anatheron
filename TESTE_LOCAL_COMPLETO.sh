#!/bin/bash

echo "🧪 TESTE LOCAL COMPLETO"
echo "======================"

# 1. Verificar se o servidor local está funcionando
echo ""
echo "🌐 INICIANDO SERVIDOR LOCAL..."
echo "Acesse: http://localhost:3000/central"
echo ""

# Executar em background e capturar output
npm run dev > dev-server.log 2>&1 &
SERVER_PID=$!

# Aguardar o servidor iniciar
sleep 10

# 2. Verificar se há erros no log
echo ""
echo "📋 LOG DO SERVIDOR:"
echo "------------------"
tail -20 dev-server.log

# 3. Fazer requisição teste para verificar se está funcionando
echo ""
echo "🔍 TESTANDO ACESSO LOCAL..."
if curl -s http://localhost:3000/central > /dev/null; then
    echo "✅ Servidor local respondendo!"
    
    # Verificar conteúdo da página
    echo ""
    echo "📄 CONTEÚDO DA PÁGINA (primeiras linhas):"
    curl -s http://localhost:3000/central | head -10
    
else
    echo "❌ Servidor local não está respondendo"
    echo ""
    echo "🔍 DETALHES DO ERRO:"
    cat dev-server.log | grep -i error
fi

# 4. Parar servidor
kill $SERVER_PID 2>/dev/null

# 5. Verificar build final
echo ""
echo "🏗️ VERIFICANDO BUILD FINAL..."
npm run build

if [ $? -eq 0 ]; then
    echo ""
    echo "�� BUILD SUCESSO! Sistema pronto para deploy."
    
    # Obter URL atual do Vercel
    echo ""
    echo "🌐 URL ATUAL DO VERCEL:"
    npx vercel --prod 2>&1 | grep -o 'https://[^ ]*\.vercel\.app' | head -1
else
    echo ""
    echo "❌ ERRO NO BUILD FINAL"
    npm run build 2>&1 | tail -10
fi

