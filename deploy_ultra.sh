#!/bin/bash

echo "🚀 DEPLOY ULTRA-SIMPLES"
echo "======================"

read -p "🔑 Cole seu token GitHub: " token

echo "📤 Enviando..."
git push https://${token}@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git main

if [ $? -eq 0 ]; then
    echo "🎉 PRONTO! Acesse:"
    echo "   https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
else
    echo "❌ Erro. Verifique o token."
fi
