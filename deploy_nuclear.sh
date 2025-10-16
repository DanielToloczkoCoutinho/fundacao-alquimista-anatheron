#!/bin/bash

echo "💥 SOLUÇÃO NUCLEAR - NOVO REPOSITÓRIO"
echo "===================================="

# Salvar arquivos atuais
echo "💾 SALVANDO ARQUIVOS ATUAIS..."
mkdir /tmp/fundacao_backup
cp -r ./* /tmp/fundacao_backup/ 2>/dev/null || true
cp -r ./.* /tmp/fundacao_backup/ 2>/dev/null || true

# Voltar para diretório anterior
cd ..

# Clonar repositório vazio
echo "🔄 CLONANDO REPOSITÓRIO VAZIO..."
git clone https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git fundacao-nova
cd fundacao-nova

# Copiar arquivos de volta (exceto .git)
echo "�� COPIANDO ARQUIVOS LIMPOS..."
cp -r /tmp/fundacao_backup/* ./
rm -f block-alpha-02.tar.gz 2>/dev/null || true

# Remover arquivos grandes
echo "🗑️ REMOVENDO ARQUIVOS GRANDES..."
find . -type f -size +50M -exec rm -f {} \; 2>/dev/null

# Commit e push
echo "🚀 DEPLOY NOVO..."
git add .
git commit -m "🌌 Fundação Alquimista - Deploy Nuclear Limpo"
git push -u origin main

echo ""
echo "🎉 NOVO REPOSITÓRIO LIMPO!"
echo "🌐 https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
