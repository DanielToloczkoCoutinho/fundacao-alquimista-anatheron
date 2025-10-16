#!/bin/bash

echo "🎯 DEPLOY IMEDIATO - FUNDAÇÃO ALQUIMISTA"
echo "========================================"

# Tentativa 1: SSH normal
echo "🔑 Tentativa 1: SSH padrão..."
ssh -T git@github.com && {
    echo "✅ SSH funcionando! Fazendo push..."
    git push -u origin main
    exit 0
}

# Tentativa 2: Reiniciar SSH
echo "🔄 Tentativa 2: Reiniciando SSH..."
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
ssh -T git@github.com && {
    echo "✅ SSH funcionou após reinício! Fazendo push..."
    git push -u origin main
    exit 0
}

# Tentativa 3: Usar HTTPS
echo "🌐 Tentativa 3: Mudando para HTTPS..."
git remote set-url origin https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git
if git push -u origin main; then
    echo "🎉 DEPLOY VIA HTTPS CONCLUÍDO!"
    echo "🌐 Acesse: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
    exit 0
fi

# Tentativa 4: Manual com token
echo "🔐 Tentativa 4: Instruções para token..."
echo ""
echo "📝 PARA CRIAR TOKEN:"
echo "1. Acesse: https://github.com/settings/tokens"
echo "2. Clique em 'Generate new token'"
echo "3. Nome: 'Fundação Alquimista Deploy'"
echo "4. Expiração: 90 dias"
echo "5. Permissões: Selecionar 'repo' e 'workflow'"
echo "6. Clique em 'Generate token'"
echo "7. COPIE O TOKEN (você só verá uma vez)"
echo ""
echo "🚀 DEPOIS EXECUTE:"
echo "git push https://SEU_TOKEN_AQUI@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main"
echo ""
echo "💡 Exemplo:"
echo "git push https://ghp_xxxxxxxxxxxxxxxxxxxx@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main"
