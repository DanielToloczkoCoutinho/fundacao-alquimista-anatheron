#!/bin/bash

echo "📊 STATUS COMPLETO - FUNDAÇÃO ALQUIMISTA"
echo "========================================"

# Cores
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Sistema Git
echo -e "${CYAN}🌐 SISTEMA GIT:${NC}"
echo "📍 Branch: $(git branch --show-current)"
echo "📦 Remote: $(git remote -v | grep origin | head -1 | awk '{print $2}')"
echo "💾 Último commit: $(git log -1 --pretty=format:'%h - %s' --since='1 day ago')"

# Sistema SSH
echo ""
echo -e "${CYAN}🔐 SISTEMA SSH:${NC}"
if [ -f ~/.ssh/id_rsa.pub ]; then
    echo -e "${GREEN}✅ Chave SSH: Presente${NC}"
    echo "📝 Fingerprint: $(ssh-keygen -lf ~/.ssh/id_rsa.pub | awk '{print $2}')"
else
    echo -e "${YELLOW}⚠️ Chave SSH: Ausente${NC}"
fi

# Teste de conexão
echo ""
echo -e "${CYAN}🌐 TESTE DE CONEXÃO:${NC}"
ssh -o ConnectTimeout=5 -T git@github.com 2>&1 | head -1

# Arquivos do projeto
echo ""
echo -e "${CYAN}📁 PROJETO:${NC}"
echo "📊 Total arquivos: $(find . -type f -name "*.py" -o -name "*.js" -o -name "*.json" -o -name "*.md" | wc -l)"
echo "🐍 Scripts Python: $(find . -name "*.py" | wc -l)"
echo "⚛️ Arquivos React: $(find . -name "*.jsx" -o -name "*.tsx" | wc -l)"
echo "📚 Documentação: $(find . -name "*.md" | wc -l)"

# Sistemas principais
echo ""
echo -e "${CYAN}🎯 SISTEMAS PRINCIPAIS:${NC}"
[ -f "sistema_fundacao_unificado.py" ] && echo -e "${GREEN}✅ Sistema Unificado${NC}" || echo -e "${YELLOW}⚠️ Sistema Unificado${NC}"
[ -f "painel_controle_quantico.sh" ] && echo -e "${GREEN}✅ Painel de Controle${NC}" || echo -e "${YELLOW}⚠️ Painel de Controle${NC}"
[ -f "visualizador_textual.py" ] && echo -e "${GREEN}✅ Visualizador${NC}" || echo -e "${YELLOW}⚠️ Visualizador${NC}"

# Status do deploy
echo ""
echo -e "${CYAN}🚀 STATUS DO DEPLOY:${NC}"
if git status | grep -q "nothing to commit"; then
    echo -e "${GREEN}✅ Repositório sincronizado${NC}"
else
    echo -e "${YELLOW}📦 Alterações pendentes${NC}"
    git status --short
fi

# Próximos passos
echo ""
echo -e "${CYAN}�� PRÓXIMOS PASSOS:${NC}"
echo "1. 🔑 Configurar SSH: ./configurar_ssh_final.sh"
echo "2. 🚀 Fazer Deploy: ./deploy_final.sh" 
echo "3. 🌐 Verificar: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
echo "4. 🎮 Usar Local: python3 sistema_fundacao_unificado.py"
