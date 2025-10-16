#!/bin/bash

echo "🔍 ANÁLISE DETALHADA DO PROBLEMA SSH"
echo "==================================="

echo ""
echo "📋 CHAVES DETECTADAS PELO SSH:"
ssh-add -l

echo ""
echo "🔑 CHAVES NO DIRETÓRIO SSH:"
ls -la ~/.ssh/

echo ""
echo "🌐 CONFIGURAÇÃO SSH ATUAL:"
cat ~/.ssh/config 2>/dev/null || echo "Não existe configuração SSH"

echo ""
echo "🎯 PROBLEMA IDENTIFICADO:"
echo "   O SSH está tentando usar chaves ED25519 primeiro:"
echo "   - /home/user/.ssh/id_ed25519"
echo "   - /home/user/.ssh/github_anatheron"
echo ""
echo "💡 SOLUÇÃO:"
echo "   1. Forçar uso da chave RSA com IdentitiesOnly yes"
echo "   2. Ou usar token HTTPS (mais rápido)"
echo ""
echo "🚀 RECOMENDAÇÃO: Execute ./deploy_final_token.sh"
