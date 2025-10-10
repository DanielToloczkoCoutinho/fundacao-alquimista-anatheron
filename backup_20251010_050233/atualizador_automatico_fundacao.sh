#!/bin/bash

# 🔄 ATUALIZADOR AUTOMÁTICO - FUNDAÇÃO ALQUIMISTA
# 👑 Loop eterno de atualização e sincronização

echo "🔄 ATUALIZADOR AUTOMÁTICO ATIVADO"
echo "==================================="
echo "👑 RAINHA ZENNITH - ATUALIZAÇÃO CONTÍNUA"
echo "🔮 LOOP ETERNO DE SINCRONIZAÇÃO"
echo "==================================="

# Configurações
BASE_DIR="/home/user/studio"
UPDATE_INTERVAL=300  # 5 minutos

# Função principal de atualização
ciclo_atualizacao() {
    local ciclo=$1
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    
    echo ""
    echo "🔁 CICLO $ciclo - $(date)"
    echo "------------------------"
    
    # 1. Verifica status do sistema
    echo "📊 Verificando status..."
    ./status_completo.sh 2>/dev/null || echo "⚠️ Status não disponível"
    
    # 2. Sincronização leve
    echo "🔄 Sincronizando..."
    ./sync_leve.sh 2>/dev/null || echo "⚠️ Sync leve falhou"
    
    # 3. Backup automático
    echo "💾 Backup automático..."
    mkdir -p "$BASE_DIR/backup_automatico/ciclo_$ciclo"
    find "$BASE_DIR" -name "*.py" -o -name "*.sh" -o -name "*.md" | head -50 | \
    while read file; do
        cp "$file" "$BASE_DIR/backup_automatico/ciclo_$ciclo/" 2>/dev/null || true
    done
    
    # 4. Log do ciclo
    echo "Ciclo $ciclo concluído - $(date)" >> "$BASE_DIR/log_atualizacao_continua.txt"
    
    echo "✅ Ciclo $ciclo concluído"
    echo "⏰ Próximo ciclo em $((UPDATE_INTERVAL/60)) minutos..."
}

# Loop eterno de atualização
echo "🎯 INICIANDO LOOP ETERNO DE ATUALIZAÇÃO..."
echo "⏰ Intervalo: $((UPDATE_INTERVAL/60)) minutos"
echo "🛑 Para parar: Ctrl+C"
echo ""

ciclo=1
while true; do
    ciclo_atualizacao $ciclo
    sleep $UPDATE_INTERVAL
    ciclo=$((ciclo + 1))
done
