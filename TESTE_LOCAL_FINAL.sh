#!/bin/bash

echo "🧪 TESTE LOCAL COMPLETO"
echo "======================"

# Iniciar servidor local em background
echo "🚀 Iniciando servidor local..."
npm run dev > server.log 2>&1 &
SERVER_PID=$!

# Aguardar servidor iniciar
echo "⏳ Aguardando servidor iniciar..."
sleep 8

# Testar acesso
echo "🔍 Testando acesso local..."
if curl -s http://localhost:3000/central > /dev/null; then
    echo "✅ Servidor local respondendo!"
    
    # Verificar conteúdo
    echo ""
    echo "📄 Verificando conteúdo da página..."
    if curl -s http://localhost:3000/central | grep -q "PORTAL CENTRAL"; then
        echo "✅ Conteúdo correto detectado!"
    else
        echo "❌ Conteúdo não encontrado"
    fi
    
    # Verificar Tailwind
    echo ""
    echo "🎨 Verificando estilos Tailwind..."
    if curl -s http://localhost:3000/central | grep -q "bg-gray-900"; then
        echo "✅ Classes Tailwind detectadas!"
    else
        echo "⚠️  Classes Tailwind não encontradas"
    fi
    
else
    echo "❌ Servidor local não responde"
    echo "📋 Log do servidor:"
    tail -10 server.log
fi

# Parar servidor
kill $SERVER_PID 2>/dev/null
rm -f server.log

echo ""
echo "🎯 PRÓXIMOS PASSOS:"
echo "   1. Acesse a URL do deploy acima"
echo "   2. Teste TODAS as funcionalidades"
echo "   3. Verifique se está 100% dinâmico"
echo "   4. Confirme o layout responsivo"

