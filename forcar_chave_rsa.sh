#!/bin/bash

echo "🔧 FORÇANDO USO DA CHAVE RSA CORRETA..."
echo ""

# 1. Parar agente SSH atual
echo "🛑 Parando agente SSH..."
eval "$(ssh-agent -k)" 2>/dev/null || true

# 2. Recarregar agente limpo
echo "🔄 Iniciando agente limpo..."
eval "$(ssh-agent -s)"

# 3. Remover todas as chaves do agente
echo "🧹 Removendo chaves existentes..."
ssh-add -D 2>/dev/null || true

# 4. Adicionar APENAS nossa chave RSA
echo "🔑 Adicionando chave RSA da Fundação Alquimista..."
ssh-add ~/.ssh/id_rsa

# 5. Verificar se é a única chave
echo "📋 Chaves no agente:"
ssh-add -l

# 6. Criar configuração SSH específica
echo "⚙️ Criando configuração SSH específica..."
cat > ~/.ssh/config << 'CONFIG'
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly yes
    PreferredAuthentications publickey
CONFIG

chmod 600 ~/.ssh/config

# 7. Testar conexão
echo "🌐 Testando conexão com chave específica..."
ssh -T git@github.com

echo ""
echo "🎯 Se funcionar, execute: git push -u origin main"
