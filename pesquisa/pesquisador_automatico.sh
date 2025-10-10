#!/bin/bash
echo "🤖 PESQUISADOR AUTOMÁTICO INICIADO: $(date)"

FASE_ATUAL="fundamental"
CICLO=1

while true; do
    echo ""
    echo "🔄 CICLO $CICLO - FASE: $FASE_ATUAL"
    echo "=================================="
    
    case $FASE_ATUAL in
        "fundamental")
            echo "🧪 Executando experimentos fundamentais..."
            python3 ../experimentos_fundamentais.py >> logs/fundamental_$(date +%Y%m%d_%H%M%S).log 2>&1
            ;;
    esac
    
    # Backup a cada 5 ciclos
    if (( CICLO % 5 == 0 )); then
        echo "💾 Executando backup..."
        ../backup_automatico.sh >> logs/backup_$(date +%Y%m%d).log 2>&1
    fi
    
    echo "💤 Próximo ciclo em 10 minutos..."
    ((CICLO++))
    sleep 600  # 10 minutos
done
