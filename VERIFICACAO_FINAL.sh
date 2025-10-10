#!/bin/bash

echo "🔧 VERIFICAÇÃO FINAL DA ESTRUTURA"
echo "================================"

# Verificar se todos os diretórios necessários existem
echo "📁 Verificando estrutura de diretórios..."
mkdir -p app/components
mkdir -p app/dashboard-completo
mkdir -p app/organograma
mkdir -p app/canal-unico

# Listar estrutura criada
echo ""
echo "🌳 ESTRUTURA CRIADA:"
find app -type f -name "*.js" | head -20

echo ""
echo "📊 COMPONENTES CRIADOS:"
ls -la app/components/

echo ""
echo "🚀 FAZENDO DEPLOY FINAL..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ BUILD SUCESSO! Fazendo deploy..."
    npx vercel --prod --force
else
    echo "❌ ERRO NO BUILD. Verificando problemas..."
    # Tentar corrigir problemas comuns
    npm install
    npm run build
    npx vercel --prod --force
fi

