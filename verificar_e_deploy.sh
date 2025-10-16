#!/bin/bash

echo "🔍 VERIFICANDO CONFIGURAÇÃO SSH..."
echo ""

# Mostrar chave atual
echo "📋 SUA CHAVE SSH:"
cat ~/.ssh/id_rsa.pub
echo ""

# Testar conexão
echo "�� TESTANDO CONEXÃO..."
ssh -T git@github.com

echo ""
echo "🚀 SE CONECTOU, EXECUTE O DEPLOY:"
echo "   ./deploy_force_final.sh"
echo ""
echo "🎯 OU DIRETAMENTE:"
echo "   git push -u origin main --force"
