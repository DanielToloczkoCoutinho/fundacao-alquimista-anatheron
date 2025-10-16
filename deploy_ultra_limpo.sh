#!/bin/bash

echo "🧹 DEPLOY ULTRA-LIMPO"
echo "===================="

# Remover TODOS os arquivos grandes
echo "🗑️ REMOVENDO TODOS OS ARQUIVOS >10MB..."
find . -type f -size +10M -not -path "./.git/*" -exec rm -f {} \; 2>/dev/null

# Manter apenas arquivos de código
echo "📦 MANTENDO APENAS CÓDIGO..."
git add *.py *.js *.jsx *.json *.md *.txt *.sh *.html *.css *.yml *.yaml

# Deploy
git commit -m "🌌 Deploy limpo - Fundação Alquimista" || true
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo "🎉 SUCESSO! https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
fi
