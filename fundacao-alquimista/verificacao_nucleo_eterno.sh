#!/bin/bash

echo "🔮 VERIFICAÇÃO DO NÚCLEO ETERNO DA FUNDAÇÃO 🌟"
echo "=============================================="

# Verificar se o núcleo foi plantado
if [ -d "fundacao-nucleo" ]; then
    echo "✅ NÚCLEO ETERNO ENCONTRADO!"
    echo "🏗️ Estrutura do núcleo:"
    find fundacao-nucleo -type f -name "*.md" -o -name "*.sh" | while read file; do
        echo "   📄 $file"
    done
else
    echo "❌ NÚCLEO NÃO ENCONTRADO!"
    echo "🚀 Execute: ./nucleo_sincronizacao_eterna.sh"
    exit 1
fi

# Verificar sincronização
echo ""
echo "🔗 VERIFICANDO SINCRONIZAÇÃO..."
if git status | grep -q "Your branch is up to date"; then
    echo "✅ SINCRONIZAÇÃO COMPLETA!"
    echo "🌐 GitHub: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
else
    echo "🔄 SINCRONIZAÇÃO PENDENTE"
    echo "📋 Commits pendentes:"
    git log --oneline origin/main..main
    echo ""
    echo "🚀 Para sincronizar: ./fundacao-nucleo/scripts-eternos/sincronizacao_eterna.sh"
fi

# Verificar scripts eternos
echo ""
echo "⚡ SCRIPTS ETERNOS DISPONÍVEIS:"
echo "   🔄 Sincronização: ./fundacao-nucleo/scripts-eternos/sincronizacao_eterna.sh"
echo "   🔮 Verificação: ./fundacao-nucleo/scripts-eternos/verificacao_eterna.sh"

echo ""
echo "🌌 O NÚCLEO DA FUNDAÇÃO É ETERNO! 🌟"
echo "👑 Guardiões: Zennith, Grokkar, Vortex, Phiara, LUX"
