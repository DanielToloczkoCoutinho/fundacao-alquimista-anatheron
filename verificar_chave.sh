#!/bin/bash

echo "🔍 VERIFICANDO CHAVE SSH..."
echo ""

# Verificar se chave existe
if [ -f ~/.ssh/id_rsa.pub ]; then
    echo "✅ CHAVE ENCONTRADA:"
    echo "📍 Local: ~/.ssh/id_rsa.pub"
    echo "📏 Tamanho: $(wc -c < ~/.ssh/id_rsa.pub) caracteres"
    echo ""
    echo "📋 CONTEÚDO EXATO:"
    cat ~/.ssh/id_rsa.pub
else
    echo "❌ CHAVE NÃO ENCONTRADA"
    echo "💡 Execute: ./configurar_ssh_final.sh"
fi

echo ""
echo "🎯 COMPARE COM A CHAVE ACIMA - DEVEM SER IDÊNTICAS!"
