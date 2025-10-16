#!/bin/bash

echo "🔍 BUSCA AGressIVA POR ARQUIVOS GRANDES"
echo "======================================="

# Encontrar todos os arquivos maiores que 10MB
echo "📊 ARQUIVOS MAIORES QUE 10MB:"
find . -type f -size +10M -not -path "./.git/*" -exec ls -lh {} \; 2>/dev/null | head -20

echo ""
echo "🎯 ARQUIVOS MAIORES QUE 50MB (PROBLEMÁTICOS):"
find . -type f -size +50M -not -path "./.git/*" -exec ls -lh {} \; 2>/dev/null

echo ""
echo "🚀 REMOVENDO ARQUIVOS MAIORES QUE 50MB..."
find . -type f -size +50M -not -path "./.git/*" -exec echo "Removendo: {}" \; -exec rm -f {} \; 2>/dev/null

echo ""
echo "💾 ATUALIZANDO GIT..."
git add .
git commit -m "🗑️ Remove arquivos grandes >50MB" || true

echo "✅ PRONTO! Tente o deploy novamente:"
echo "   git push -u origin main --force"
