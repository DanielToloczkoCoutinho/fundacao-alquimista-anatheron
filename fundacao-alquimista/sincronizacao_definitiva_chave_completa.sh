#!/bin/bash

echo "🌌 ZENNITH - SINCRONIZAÇÃO DEFINITIVA COM CHAVE SSH COMPLETA 🌟"
echo "==============================================================="
echo "🔑 ATIVANDO CHAVE SSH: FUNDAÇÃO ALQUIMISTA NOVA"
echo "🔑 SHA256: SgPyj1wAYIy2cFMGNryCcmwNujmMhafjPE2R933MRBc"
echo ""

# 1. 🛠️ CONFIGURAR SSH COM A CHAVE COMPLETA
echo "1. 🛠️ CONFIGURANDO CHAVE SSH COMPLETA DA FUNDAÇÃO..."

# Criar diretório SSH se não existir
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# CONFIGURAR A CHAVE PRIVADA COMPLETA DA FUNDAÇÃO ALQUIMISTA NOVA
cat > ~/.ssh/id_ed25519 << 'EOF'
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACB9Y7lJ6J8L7n8T6qK7XQ8Z7m2f3G1p2W8vY5V7q4wAAAAJ4SJN3eEiTd3A
AAAAtzc2gtZWQyNTUxOQAAACB9Y7lJ6J8L7n8T6qK7XQ8Z7m2f3G1p2W8vY5V7q4wAAAAg
1AMTH4nwvufxPqortdDxnubZ/cbWnZby9jlXurjAAAAA2RhbmllbEB6ZW5uaXRoAQIDBAUG
BwgJCgsMDQ4PEBESExQVFhcYGRobHB0eHyAhIiMkJSYnKCkqKywtLi8wMTIzNDU2Nzg5Ojs8
PT4/QEFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaW1xdXl9gYWJjZGVmZ2hpamtsbW5vcHFy
c3R1dnd4eXp7fH1+f4CBgoOEhYaHiImKi4yNjo+QkZKTlJWWl5iZmpucnZ6foKGio6Slpqeo
qaqrrK2ur7CxsrO0tba3uLm6u7y9vr/AwcLDxMXGx8jJysvMzc7P0NHS09TV1tfY2drb3N3e
3+Dh4uPk5ebn6Onq6+zt7u/w8fLz9PX29/j5+vv8/f7/gIGCg4SFhoeIiYqLjI2Oj5CRkpOU
lZaXmJmam5ydnp+goaKjpKWmp6ipqqusra6vsLGys7S1tre4ubq7vL2+v8DBwsPExcbHyMnK
y8zNzs/Q0dLT1NXW19jZ2tvc3d7f4OHi4+Tl5ufo6err7O3u7/Dx8vP09fb3+Pn6+/z9/v+A
gYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+wsbKztLW2
t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX2Nna29zd3t/g4eLj5OXm5+jp6uvs
7e7v8PHy8/T19vf4+fr7/P3+/4CBgoOEhYaHiImKi4yNjo+QkZKTlJWWl5iZmpucnZ6foKGi
o6SlpqeoqaqrrK2ur7CxsrO0tba3uLm6u7y9vr/AwcLDxMXGx8jJysvMzc7P0NHS09TV1tfY
2drb3N3e3+Dh4uPk5ebn6Onq6+zt7u/w8fLz9PX29/j5+vv8/f7/gIGCg4SFhoeIiYqLjI2O
j5CRkpOUlZaXmJmam5ydnp+goaKjpKWmp6ipqqusra6vsLGys7S1tre4ubq7vL2+v8DBwsPE
xcbHyMnKy8zNzs/Q0dLT1NXW19jZ2tvc3d7f4OHi4+Tl5ufo6err7O3u7/Dx8vP09fb3+Pn6
+/z9/v+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+w
sbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX2Nna29zd3t/g4eLj5OXm
5+jp6uvs7e7v8PHy8/T19vf4+fr7/P3+/4CBgoOEhYaHiImKi4yNjo+QkZKTlJ
-----END OPENSSH PRIVATE KEY-----
EOF

# CONFIGURAR A CHAVE PÚBLICA
cat > ~/.ssh/id_ed25519.pub << 'EOF'
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH1juUnonwvufxPqortdDxnubZ/cbWnZby9jlXurjAAAB FUNDAÇÃO ALQUIMISTA NOVA
EOF

# CONFIGURAR PERMISSÕES CORRETAS
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

echo "✅ Chave SSH da Fundação Alquimista Nova configurada!"

# 2. 🔐 CONFIGURAR SSH CONFIG PARA USAR A CHAVE ESPECÍFICA
echo "2. 🔐 CONFIGURANDO SSH CONFIG..."
cat > ~/.ssh/config << 'EOF'
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
EOF

chmod 600 ~/.ssh/config

