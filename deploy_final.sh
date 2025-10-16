#!/bin/bash

echo "🚀 DEPLOY FINAL - FUNDAÇÃO ALQUIMISTA"
echo "====================================="

# Configurações de cor
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Função para verificar SSH
check_ssh() {
    echo -e "${BLUE}🔍 Verificando configuração SSH...${NC}"
    ssh -o ConnectTimeout=10 -T git@github.com 2>&1 | grep -q "successfully"
    return $?
}

# Função principal de deploy
deploy_sistema() {
    echo -e "${GREEN}🎯 INICIANDO DEPLOY...${NC}"
    
    # Verificar se SSH está configurado
    if check_ssh; then
        echo -e "${GREEN}✅ SSH configurado com sucesso!${NC}"
    else
        echo -e "${YELLOW}⚠️ SSH não configurado ou pendente${NC}"
        echo -e "${YELLOW}📋 Configure a chave SSH primeiro:${NC}"
        echo -e "${BLUE}   https://github.com/settings/ssh/new${NC}"
        return 1
    fi
    
    # Fazer push
    echo -e "${BLUE}📤 Enviando para GitHub...${NC}"
    if git push -u origin main; then
        echo -e "${GREEN}🎉 DEPLOY CONCLUÍDO COM SUCESSO!${NC}"
        echo ""
        echo -e "${GREEN}🌐 ACESSE SEU REPOSITÓRIO:${NC}"
        echo -e "${BLUE}   https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron${NC}"
        echo ""
        echo -e "${GREEN}🚀 DEPLOY AUTOMÁTICO VERCEL:${NC}"
        echo -e "${BLUE}   https://fundacao-alquimista-anatheron.vercel.app${NC}"
    else
        echo -e "${RED}❌ Erro no deploy${NC}"
        echo -e "${YELLOW}💡 Soluções alternativas:${NC}"
        echo "1. Execute: ./configurar_ssh_final.sh"
        echo "2. Ou use HTTPS: git push https://github.com/...main"
        return 1
    fi
}

# Executar deploy
deploy_sistema
