#!/bin/bash

echo "🗑️ REMOVENDO ARQUIVOS GRANDES E FAZENDO DEPLOY"
echo "=============================================="
echo ""

# Encontrar arquivos maiores que 50MB
echo "🔍 PROCURANDO ARQUIVOS GRANDES..."
large_files=$(find . -type f -size +50M -not -path "./.git/*" 2>/dev/null | head -10)

if [ -n "$large_files" ]; then
    echo "📦 ARQUIVOS GRANDES ENCONTRADOS:"
    echo "$large_files"
    echo ""
    
    # Remover arquivos grandes
    echo "🗑️ REMOVENDO ARQUIVOS GRANDES..."
    for file in $large_files; do
        echo "Removendo: $file"
        git rm --cached "$file" 2>/dev/null
        rm -f "$file"
    done
else
    echo "✅ Nenhum arquivo grande encontrado"
fi

# Verificar se ainda há arquivos grandes no Git
echo ""
echo "�� VERIFICANDO ARQUIVOS NO GIT LFS..."
git lfs ls-files 2>/dev/null || echo "Git LFS não configurado"

# Fazer commit das remoções
echo ""
echo "💾 COMMIT DAS REMOÇÕES..."
git add .
git commit -m "🔧 Remove arquivos grandes para deploy no GitHub" || true

# Tentar push novamente
echo ""
echo "🚀 TENTANDO DEPLOY NOVAMENTE..."
if git push -u origin main --force; then
    echo ""
    echo "🎉 DEPLOY CONCLUÍDO COM SUCESSO!"
    echo "🌐 https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
else
    echo "❌ Ainda há problemas. Vamos tentar método alternativo..."
    remove_all_large_files
fi
