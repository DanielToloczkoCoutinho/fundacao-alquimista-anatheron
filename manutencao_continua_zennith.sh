#!/bin/bash
echo "🔄 SISTEMA DE MANUTENÇÃO CONTÍNUA ZENNITH"
echo "========================================="

# VERIFICAR SAÚDE DO SISTEMA PERIODICAMENTE
verificar_saude_sistema() {
    echo "🔍 VERIFICAÇÃO DE SAÚDE - $(date)"
    echo "================================"
    
    # Verificar logs
    echo "📊 Sistema de Log:"
    find . -name "*.log" -mtime -1 | wc -l | xargs echo "  Logs últimos 24h:"
    
    # Verificar funções core
    echo "🔧 Funções Core:"
    grep -r "function\|def " utils_zennith_*.sh 2>/dev/null | wc -l | xargs echo "  Funções disponíveis:"
    
    # Verificar espaço
    echo "💾 Espaço em Disco:"
    du -sh . | awk '{print "  " $1}'
    
    echo "✅ Verificação concluída"
}

# EXECUTAR MANUTENÇÃO AUTOMÁTICA
executar_manutencao() {
    echo "🛠️ EXECUTANDO MANUTENÇÃO AUTOMÁTICA"
    echo "================================="
    
    # Limpar caches
    find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
    echo "✅ Cache Python limpo"
    
    # Compactar logs antigos
    find . -name "*.log" -mtime +7 -exec gzip {} \; 2>/dev/null
    echo "✅ Logs antigos compactados"
    
    # Verificar integridade
    echo "🔍 Verificando integridade do sistema..."
    for script in utils_zennith_log_avancado.sh utils_zennith_processamento.sh; do
        if [[ -f "$script" ]]; then
            echo "✅ $script: OK"
        else
            echo "❌ $script: AUSENTE"
        fi
    done
    
    echo "�� Manutenção concluída"
}

# MENU PRINCIPAL
case "${1:-verificar}" in
    "verificar")
        verificar_saude_sistema
        ;;
    "manutencao")
        executar_manutencao
        ;;
    *)
        echo "Uso: $0 [verificar|manutencao]"
        ;;
esac
