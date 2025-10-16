#!/bin/bash

echo "🚀 DEPLOY AGORA - FUNDAÇÃO ALQUIMISTA"
echo "======================================"

# Force push simples
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 PRONTO! ACESSE:"
    echo "   https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
    echo ""
    echo "🌐 Vercel: https://fundacao-alquimista-anatheron.vercel.app"
else
    echo "❌ Erro. Use: git push -u origin main --force"
fi
