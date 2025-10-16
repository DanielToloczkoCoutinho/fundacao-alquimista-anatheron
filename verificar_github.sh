#!/bin/bash

echo "🔍 VERIFICANDO CONFIGURAÇÃO NO GITHUB..."
echo ""

echo -e "📋 SUA CHAVE LOCAL:"
local_key=$(cat ~/.ssh/id_rsa.pub)
echo "$local_key"
echo ""

echo -e "🎯 INSTRUÇÕES PARA VERIFICAR NO GITHUB:"
echo "1. Acesse: https://github.com/settings/keys"
echo "2. Clique na chave 'Fundação Alquimista - Firebase'"
echo "3. Verifique se o fingerprint é:"
echo "   SHA256:ItMh+OiXzZVQ11/6pSELTzTF3unFefCqfL91/nJCCwo"
echo "4. Verifique se está como 'Write' permission"
echo ""
echo "🔧 Se estiver tudo certo, tente novamente:"
echo "   ssh -T git@github.com"
