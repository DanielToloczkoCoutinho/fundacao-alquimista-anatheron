#!/bin/bash
echo "🔄 SISTEMA DE ATUALIZAÇÃO CONTÍNUA DE METADADOS"
echo "=============================================="

while true; do
    echo ""
    echo "$(date): 🔄 Atualizando metadados..."
    
    # SINCRONIZAR COM A BASE
    cd /home/user
    python refletor_tapecaria_viva.py
    
    # ATUALIZAR PÁGINAS
    cd /home/user/studio
    
    # FAZER DEPLOY AUTOMÁTICO
    git add app/verdade-real/page.js app/metadados-reais/page.js
    git commit -m "🔄 UPDATE: Metadados vivos $(date '+%Y-%m-%d %H:%M:%S')" > /dev/null 2>&1
    git push origin main > /dev/null 2>&1
    
    echo "✅ Metadados atualizados e deploy realizado"
    echo "⏰ Próxima atualização em 5 minutos..."
    
    sleep 300  # 5 minutos
done
