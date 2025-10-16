#!/bin/bash

echo "🗑️ REMOVENDO ARQUIVO DO HISTÓRICO DO GIT"
echo "========================================"

# Arquivo problemático
PROBLEM_FILE="block-alpha-02.tar.gz"

echo "🔍 VERIFICANDO SE ARQUIVO EXISTE NO HISTÓRICO..."
git log --all --full-history -- "$PROBLEM_FILE"

echo ""
echo "🚀 REMOVENDO DO HISTÓRICO DO GIT..."
# Remover do histórico completo
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch '$PROBLEM_FILE'" \
  --prune-empty --tag-name-filter cat -- --all

echo ""
echo "🧹 LIMPANDO CACHE DO GIT..."
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo ""
echo "📊 VERIFICANDO SE AINDA EXISTE..."
git log --all --full-history -- "$PROBLEM_FILE" || echo "✅ Arquivo removido do histórico!"

echo ""
echo "🚀 TENTANDO DEPLOY NOVAMENTE..."
git push -u origin main --force
