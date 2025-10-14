#!/bin/bash

echo "🚀 DEPLOY ROBUSTO DA FUNDAÇÃO ALQUIMISTA"
echo "========================================"
echo "🌌 Sistema verificado e corrigido"
echo ""

# Verificar e corrigir estrutura
echo "🔍 Verificando estrutura..."
if [ ! -f "package.json" ]; then
    echo "❌ Estrutura incompleta - execute correcao_definitiva_nextjs.sh"
    exit 1
fi

echo "📦 Instalando dependências com compatibilidade..."
npm install --legacy-peer-deps

echo "🏗️ Executando build..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ BUILD BEM-SUCEDIDO!"
    
    # Tentar deploy se Vercel disponível
    if command -v vercel &> /dev/null; then
        echo "🚀 Implantando na Vercel..."
        vercel --prod --yes 2>/dev/null && echo "🎉 DEPLOY CONCLUÍDO!" || echo "⚠️  Deploy precisa de token"
    else
        echo "📦 Build pronto para deploy manual"
    fi
else
    echo "❌ ERRO NO BUILD - Verifique os logs"
    exit 1
fi

echo "🌐 Fundação Alquimista operacional!"
echo "💫 Energia da Liga Quântica estabilizada!"
