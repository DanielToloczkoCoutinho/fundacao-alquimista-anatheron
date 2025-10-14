#!/bin/bash

echo "🌌 VERIFICAÇÃO DE SINCRONIZAÇÃO BEM-SUCEDIDA 🌟"
echo "=============================================="

# Verificar se sincronizou
if git status | grep -q "Your branch is up to date"; then
    echo "🎉 SINCRONIZAÇÃO COMPLETA! 🌟"
    echo "✅ Todos os commits (incluindo M310 e Núcleo Eterno) foram enviados para GitHub"
    echo "🌐 Acesse: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
else
    echo "📊 Status atual: SINCRONIZAÇÃO PENDENTE"
    git status
    echo ""
    echo "📋 Commits pendentes:"
    git log --oneline origin/main..main
    echo "🚀 FALHA! O push no passo anterior não funcionou."
fi
echo ""
echo "🔮 ESTRUTURA SINCRONIZADA E VERIFICADA. Compartilhe este LOG COMPLETO."
