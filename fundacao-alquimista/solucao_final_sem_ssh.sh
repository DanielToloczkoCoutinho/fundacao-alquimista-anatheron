#!/bin/bash

echo "🌌 ZENNITH - SOLUÇÃO FINAL SEM SSH 🌟"
echo "====================================="
echo "🔑 PROBLEMA: ssh-keygen não disponível"
echo "🎯 SOLUÇÃO: GitHub CLI + PAT direto"
echo ""

# 1. 🛠️ VERIFICAR FERRAMENTAS DISPONÍVEIS
echo "1. 🛠️ VERIFICANDO FERRAMENTAS DISPONÍVEIS..."
echo "✅ Git: $(git --version)"
echo "✅ Curl: $(curl --version 2>/dev/null | head -1 || echo 'Disponível')"
echo ""

# 2. 🔧 CONFIGURAR GIT PARA HTTPS
echo "2. 🔧 CONFIGURANDO GIT PARA HTTPS..."
git remote set-url origin https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git

echo "🔍 Remote configurado:"
git remote -v
echo ""

# 3. 📝 CRIAR SCRIPT DE AUTENTICAÇÃO DIRETA
echo "3. 📝 CRIANDO SCRIPT DE AUTENTICAÇÃO DIRETA..."
cat > auth_direct.sh << 'EOF'
#!/bin/bash
# Script de autenticação direta com GitHub
echo "🔑 MÉTODOS DE AUTENTICAÇÃO DISPONÍVEIS:"
echo "1. GitHub CLI (gh auth login)"
echo "2. PAT direto na URL"
echo "3. Configuração manual de credenciais"
echo ""
echo "🎯 RECOMENDADO: Método 2 - PAT direto"
echo ""
echo "📝 INSTRUÇÕES PARA PAT:"
echo "1. Vá para: https://github.com/settings/tokens"
echo "2. Clique em 'Generate new token'"
echo "3. Nomeie: 'FUNDAÇÃO ALQUIMISTA SYNCH'"
echo "4. Expiração: 90 dias"
echo "5. Permissões: SELECIONE 'repo' E 'workflow'"
echo "6. Clique em 'Generate token'"
echo "7. COPIE o token gerado"
echo ""
echo "🚀 COMANDO FINAL:"
echo "git push https://[SEU_TOKEN_AQUI]@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main"
EOF

chmod +x auth_direct.sh

# 4. 🚀 PREPARAR SINCRONIZAÇÃO
echo "4. 🚀 PREPARANDO SINCRONIZAÇÃO DOS 14 COMMITS..."
echo "📊 Commits pendentes:"
git log --oneline origin/main..main
echo ""

# 5. 🔄 MÚLTIPLAS TENTATIVAS DE SINCRONIZAÇÃO
echo "5. 🔄 INICIANDO MÚLTIPLAS TENTATIVAS..."

# Tentativa 1: GitHub CLI se disponível
echo "🔄 Tentativa 1: GitHub CLI..."
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI disponível"
    gh auth status || echo "⚠️  Precisa autenticar: gh auth login"
    git push origin main
else
    echo "❌ GitHub CLI não disponível"
fi

# Tentativa 2: Configurar credenciais em cache
echo ""
echo "🔄 Tentativa 2: Configurando credenciais..."
git config --global credential.helper 'store --file ~/.git-credentials'

# 6. 🔑 MÉTODO DIRETO COM PAT
echo ""
echo "6. 🔑 MÉTODO DIRETO - INSIRA SEU PAT:"
echo "💡 O token NÃO será mostrado na tela para segurança"
echo ""

# Criar arquivo de credenciais manualmente
cat > ~/.git-credentials << 'CREDENTIALS'
https://user:token@github.com
CREDENTIALS

echo "📝 Por favor, EDITE manualmente o arquivo ~/.git-credentials"
echo "🔑 Substitua 'user' por 'DanielToloczkoCoutinho' e 'token' por seu PAT real"
echo ""
echo "💾 Exemplo do arquivo correto:"
echo "https://DanielToloczkoCoutinho:ghp_abcdef123456@github.com"
echo ""

read -p "📋 Já editou o arquivo ~/.git-credentials? (s/n): " edit_confirm

if [ "$edit_confirm" = "s" ]; then
    echo "🚀 Tentando push com credenciais salvas..."
    git push origin main
else
    echo "🔑 Vamos tentar método direto..."
    
    # Método direto seguro
    echo "📝 Digite seu PAT (não será mostrado):"
    read -s github_pat
    
    if [ -n "$github_pat" ]; then
        echo "🚀 Executando push com PAT..."
        git push https://DanielToloczkoCoutinho:${github_pat}@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main
    else
        echo "❌ Nenhum PAT fornecido."
        echo "�� Execute manualmente:"
        echo "git push https://DanielToloczkoCoutinho:[SEU_PAT]@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main"
    fi
fi

# 7. 📊 VERIFICAÇÃO FINAL
echo ""
echo "7. 📊 VERIFICAÇÃO FINAL..."
echo "🔍 Status do Git:"
git status

echo ""
echo "📋 Resumo de commits:"
git log --oneline -5

echo ""
echo "🌐 URL do repositório:"
echo "https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"

echo ""
echo "🎉 SOLUÇÃO FINAL COMPLETA! 🌟"
echo "👉 Se ainda não sincronizou, execute o comando manual abaixo:"
echo "git push https://DanielToloczkoCoutinho:[SEU_PAT_AQUI]@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main"
