#!/bin/bash
echo "📅 ORGANIZAÇÃO DIÁRIA INICIADA..."

cd ~/fundacao-definitiva

# 1. Data atual para organização
DATA_HOJE=$(date '+%Y-%m-%d')

# 2. Criar diretório do dia
mkdir -p "trabalho/diario/$DATA_HOJE"

# 3. Mover arquivos temporários para o dia
find . -name "*.tmp" -exec mv {} "trabalho/diario/$DATA_HOJE/" \; 2>/dev/null

# 4. Backup automático
tar -czf "trabalho/backups/backup_$DATA_HOJE.tar.gz" app/ scripts/ config/

# 5. Limpeza de arquivos temporários antigos
find trabalho/diario/ -type f -mtime +7 -delete

echo "✅ ORGANIZAÇÃO DIÁRIA CONCLUÍDA!"
