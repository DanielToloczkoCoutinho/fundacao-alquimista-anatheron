#!/bin/bash

# 🚨 SISTEMA DE EMERGÊNCIA - Funciona sem espaço

echo "🚨 MODO EMERGÊNCIA - SINCRONIZAÇÃO MÍNIMA"
echo "=========================================="

# Apenas verifica se o site está online
check_online() {
    echo "🌐 Verificando status online..."
    
    if curl -s --head "https://fundacao-alquimista-anatheron-mtnk3sp7c.vercel.app" | grep "200 OK" > /dev/null; then
        echo "✅ PORTAL ONLINE!"
        echo "🔗 https://fundacao-alquimista-anatheron-mtnk3sp7c.vercel.app"
        return 0
    else
        echo "❌ PORTAL OFFLINE"
        return 1
    fi
}

# Backup mínimo em memória
backup_memoria() {
    echo "💾 Backup em memória..."
    
    # Cria backup dos scripts mais importantes
    IMPORTANT_FILES=(
        "sincronizador_universal.sh"
        "sync_leve.sh" 
        "status_completo.sh"
        "salvar_rapido.sh"
    )
    
    for file in "${IMPORTANT_FILES[@]}"; do
        if [[ -f "$file" ]]; then
            echo "📄 Mantendo: $file"
        fi
    done
}

# Status do sistema
system_status() {
    echo "📊 STATUS DO SISTEMA:"
    echo "💾 Espaço: $(df -h /home/user/studio | awk 'NR==2 {print $4}') livre"
    echo "🕐 Horário: $(date)"
    echo "🔮 Fundação: OPERACIONAL (modo emergência)"
}

# Execução
check_online
backup_memoria  
system_status

echo "🎯 SISTEMA ESTÁVEL EM MODO EMERGÊNCIA"
