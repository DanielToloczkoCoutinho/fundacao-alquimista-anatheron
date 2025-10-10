#!/bin/bash

# 🔮 ATIVADOR AUTOMÁTICO - Monitora mudanças e sincroniza automaticamente

MONITOR_DIR="/home/user/studio"
SYNC_SCRIPT="/home/user/studio/sincronizador_universal.sh"
LOG_FILE="/home/user/studio/log_sincronizacao.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

monitorar_mudancas() {
    log "🔮 INICIANDO MONITORAMENTO AUTOMÁTICO..."
    
    # Monitora arquivos .py, .js, .ts, .json, .md
    inotifywait -m -r -e modify,create,delete --include='\.(py|js|ts|json|md|sh)$' "$MONITOR_DIR" |
    while read path action file; do
        # Ignora diretórios do sistema
        if [[ "$path" == *".git"* ]] || [[ "$path" == *"node_modules"* ]] || [[ "$path" == *".next"* ]]; then
            continue
        fi
        
        log "📁 Mudança detectada: $action em $path$file"
        
        # Espera 2 segundos para agrupar mudanças
        sleep 2
        
        # Executa sincronização rápida
        log "⚡ Executando sincronização rápida..."
        "$SYNC_SCRIPT" rapida
    done
}

# Verifica se inotifywait está instalado
if ! command -v inotifywait &> /dev/null; then
    echo "❌ inotifywait não encontrado. Instale com: sudo apt-get install inotify-tools"
    exit 1
fi

# Inicia monitoramento
echo "🎯 Ativador Automático Iniciado..."
echo "📁 Monitorando: $MONITOR_DIR"
echo "📝 Log: $LOG_FILE"
echo "🛑 Para parar: Ctrl+C"

monitorar_mudancas
