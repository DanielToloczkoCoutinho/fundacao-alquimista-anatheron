#!/bin/bash
echo "🔄 MIGRADOR SEGURO - FUNÇÃO LOG UNIFICADA"
echo "=========================================="

# 1. ANALISAR AS 3 IMPLEMENTAÇÕES DE LOG
echo "🔍 Analisando implementações atuais de log():"

echo ""
echo "📄 organizador_universal_fundacao.sh (linha 24):"
sed -n '24,30p' organizador_universal_fundacao.sh

echo ""
echo "📄 sistema_governanca_zennith.sh (linha 21):" 
sed -n '21,27p' sistema_governanca_zennith.sh

echo ""
echo "📄 analisador_zennith.sh (linha 19):"
sed -n '19,25p' analisador_zennith.sh

# 2. CRIAR FUNÇÃO LOG UNIFICADA SUPERIOR
echo ""
echo "🆙 Criando função log unificada melhorada..."

cat > utils_zennith_log_avancado.sh << 'LOGAVANCADOEOF'
#!/bin/bash
# 🧠 UTILS_ZENNITH_LOG - Sistema de Log Unificado Avançado
# =======================================================

# CONFIGURAÇÕES DE LOG
ZENNITH_LOG_LEVEL="${ZENNITH_LOG_LEVEL:-INFO}"  # DEBUG, INFO, WARN, ERROR
ZENNITH_LOG_FILE="${ZENNITH_LOG_FILE:-/tmp/zennith_system.log}"

# FUNÇÃO LOG UNIFICADA AVANÇADA
log_zennith() {
    local level="INFO"
    local message="$1"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Determinar nível se especificado
    if [[ "$1" =~ ^(DEBUG|INFO|WARN|ERROR): ]]; then
        level="${BASH_REMATCH[1]}"
        message="${message#*: }"
    fi
    
    # Verificar se o nível é suficiente para log
    case "$ZENNITH_LOG_LEVEL" in
        DEBUG) ;;
        INFO) [[ "$level" =~ (DEBUG) ]] && return ;;
        WARN) [[ "$level" =~ (DEBUG|INFO) ]] && return ;;
        ERROR) [[ "$level" =~ (DEBUG|INFO|WARN) ]] && return ;;
    esac
    
    # Formatar saída
    local log_entry="[ZENNITH $timestamp $level] $message"
    
    # Saída para console
    echo "$log_entry"
    
    # Saída para arquivo se configurado
    if [[ -n "$ZENNITH_LOG_FILE" ]]; then
        echo "$log_entry" >> "$ZENNITH_LOG_FILE"
    fi
}

# FUNÇÕES ESPECIALIZADAS
log_info() { log_zennith "INFO: $1"; }
log_warn() { log_zennith "WARN: $1"; }
log_error() { log_zennith "ERROR: $1"; }
log_debug() { log_zennith "DEBUG: $1"; }

# FUNÇÃO DE RELATÓRIO DE SISTEMA
log_system_report() {
    log_info "=== RELATÓRIO DE SISTEMA ZENNITH ==="
    log_info "Data/Hora: $(date)"
    log_info "Usuário: $(whoami)"
    log_info "Diretório: $(pwd)"
    log_info "Script: $0"
    log_info "====================================="
}

# VERIFICAR E CARREGAR
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Execução direta - testar
    log_zennith "TESTE: Sistema de log Zennith carregado com sucesso"
    log_info "Mensagem informativa"
    log_warn "Mensagem de aviso" 
    log_error "Mensagem de erro"
    log_debug "Mensagem de debug"
else
    # Sourced - apenas carregar
    log_zennith "DEBUG: Utils Zennith Log carregado como library"
fi

export -f log_zennith log_info log_warn log_error log_debug log_system_report
LOGAVANCADOEOF

echo "✅ Sistema de log avançado criado"

# 3. MIGRADOR AUTOMÁTICO SEGURO
echo ""
echo "🛡️ Executando migração segura das funções log..."

# Backup primeiro
cp organizador_universal_fundacao.sh organizador_universal_fundacao.sh.pre_log_migration
cp sistema_governanca_zennith.sh sistema_governanca_zennith.sh.pre_log_migration
cp analisador_zennith.sh analisador_zennith.sh.pre_log_migration

# Substituir chamadas de log
for script in organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh; do
    echo "🔧 Migrando $script..."
    
    # Remover função log original e substituir chamadas
    sed -i '24,30d' "$script"  # Remove função log original
    sed -i 's/log "/log_zennith "/g' "$script"  # Substitui chamadas
    
    # Adicionar import no topo
    sed -i '1i\source utils_zennith_log_avancado.sh' "$script"
    
    echo "✅ $script migrado"
done

# 4. VERIFICAR MIGRAÇÃO
echo ""
echo "🔍 Verificando migração..."
for script in organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh; do
    echo "📄 $script:"
    echo "  Função log removida: $(grep -c "log() {" "$script")"
    echo "  Chamadas log_zennith: $(grep -c "log_zennith" "$script")"
done

echo ""
echo "🎯 MIGRAÇÃO DE LOG CONCLUÍDA!"
