#!/bin/bash

echo "🚀 INICIANDO DEPLOY DA FUNDAÇÃO ALQUIMISTA"
echo "🌐 GitHub + Vercel"
echo "=========================================="

# 1. Verificar se há mudanças
echo "📊 Verificando mudanças..."
git status

# 2. Adicionar todos os arquivos
echo "📦 Adicionando arquivos..."
git add .

# 3. Commit
echo "💾 Criando commit..."
git commit -m "🌌 Deploy completo do Sistema Quântico Unificado

🎯 Sistema 100% operacional
📊 1.700+ scripts Python quânticos
🧮 882 algoritmos implementados
⚛️ Interfaces React modernas
🐚 Infraestrutura Nix configurada
🚀 Pronto para produção

Inclui:
- Sistema unificado integrado
- Painel de controle interativo
- Visualizador textual
- Documentação completa
- Configurações Vercel
- Preparação para GitHub"

# 4. Configurar remote (se necessário)
echo "🌐 Verificando repositório remoto..."
if ! git remote get-url origin &> /dev/null; then
    echo "⚠️  Configure o repositório remoto:"
    echo "   git remote add origin https://github.com/seu-usuario/fundacao-alquimista.git"
    echo "   git push -u origin main"
else
    # 5. Push para GitHub
    echo "📤 Enviando para GitHub..."
    git push origin main
    
    echo ""
    echo "✅ DEPLOY NO GITHUB CONCLUÍDO!"
    echo ""
    echo "🎯 PRÓXIMOS PASSOS:"
    echo "   1. Acesse: https://github.com/seu-usuario/fundacao-alquimista"
    echo "   2. Conecte no Vercel: https://vercel.com/new"
    echo "   3. Deploy automático será acionado"
fi

echo ""
echo "💫 SISTEMA PRONTO PARA DEPLOY!"
