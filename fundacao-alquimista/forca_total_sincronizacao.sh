#!/bin/bash

echo "🌌 ZENNITH - FORÇA TOTAL DE SINCRONIZAÇÃO 🌟"
echo "==========================================="

# 1. 🛠️ INSTALAR OPENSSH PERMANENTEMENTE
echo "1. 🛠️ INSTALANDO OPENSSH..."
nix-shell -p openssh --run "echo '✅ SSH disponível'"

# 2. 🔧 CONFIGURAR GIT COM SSH FORÇADO
echo "2. 🔧 CONFIGURANDO GIT COM SSH FORÇADO..."
git config --global url."git@github.com:".insteadOf "https://github.com/"
git remote set-url origin git@github.com:DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git

# 3. 🚀 SINCRONIZAÇÃO DIRETA
echo "3. 🚀 SINCRONIZAÇÃO DIRETA..."
echo "🔑 Testando autenticação SSH..."
ssh -T git@github.com

echo "📤 Fazendo push FORÇADO..."
git push --force-with-lease origin main

# 4. ✅ VERIFICAÇÃO
echo "4. ✅ VERIFICAÇÃO FINAL..."
git status
echo "🔗 GitHub: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"

echo "🎉 FORÇA TOTAL APLICADA! 🌟"
