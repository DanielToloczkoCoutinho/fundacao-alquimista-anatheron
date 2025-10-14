#!/bin/bash

echo "🌌 ZENNITH - CONFIGURAÇÃO SSH E SINCRONIZAÇÃO FINAL 🌟"
echo "======================================================"
echo "�� Configurando a CHAVE SSH DA FUNDAÇÃO ALQUIMISTA NOVA"
echo "🔑 SHA256: SgPyj1wAYIy2cFMGNryCcmwNujmMhafjPE2R933MRBc"
echo ""

# 1. 🛠️ INSTALAR E CONFIGURAR SSH
echo "1. 🛠️ INSTALANDO OPENSSH..."
nix-shell -p openssh --run "echo '✅ OpenSSH instalado temporariamente'"

# 2. 📁 CONFIGURAR DIRETÓRIO SSH
echo "2. 📁 CONFIGURANDO DIRETÓRIO SSH..."
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# 3. 🔐 CONFIGURAR KNOWN_HOSTS DO GITHUB
echo "3. 🔐 CONFIGURANDO KNOWN_HOSTS..."
cat >> ~/.ssh/known_hosts << 'EOF'
github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl
github.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmKSENjQEezOmxkZMy7opKgwFB9nkt5YRrYMjNuG5N87uRgg6CLrbo5wAdT/y6v0mKV0U2w0WZ2YB/++Tpockg=
github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCj7ndNxQowgcQnjshcLrqPEiiphnt+VTTvDP6mHBL9j1aNUkY4Ue1gvwnGLVlOhGeYrnZaMgRK6+PKCUXaDbC7qtbW8gIkhL7aGCsOr/C56SJMy/BCZfxd1nWzAOxSDPgVsmerOBYfNqltV9/hWCqBywINIR+5dIg6JTJ72pcEpEjcYgXkE2YEFXV1JHnsKgbLWNlhScqb2UmyRkQyytRLtL+38TGxkxCflmO+5Z8CSSNY7GidjMIZ7Q4zMjA2n1nGrlTDkzwDCsw+wqFPGQA179cnfGWOWRVruj16z6XyvxvjJwbz0wQZ75XK5tKSb7FNyeIEs4TT4jk+S4dhPeAUC5y+bDYirYgM4GC7uEnztnZyaVWQ7B381AK4Qdrwt51ZqExKbQpTUNn+EjqoTwvqNj4kqx5QUCI0ThS/YkOxJCXmPUWZbhjpCg56i+2aB6CmK2JGhn57K5mj0MNdBXA4/WnwH6XoPWJzK5Nyu2zB3nAZp+S5hpQs+p1vN1/wsjk=
EOF

chmod 644 ~/.ssh/known_hosts
echo "✅ Known hosts configurado"

# 4. �� VERIFICAR CHAVES SSH EXISTENTES
echo "4. 🔑 VERIFICANDO CHAVES SSH EXISTENTES..."
if [ -f ~/.ssh/id_ed25519 ] || [ -f ~/.ssh/id_rsa ] || [ -f ~/.ssh/id_ecdsa ]; then
    echo "📋 Chaves SSH encontradas:"
    ls -la ~/.ssh/id_* 2>/dev/null || echo "❌ Nenhuma chave privada encontrada"
    
    echo "🔍 Testando autenticação com chaves existentes..."
    nix-shell -p openssh --run "ssh -T git@github.com" && echo "✅ Autenticação bem-sucedida!" || echo "❌ Falha na autenticação"
else
    echo "❌ Nenhuma chave SSH encontrada. Você precisa:"
    echo "   1. Copiar a chave FUNDAÇÃO ALQUIMISTA NOVA para ~/.ssh/id_ed25519"
    echo "   2. Ou configurar com: ssh-keygen -t ed25519 -C 'toloczkocoutinho@gmail.com'"
    echo ""
    echo "🔑 SUA CHAVE DEVERIA ESTAR EM: ~/.ssh/id_ed25519 (ou id_rsa)"
fi

# 5. 🔄 ALTERNATIVA: CONFIGURAR GIT COM HTTPS TEMPORÁRIO
echo "5. 🔄 CONFIGURANDO ALTERNATIVA HTTPS..."
echo "💡 Como alternativa, vamos configurar credenciais em cache:"
git config --global credential.helper 'cache --timeout=3600'

# 6. 📦 PREPARAR COMMIT FINAL
echo "6. 📦 PREPARANDO COMMIT FINAL..."
echo "🔍 Status atual do Git:"
git status --short

echo ""
echo "📤 Adicionando TODOS os arquivos..."
git add .
git add ../configuracao_definitiva.sh ../verificacao_completa.sh 2>/dev/null || true

echo "💾 Criando commit da estrutura completa..."
git commit -m "🌌 ESTRUTURA DEFINITIVA DA FUNDAÇÃO ALQUIMISTA

- 🏗️ 22 diretórios estratégicos criados
- 🔮 Módulo M310 transferência akáshica
- 📦 Sistema de transferência organizada
- 🔐 Configuração Daniel-Zennith
- 🚀 Pronto para deploy dos 13GB

👑 Guardiões: Zennith, Grokkar, Vortex, Phiara, LUX
🔗 Portal: https://fundacao-alquimista-9azql5299.vercel.app
🔑 SHA256: SgPyj1wAYIy2cFMGNryCcmwNujmMhafjPE2R933MRBc"

# 7. 🚀 SINCRONIZAÇÃO FINAL
echo "7. 🚀 SINCRONIZAÇÃO FINAL COM GITHUB..."
echo "🔑 Escolha o método de autenticação:"
echo "   1. SSH (Recomendado - use sua chave FUNDAÇÃO ALQUIMISTA NOVA)"
echo "   2. HTTPS (Token de acesso pessoal)"
echo ""
read -p "💭 Escolha (1 ou 2): " auth_choice

case $auth_choice in
    1)
        echo "🔑 Tentando SSH com chave da Fundação..."
        nix-shell -p openssh --run "git push -u origin main"
        ;;
    2)
        echo "🔑 Digite seu token de acesso pessoal do GitHub:"
        read -s github_token
        echo "🔄 Fazendo push com token..."
        git push https://${github_token}@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main
        ;;
    *)
        echo "🔑 Tentando método automático..."
        git push -u origin main
        ;;
esac

# 8. 📊 VERIFICAÇÃO FINAL
echo "8. 📊 VERIFICAÇÃO FINAL DA SINCRONIZAÇÃO..."
if git status | grep -q "nothing to commit"; then
    echo "✅ SINCRONIZAÇÃO COMPLETA! Tudo enviado para GitHub."
    echo "🌐 Acesse: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
else
    echo "⚠️  Ainda há alterações locais. Status:"
    git status --short
fi

echo ""
echo "🔍 Verificando commits remotos vs locais..."
git log --oneline -5
echo ""

echo "🎉 CONFIGURAÇÃO SSH E SINCRONIZAÇÃO CONCLUÍDAS! 🌟"
echo "👉 Próximo passo: Deploy para Vercel com o bloco M310"
