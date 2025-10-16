#!/bin/bash

echo "🔐 CONFIGURANDO GIT LFS"
echo "======================="

# Instalar Git LFS
echo "📦 INSTALANDO GIT LFS..."
git lfs install

# Track arquivos grandes
echo "🎯 CONFIGURANDO TRACK DE ARQUIVOS GRANDES..."
git lfs track "*.tar.gz"
git lfs track "*.zip"
git lfs track "*.large"

# Verificar configuração
echo "📋 CONFIGURAÇÃO LFS:"
cat .gitattributes

# Add LFS config
echo "💾 ADICIONANDO CONFIGURAÇÃO LFS..."
git add .gitattributes
git commit -m "🔐 Add Git LFS configuration"

echo ""
echo "🚀 AGORA TENTE O DEPLOY:"
echo "   git push -u origin main --force"
