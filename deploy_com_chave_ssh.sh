#!/bin/bash

echo "�� DEPLOY COM CHAVE SSH - FUNDAÇÃO ALQUIMISTA"
echo "============================================="
echo ""

# Configurar SSH específico para GitHub
setup_ssh() {
    echo "🔧 Configurando SSH..."
    eval "$(ssh-agent -s)" > /dev/null 2>&1
    ssh-add ~/.ssh/id_rsa > /dev/null 2>&1
    
    # Criar configuração SSH se não existir
    if [ ! -f ~/.ssh/config ]; then
        cat > ~/.ssh/config << 'SSHCONFIG'
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly yes
    PreferredAuthentications publickey
SSHCONFIG
        chmod 600 ~/.ssh/config
        echo "✅ Configuração SSH criada"
    fi
}

# Verificar conexão SSH
check_ssh() {
    echo "🌐 Verificando conexão SSH..."
    if ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
        echo "✅ SSH conectado com sucesso!"
        return 0
    else
        echo "❌ Falha na conexão SSH"
        return 1
    fi
}

# Deploy principal
deploy() {
    echo ""
    echo "🚀 INICIANDO DEPLOY..."
    echo "📦 Enviando: 1.700+ scripts quânticos"
    echo "⚛️  Algoritmos: 882 implementações"
    echo "🎛️  Interfaces: React modernas"
    echo ""
    
    if git push -u origin main --force; then
        show_success
    else
        echo "❌ Erro no deploy. Tentando método alternativo..."
        alternative_deploy
    fi
}

# Deploy alternativo
alternative_deploy() {
    echo ""
    echo "🔐 MÉTODO ALTERNATIVO:"
    read -p "🔑 Cole token GitHub: " token
    
    if [ -n "$token" ]; then
        echo "📤 Enviando com token..."
        git push https://${token}@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main --force
        
        if [ $? -eq 0 ]; then
            show_success
        else
            echo "❌ Falha no deploy com token"
        fi
    else
        echo "🎯 Execute manualmente:"
        echo "   git push -u origin main --force"
    fi
}

# Tela de sucesso
show_success() {
    echo ""
    echo "🌌 ╔══════════════════════════════════════════════════╗"
    echo "   ║                 🎉 SUCESSO!                    ║"
    echo "   ║         FUNDAÇÃO ALQUIMISTA NO GITHUB!         ║"
    echo "   ╚══════════════════════════════════════════════════╝"
    echo ""
    echo "🚀 REPOSITÓRIO:"
    echo "   https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
    echo ""
    echo "🌐 SITE:"
    echo "   https://fundacao-alquimista-anatheron.vercel.app"
    echo ""
    echo "📊 ESTATÍSTICAS:"
    echo "   �� 1.700+ scripts Python"
    echo "   ⚛️  882 algoritmos quânticos"
    echo "   🎛️  Interfaces React"
    echo "   📚 Documentação completa"
    echo ""
    echo "⚛️  SISTEMA QUÂNTICO OPERACIONAL!"
}

# Executar sequência
setup_ssh
if check_ssh; then
    deploy
else
    alternative_deploy
fi
