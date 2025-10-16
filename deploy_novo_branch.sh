#!/bin/bash

echo "🔄 CRIANDO NOVO BRANCH LIMPO"
echo "============================"

# Criar novo branch sem o histórico problemático
echo "🌿 CRIANDO BRANCH 'deploy-limpo'..."
git checkout --orphan deploy-limpo

# Adicionar todos os arquivos atuais (exceto os grandes)
echo "📦 ADICIONANDO ARQUIVOS ATUAIS..."
git add .

# Commit inicial
echo "💾 COMMIT INICIAL..."
git commit -m "🌌 Fundação Alquimista - Deploy Limpo"

# Fazer push do novo branch
echo "🚀 ENVIANDO NOVO BRANCH..."
git push -u origin deploy-limpo

echo ""
echo "🎯 AGORA NO GITHUB:"
echo "   1. Acesse: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
echo "   2. Vá em Settings → Branches"
echo "   3. Mude default branch para 'deploy-limpo'"
echo "   4. Delete a branch 'main'"
echo "   5. Renomeie 'deploy-limpo' para 'main'"
