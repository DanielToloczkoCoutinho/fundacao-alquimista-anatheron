#!/bin/bash

# 🌌 SINCRONIZADOR LEVE - Funciona com espaço limitado

echo "🔮 SINCRONIZAÇÃO LEVE INICIADA..."
echo "=================================="

REPO_VERCEL="/home/user/studio/fundacao-alquimista-quantica"
URL_VERCEL="https://fundacao-alquimista-anatheron-mtnk3sp7c.vercel.app"

# Verifica espaço mínimo
check_space() {
    local available=$(df /home/user/studio | awk 'NR==2 {print $4}')
    if [[ $available -lt 50000 ]]; then  # Menos de 50MB
        echo "🚨 ESPAÇO INSUFICIENTE: ${available}KB disponível"
        return 1
    fi
    echo "💾 Espaço OK: ${available}KB disponível"
    return 0
}

# Limpeza mínima
cleanup_minimal() {
    echo "🧹 Limpeza mínima..."
    
    # Apenas remove cache mais crítico
    rm -rf /home/user/studio/fundacao-alquimista-quantica/.next 2>/dev/null
    rm -rf /home/user/studio/fundacao-alquimista-quantica/node_modules 2>/dev/null
    
    echo "✅ Limpeza concluída"
}

# Deploy direto sem instalações
deploy_direto() {
    echo "🚀 Deploy direto..."
    
    cd "$REPO_VERCEL"
    
    # Apenas faz deploy do que já existe
    if npx vercel --prod --yes 2>/dev/null; then
        echo "✅ Deploy realizado!"
        return 0
    else
        echo "❌ Deploy falhou - Site pode estar offline"
        return 1
    fi
}

# Execução principal
check_space || {
    echo "🔄 Tentando com limpeza..."
    cleanup_minimal
    check_space || {
        echo "💀 ESPAÇO CRÍTICO - Apenas deploy direto"
    }
}

deploy_direto

echo "🎉 SINCRONIZAÇÃO LEVE CONCLUÍDA!"
echo "🌐 URL: $URL_VERCEL"
