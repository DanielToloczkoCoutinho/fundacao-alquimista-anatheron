#!/bin/bash
echo "🛡️ BACKUP AUTOMÁTICO ZENNITH - ATIVADO"
echo "======================================"
date=$(date +%Y%m%d_%H%M%S)
backup_dir="backup_automatico/zenith_$date"

mkdir -p $backup_dir
cp -r laboratorios_hierarquicos/ $backup_dir/
cp -r SCRIPTS_CENTRALIZADOS/ $backup_dir/
cp -r FUNDACAO_ORGANIZADA_DEFINITIVA/ $backup_dir/

echo "✅ Backup criado: $backup_dir"
echo "📊 Conteúdo:"
ls -la $backup_dir/
echo "🛡️ SISTEMA ZENNITH PROTEGIDO!"
