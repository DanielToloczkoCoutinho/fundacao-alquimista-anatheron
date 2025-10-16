#!/bin/bash

echo "🔍 ENCONTRANDO ARQUIVO PROBLEMÁTICO: block-alpha-02.tar.gz"
echo "========================================================="

# Encontrar o arquivo específico
find . -name "block-alpha-02.tar.gz" -type f 2>/dev/null

# Verificar tamanho
echo ""
echo "📊 TAMANHO DOS ARQUIVOS .tar.gz:"
find . -name "*.tar.gz" -type f -exec ls -lh {} \; 2>/dev/null

# Remover arquivos .tar.gz
echo ""
echo "��️ REMOVENDO ARQUIVOS .tar.gz..."
find . -name "*.tar.gz" -type f -exec echo "Removendo: {}" \; -exec rm -f {} \; 2>/dev/null

echo ""
echo "✅ ARQUIVOS REMOVIDOS! Tente o deploy novamente."
