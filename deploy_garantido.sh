#!/bin/bash

echo "🚀 DEPLOY GARANTIDO - FUNDAÇÃO ALQUIMISTA"
echo "========================================="

# Tentar SSH primeiro
echo "🔑 Tentando com SSH..."
if git push -u origin main; then
    echo "🎉 Sucesso via SSH!"
    ./celebrar_deploy.sh
    exit 0
fi

# Se falhar, pedir token
echo "🔐 SSH falhou, usando token..."
echo ""
read -p "🔑 Cole seu token GitHub: " token

if [ -n "$token" ]; then
    echo "📤 Enviando com token..."
    git push https://${token}@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main
    
    if [ $? -eq 0 ]; then
        ./celebrar_deploy.sh
    else
        echo "❌ Erro. Verifique o token e tente novamente."
    fi
else
    echo "❌ Nenhum token fornecido."
fi
