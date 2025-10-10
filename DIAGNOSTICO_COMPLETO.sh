#!/bin/bash

echo "🔍 DIAGNÓSTICO COMPLETO DO SISTEMA"
echo "==================================="

# 1. Verificar estrutura atual
echo ""
echo "📁 ESTRUTURA DE ARQUIVOS:"
echo "-------------------------"
find app -name "*.js" -o -name "*.css" | head -20

# 2. Verificar conteúdo do layout
echo ""
echo "📄 CONTEÚDO DO LAYOUT:"
echo "---------------------"
cat app/layout.js

# 3. Verificar se Tailwind está configurado
echo ""
echo "🎨 CONFIGURAÇÃO TAILWIND:"
echo "------------------------"
if [ -f "tailwind.config.js" ]; then
    echo "✅ tailwind.config.js existe"
    cat tailwind.config.js | head -20
else
    echo "❌ tailwind.config.js NÃO EXISTE"
fi

# 4. Verificar globals.css
echo ""
echo "🌐 GLOBALS.CSS:"
echo "--------------"
if [ -f "app/globals.css" ]; then
    echo "✅ globals.css existe"
    cat app/globals.css | head -10
else
    echo "❌ globals.css NÃO EXISTE"
fi

# 5. Teste local
echo ""
echo "🚀 INICIANDO SERVIDOR LOCAL PARA TESTE:"
echo "--------------------------------------"
echo "Acesse: http://localhost:3000/central"
echo "Pressione Ctrl+C para parar o servidor"
npm run dev

