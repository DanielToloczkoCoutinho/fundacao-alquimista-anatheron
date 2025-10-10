#!/bin/bash
echo "📦 COMPACTADOR INTELIGENTE - MÓDULO 9"
echo "======================================"
echo "🎯 Compressão sem perda de dados"
echo ""

# 1. COMPACTAR LOGS ANTIGOS
echo "🗜️ COMPACTANDO LOGS ANTIGOS..."
find . -name "*.log" -mtime +7 -exec gzip {} \; 2>/dev/null
echo "✅ Logs antigos compactados"

# 2. COMPACTAR BACKUPS REDUNDANTES
echo "🗜️ COMPACTANDO BACKUPS REDUNDANTES..."
find backup_automatico -name "*.md" -o -name "*.txt" -exec gzip {} \; 2>/dev/null
echo "✅ Backups compactados"

# 3. CRIAR ARQUIVO COMPACTO PARA GIT
echo "📦 CRIANDO PACOTE GIT COMPACTO..."
tar -czf sistema_zenith_compacto_$(date +%Y%m%d_%H%M%S).tar.gz \
    laboratorios_hierarquicos/ \
    SCRIPTS_CENTRALIZADOS/ \
    FUNDACAO_ORGANIZADA_DEFINITIVA/ \
    --exclude="*.log" --exclude="*.tmp" 2>/dev/null
echo "✅ Pacote Git criado"

# 4. VERIFICAR GANHO DE ESPAÇO
echo ""
echo "📊 ESPAÇO LIBERADO:"
du -sh . before_compact/
