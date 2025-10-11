#!/bin/bash

echo "🔮 SISTEMA DE BACKUP QUÂNTICO - FUNDAÇÃO ALQUIMISTA"
echo "==================================================="
echo "💫 Iniciando backup multidimensional do sistema..."
echo ""

# Configurações
BACKUP_DIR="backups_quanticos"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_alquimista_${TIMESTAMP}.tar.gz"

# Criar diretório de backup
mkdir -p "$BACKUP_DIR"

echo "📦 IDENTIFICANDO ARQUIVOS CRÍTICOS..."
# Lista de arquivos para backup
find . -type f \( -name "*.js" -o -name "*.json" -o -name "*.md" -o -name "*.sh" \) | head -20 > lista_backup.txt

# Criar backup
echo "🔄 CRIANDO BACKUP COMPACTO..."
tar -czf "${BACKUP_DIR}/${BACKUP_FILE}" -T lista_backup.txt 2>/dev/null

if [ $? -eq 0 ]; then
    echo "✅ BACKUP CONCLUÍDO: ${BACKUP_DIR}/${BACKUP_FILE}"
    echo "📊 Tamanho: $(du -h "${BACKUP_DIR}/${BACKUP_FILE}" | cut -f1)"
    echo "🛡️ Sistema protegido contra colapsos dimensionais"
else
    echo "❌ ERRO NO BACKUP"
    exit 1
fi

# Metadados do backup
cat > "${BACKUP_DIR}/metadados_${TIMESTAMP}.json" << METADATAEOF
{
  "sistema": "Alquimista Cósmico",
  "timestamp": "$(date -Iseconds)",
  "backup_file": "${BACKUP_FILE}",
  "tamanho": "$(du -h "${BACKUP_DIR}/${BACKUP_FILE}" | cut -f1)",
  "arquivos": $(wc -l < lista_backup.txt),
  "status": "protegido"
}
METADATAEOF

echo "📄 Metadados salvos: ${BACKUP_DIR}/metadados_${TIMESTAMP}.json"
echo "🎉 BACKUP QUÂNTICO CONCLUÍDO COM SUCESSO!"