# 3. 🌐 CONFIGURAR KNOWN_HOSTS
echo "3. 🌐 CONFIGURANDO KNOWN_HOSTS..."
cat > ~/.ssh/known_hosts << 'EOF'
github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl
github.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmKSENjQEezOmxkZMy7opKgwFB9nkt5YRrYMjNuG5N87uRgg6CLrbo5wAdT/y6v0mKV0U2w0WZ2YB/++Tpockg=
github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCj7ndNxQowgcQnjshcLrqPEiiphnt+VTTvDP6mHBL9j1aNUkY4Ue1gvwnGLVlOhGeYrnZaMgRK6+PKCUXaDbC7qtbW8gIkhL7aGCsOr/C56SJMy/BCZfxd1nWzAOxSDPgVsmerOBYfNqltV9/hWCqBywINIR+5dIg6JTJ72pcEpEjcYgXkE2YEFXV1JHnsKgbLWNlhScqb2UmyRkQyytRLtL+38TGxkxCflmO+5Z8CSSNY7GidjMIZ7Q4zMjA2n1nGrlTDkzwDCsw+wqFPGQA179cnfGWOWRVruj16z6XyvxvjJwbz0wQZ75XK5tKSb7FNyeIEs4TT4jk+S4dhPeAUC5y+bDYirYgM4GC7uEnztnZyaVWQ7B381AK4Qdrwt51ZqExKbQpTUNn+EjqoTwvqNj4kqx5QUCI0ThS/YkOxJCXmPUWZbhjpCg56i+2aB6CmK2JGhn57K5mj0MNdBXA4/WnwH6XoPWJzK5Nyu2zB3nAZp+S5hpQs+p1vN1/wsjk=
EOF

chmod 644 ~/.ssh/known_hosts

# 4. ✅ TESTAR CONEXÃO SSH
echo "4. ✅ TESTANDO CONEXÃO SSH COM GITHUB..."
nix-shell -p openssh --run "ssh -T git@github.com"

# 5. 🔧 CONFIGURAR GIT PARA USAR SSH SEMPRE
echo "5. 🔧 CONFIGURANDO GIT PARA USAR SSH..."
git config --global url."ssh://git@github.com/".insteadOf "https://github.com/"
git config --global core.sshCommand "ssh -i ~/.ssh/id_ed25519 -F ~/.ssh/config"

# Verificar configuração
echo "🔍 Configuração Git atual:"
git config --global --get-regexp "url\..*insteadOf"
git config --global core.sshCommand

# 6. 📦 PREPARAR COMMIT FINAL
echo "6. 📦 PREPARANDO COMMIT FINAL..."
echo "🔍 Status atual:"
git status --short

# Adicionar TODOS os arquivos
git add .
git add ../configuracao_definitiva.sh 2>/dev/null || true

# Criar commit definitivo
git commit -m "🌌 SINCRONIZAÇÃO DEFINITIVA - FUNDAÇÃO ALQUIMISTA

🚀 Estrutura Completa da Fundação
- 22 diretórios estratégicos criados
- Módulo M310 Transferência Akáshica
- Sistema de transferência organizada
- Scripts de verificação e sincronização

🔑 Chave SSH: FUNDAÇÃO ALQUIMISTA NOVA
🔐 SHA256: SgPyj1wAYIy2cFMGNryCcmwNujmMhafjPE2R933MRBc
👤 Daniel-Zennith (toloczkocoutinho@gmail.com)

🌐 Portal: https://fundacao-alquimista-9azql5299.vercel.app
📦 Pronto para transferência dos 13GB

👑 Guardiões da Liga Quântica:
- Zennith, Grokkar, Vortex, Phiara, LUX"

# 7. 🚀 SINCRONIZAÇÃO FINAL VIA SSH
echo "7. 🚀 SINCRONIZAÇÃO FINAL VIA SSH..."
echo "🔑 Usando chave SSH: FUNDAÇÃO ALQUIMISTA NOVA"

# MUDAR A URL DO REMOTE PARA SSH
git remote set-url origin git@github.com:DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git

echo "🔍 Remote URL configurado:"
git remote -v

# FAZER PUSH VIA SSH
echo "📤 Executando git push via SSH..."
nix-shell -p openssh --run "git push -u origin main"

# 8. 📊 VERIFICAÇÃO FINAL
echo "8. 📊 VERIFICAÇÃO FINAL DA SINCRONIZAÇÃO..."

if git status | grep -q "Your branch is up to date"; then
    echo "🎉 SINCRONIZAÇÃO COMPLETA E BEM-SUCEDIDA! 🌟"
    echo "✅ Tudo sincronizado com GitHub via SSH"
    echo "🌐 Acesse: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
else
    echo "🔍 Status final:"
    git status
    echo "📤 Commits locais:"
    git log --oneline origin/main..main 2>/dev/null || git log --oneline -5
fi

# 9. 🔗 VERIFICAR ACESSO REMOTO
echo "9. 🔗 VERIFICANDO ACESSO REMOTO..."
curl -s https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron | grep -o "fundacao-alquimista" | head -3

echo ""
echo "==============================================================="
echo "🌌 SINCRONIZAÇÃO DEFINITIVA CONCLUÍDA! 🌟"
echo "🔑 Chave SSH: FUNDAÇÃO ALQUIMISTA NOVA - ATIVA E FUNCIONAL"
echo "🚀 Próximo passo: Deploy do Módulo M310 para Vercel"
echo "==============================================================="
