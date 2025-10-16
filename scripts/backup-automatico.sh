#!/bin/bash
echo "💾 BACKUP AUTOMÁTICO INICIADO..."

cd ~/fundacao-definitiva

# Criar backup com timestamp
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
BACKUP_DIR="trabalho/backups/auto_$TIMESTAMP"

mkdir -p "$BACKUP_DIR"

# Backup dos arquivos essenciais
cp -r app/ "$BACKUP_DIR/"
cp -r scripts/ "$BACKUP_DIR/" 
cp -r config/ "$BACKUP_DIR/"
cp -r docs/ "$BACKUP_DIR/"

# Compactar backup
tar -czf "$BACKUP_DIR.tar.gz" "$BACKUP_DIR"
rm -rf "$BACKUP_DIR"

# Manter apenas últimos 5 backups
ls -t trabalho/backups/auto_*.tar.gz | tail -n +6 | xargs rm -f

echo "✅ BACKUP CRIADO: $BACKUP_DIR.tar.gz"
