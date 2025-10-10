#!/bin/bash
echo "🔄 MANUTENÇÃO AUTOMÁTICA ZENNITH M29"

# Limpar caches semanalmente
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
npm cache clean --force 2>/dev/null

# Compactar backups antigos automaticamente
find backup_automatico -name "*.md" -mtime +7 -exec gzip {} \; 2>/dev/null

# Verificar espaço economizado
echo "✅ Manutenção realizada: $(date)"
