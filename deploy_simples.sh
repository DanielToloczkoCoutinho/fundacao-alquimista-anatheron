#!/bin/bash

echo "🚀 DEPLOY SIMPLIFICADO - FUNDAÇÃO ALQUIMISTA"
echo "============================================"

# Configurar Git para HTTPS
echo "🔧 Configurando Git..."
git config --global url."https://github.com/".insteadOf git@github.com:

# Adicionar arquivos
echo "📦 Adicionando arquivos..."
git add .

# Commit
echo "💾 Commit..."
git commit -m "🌌 Deploy sistema quântico" || true

# Push
echo "📤 Push para GitHub..."
git push https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main

echo ""
echo "✅ DEPLOY CONCLUÍDO!"
echo "🌐 URL: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
