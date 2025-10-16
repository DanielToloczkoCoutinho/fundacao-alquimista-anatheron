#!/bin/bash

echo "🌌 CONFIGURADOR SSH - FUNDAÇÃO ALQUIMISTA"
echo "=========================================="
echo ""

# 🌟 CORES PARA OUTPUT
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 📋 FUNÇÃO PARA MOSTRAR STATUS
show_status() {
    echo -e "${CYAN}🔍 $1${NC}"
}

# ✅ FUNÇÃO PARA SUCESSO
show_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

# ⚠️ FUNÇÃO PARA AVISO
show_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

# 🚀 FUNÇÃO PARA AÇÃO
show_action() {
    echo -e "${PURPLE}🚀 $1${NC}"
}

# 🔧 CONFIGURANDO SSH
show_action "CONFIGURANDO SISTEMA SSH..."

# Criar diretório .ssh se não existir
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Verificar se já existe chave
if [ -f ~/.ssh/id_rsa.pub ]; then
    show_success "Chave SSH já existe"
else
    show_action "Gerando nova chave SSH..."
    ssh-keygen -t rsa -b 4096 -C "fundacao-alquimista@github" -f ~/.ssh/id_rsa -N "" -q
    show_success "Chave SSH gerada com sucesso!"
fi

# 🔐 CONFIGURAR PERMISSÕES
show_action "Configurando permissões..."
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub

# 🔄 REINICIAR AGENTE SSH
show_action "Reiniciando agente SSH..."
eval "$(ssh-agent -s)" > /dev/null 2>&1
ssh-add ~/.ssh/id_rsa > /dev/null 2>&1

# 🌐 CONFIGURAR GIT PARA SSH
show_action "Configurando Git para SSH..."
git remote set-url origin git@github.com:DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git

# 📤 PREPARAR PUSH FINAL
show_action "Preparando push final..."
git add .
git commit -m "🌌 Fundação Alquimista - Sistema Quântico Completo" || true

# 🎯 MOSTRAR CHAVE SSH
echo ""
show_success "CHAVE SSH GERADA COM SUCESSO!"
echo ""
echo -e "${YELLOW}📋 COPIAR A CHAVE ABAIXO E COLAR NO GITHUB:${NC}"
echo -e "${BLUE}https://github.com/settings/ssh/new${NC}"
echo ""
cat ~/.ssh/id_rsa.pub
echo ""

# 🔍 TESTAR CONEXÃO
show_action "Testando conexão SSH..."
ssh -o ConnectTimeout=5 -T git@github.com

# 📝 INSTRUÇÕES FINAIS
echo ""
show_success "CONFIGURAÇÃO CONCLUÍDA!"
echo ""
echo -e "${GREEN}🎯 PRÓXIMOS PASSOS:${NC}"
echo "1. 📋 Copie a chave SSH acima"
echo "2. 🌐 Acesse: https://github.com/settings/ssh/new"
echo "3. 🔐 Cole a chave e salve como 'Fundação Alquimista'"
echo "4. 🚀 Execute: git push -u origin main"
echo ""
echo -e "${CYAN}💫 O sistema está pronto para deploy!${NC}"
