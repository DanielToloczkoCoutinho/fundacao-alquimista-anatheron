#!/bin/bash

echo "🎯 DEPLOY ESSENCIAL - FUNDAÇÃO ALQUIMISTA"
echo "========================================="

# Remover arquivos problemáticos específicos
echo "🗑️ REMOVENDO ARQUIVOS PROBLEMÁTICOS..."
problem_files=(
    "block-alpha-02.tar.gz"
    "*.tar.gz"
    "*.zip"
    "*.large"
    "node_modules/*"
    "*.log"
    "*.tmp"
)

for pattern in "${problem_files[@]}"; do
    find . -name "$pattern" -not -path "./.git/*" -exec echo "Removendo: {}" \; -exec rm -f {} \; 2>/dev/null
done

# Manter apenas arquivos essenciais
echo ""
echo "📦 MANTENDO ARQUIVOS ESSENCIAIS..."
essential_files=(
    "*.py"
    "*.js"
    "*.jsx"
    "*.json"
    "*.md"
    "*.txt"
    "*.sh"
    "*.html"
    "*.css"
    "*.yml"
    "*.yaml"
    "LICENSE"
    "README*"
    "package.json"
    "vercel.json"
)

# Fazer commit
echo "💾 COMMIT DAS ALTERAÇÕES..."
git add .
for file in "${essential_files[@]}"; do
    git add "$file" 2>/dev/null || true
done

git commit -m "🌌 Deploy essencial - Fundação Alquimista" || true

# Deploy
echo ""
echo "🚀 DEPLOY..."
if git push -u origin main --force; then
    echo ""
    echo "🎉 SUCESSO! FUNDAÇÃO ALQUIMISTA NO GITHUB!"
    echo "🌐 https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
else
    echo "❌ Use: git push -u origin main --force"
fi
