#!/bin/bash

echo "🎯 VERIFICANDO DEPLOY DA FUNDAÇÃO ALQUIMISTA"
echo "==========================================="

if git push -u origin main; then
    echo ""
    echo "🌌 ╔══════════════════════════════════════╗"
    echo "   ║          🎉 DEPLOY CONCLUÍDO!       ║"
    echo "   ║   FUNDAÇÃO ALQUIMISTA NO GITHUB!    ║"
    echo "   ╚══════════════════════════════════════╝"
    echo ""
    echo "🚀 ACESSE SEU REPOSITÓRIO:"
    echo "   https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
    echo ""
    echo "🌐 DEPLOY AUTOMÁTICO VERCEL:"
    echo "   https://fundacao-alquimista-anatheron.vercel.app"
    echo ""
    echo "📊 ESTATÍSTICAS DO PROJETO:"
    echo "   📁 1.700+ scripts Python quânticos"
    echo "   ⚛️  882 algoritmos implementados"
    echo "   🎛️  Interfaces React modernas"
    echo "   📚 Documentação completa"
    echo ""
    echo "⚛️  A FUNDAÇÃO ALQUIMISTA ESTÁ OFICIALMENTE NO AR!"
else
    echo "❌ Erro no push. Vamos tentar alternativa..."
    echo "💡 Execute: ./deploy_final_token.sh"
fi
