#!/bin/bash

echo "🔧 CORRIGINDO URLs E FAZENDO DEPLOY CORRETO"
echo "==========================================="

# URLs mencionadas:
echo "🌐 URLs IDENTIFICADAS:"
echo "  1. https://fundacao-alquimista-anatheron-58nmzylbj.vercel.app/central ✅ (funcionando)"
echo "  2. https://fundacao-alquimista-anatheron-lxluzjev8.vercel.app/central ❌ (com problemas)"
echo "  3. https://fundacao-alquimista-anatheron-8n4emos93.vercel.app/central ❓ (nova)"

echo ""
echo "🎯 CAUSA DO PROBLEMA:"
echo "  - Deploys antigos com código desatualizado"
echo "  - Arquivos duplicados causando conflitos"
echo "  - Múltiplas versões implantadas"

echo ""
echo "🚀 SOLUÇÃO: DEPLOY ÚNICO E CORRETO"

# 1. Primeiro, garantir que temos a versão mais recente
echo ""
echo "📦 PREPARANDO DEPLOY DEFINITIVO..."

# 2. Fazer build para verificar erros
npm run build

if [ $? -eq 0 ]; then
    echo "✅ BUILD SUCESSO - Sem erros de duplicata!"
    
    # 3. Deploy para produção
    echo ""
    echo "🌐 FAZENDO DEPLOY DEFINITIVO..."
    npx vercel --prod --force
    
    # 4. Obter URL final
    URL_FINAL=$(npx vercel --prod 2>&1 | grep -o 'https://[^ ]*\.vercel\.app' | head -1)
    
    echo ""
    echo "🎉 DEPLOY CONCLUÍDO!"
    echo "==================="
    echo "🌐 URL DEFINITIVA: $URL_FINAL/central"
    echo ""
    echo "📋 INSTRUÇÕES:"
    echo "  1. Use APENAS esta URL: $URL_FINAL/central"
    echo "  2. Ignore as URLs antigas"
    echo "  3. Teste toda a funcionalidade"
    echo "  4. Verifique se está dinâmico e responsivo"
else
    echo "❌ ERRO NO BUILD - Verificando problemas..."
    echo ""
    echo "🔍 ÚLTIMOS ERROS:"
    npm run build 2>&1 | tail -20
fi

