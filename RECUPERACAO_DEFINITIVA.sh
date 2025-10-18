#!/bin/bash
# SISTEMA DE RECUPERACAO DEFINITIVA - FUNDACAO ALQUIMISTA
# Recuperacao automatica em caso de problemas

echo "SISTEMA DE RECUPERACAO DEFINITIVA - FUNDACAO ALQUIMISTA"
echo "======================================================"

# Encontrar backup mais recente
BACKUP_RECENTE=$(ls -d backup_fundacao_* 2>/dev/null | sort -r | head -1)

if [ -z "$BACKUP_RECENTE" ]; then
    echo "NENHUM BACKUP ENCONTRADO"
    echo "Execute primeiro: ./BACKUP_DEFINITIVO.sh"
    exit 1
fi

echo "BACKUP ENCONTRADO: $BACKUP_RECENTE"
echo "INICIANDO RECUPERACAO..."
echo ""

# Verificar integridade do backup
if [ ! -f "$BACKUP_RECENTE/SISTEMA_ACESSO_DEFINITIVO.json" ]; then
    echo "BACKUP CORROMPIDO: SISTEMA_ACESSO_DEFINITIVO.json nao encontrado"
    exit 1
fi

# Copiar arquivos de volta
echo "RESTAURANDO SISTEMAS..."
cp "$BACKUP_RECENTE"/* . 2>/dev/null || true

# Restaurar permissoes
chmod +x ATIVACAO_DEFINITIVA_CORRIGIDA.sh
chmod +x INTERFACE_ACESSO_CORRIGIDA.py
chmod +x VERIFICACAO_CORRIGIDA.sh

echo "RECUPERACAO CONCLUIDA!"
echo ""

# Verificar sistema
echo "VERIFICANDO SISTEMA RECUPERADO..."
./VERIFICACAO_CORRIGIDA.sh
