#!/bin/bash

echo "🚀 DEPLOY VIA HTTPS - SOLUÇÃO IMEDIATA"
echo "======================================"

# Mudar para HTTPS
git remote set-url origin https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git

# Configurar Git para HTTPS
git config --global url."https://github.com/".insteadOf git@github.com:

# Fazer deploy
echo "📤 Fazendo deploy..."
git add .
git commit -m "🌌 Fundação Alquimista - Deploy Final" || true

# Tentar push
if git push -u origin main; then
    echo "🎉 DEPLOY CONCLUÍDO COM SUCESSO!"
    echo "🌐 Acesse: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
else
    echo "💡 Use token de acesso pessoal:"
    echo "1. Acesse: https://github.com/settings/tokens"
    echo "2. Crie token com permissões 'repo'"
    echo "3. Execute:"
    echo "   git push https://TOKEN@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main"
fi
