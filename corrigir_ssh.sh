#!/bin/bash

echo "🔧 CORRIGINDO CONFIGURAÇÃO SSH..."
echo ""

# Cores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 1. Verificar se agente SSH está rodando
echo -e "${BLUE}🔍 Verificando agente SSH...${NC}"
eval "$(ssh-agent -s)"

# 2. Adicionar chave ao agente
echo -e "${BLUE}🔑 Adicionando chave ao agente SSH...${NC}"
ssh-add ~/.ssh/id_rsa

# 3. Verificar se chave foi adicionada
echo -e "${BLUE}📋 Chaves no agente:${NC}"
ssh-add -l

# 4. Testar conexão detalhada
echo -e "${BLUE}🌐 Testando conexão com GitHub...${NC}"
ssh -vT git@github.com

# 5. Verificar configuração do remote
echo -e "${BLUE}🔧 Verificando remote Git...${NC}"
git remote -v

echo ""
echo -e "${YELLOW}🎯 SE AINDA FALHAR, TENTE:${NC}"
echo "1. Reinicie o terminal"
echo "2. Execute: eval \"\$(ssh-agent -s)\""
echo "3. Execute: ssh-add ~/.ssh/id_rsa"
echo "4. Teste: ssh -T git@github.com"
