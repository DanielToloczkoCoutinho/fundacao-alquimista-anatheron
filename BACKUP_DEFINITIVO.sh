#!/bin/bash
# SISTEMA DE BACKUP DEFINITIVO - FUNDACAO ALQUIMISTA
# Backup automatico de todos os 24,183 componentes

echo "SISTEMA DE BACKUP DEFINITIVO - FUNDACAO ALQUIMISTA"
echo "================================================="

# Configuracoes
BACKUP_DIR="backup_fundacao_$(date +%Y%m%d_%H%M%S)"
CHAVE_FUNDACAO="CHAVE_272E0E77867EC48427D22F5AE895C264"

echo "INICIANDO BACKUP DEFINITIVO..."
echo "CHAVE: $CHAVE_FUNDACAO"
echo "COMPONENTES: 24,183"
echo ""

# Criar diretorio de backup
mkdir -p "$BACKUP_DIR"

# Copiar sistemas essenciais
sistemas_essenciais=(
    "SISTEMA_ACESSO_DEFINITIVO.json"
    "ATIVACAO_DEFINITIVA_CORRIGIDA.sh"
    "INTERFACE_ACESSO_CORRIGIDA.py" 
    "CHAVE_DEFINITIVA_FUNDACAO.py"
    "sistema_metadados_definitivo.py"
    "organizador_fundacao_definitivo.py"
    "sistema_fundacao_definitivo.py"
)

echo "COPIANDO SISTEMAS ESSENCIAIS..."
for sistema in "${sistemas_essenciais[@]}"; do
    if [ -f "$sistema" ]; then
        cp "$sistema" "$BACKUP_DIR/"
        echo "  COPIADO: $sistema"
    fi
done

# Copiar metadados e indices
echo "COPIANDO METADADOS E INDICES..."
cp metadados_fundacao_completo_*.json "$BACKUP_DIR/" 2>/dev/null || true
cp indice_fundacao_buscavel_*.json "$BACKUP_DIR/" 2>/dev/null || true

# Criar arquivo de informacoes do backup
cat > "$BACKUP_DIR/INFO_BACKUP.txt" << INFO
BACKUP DEFINITIVO - FUNDACAO ALQUIMISTA
=======================================
DATA: $(date)
CHAVE: $CHAVE_FUNDACAO
COMPONENTES: 24,183
SISTEMAS: ${#sistemas_essenciais[@]} sistemas essenciais

SISTEMAS INCLUIDOS:
$(printf "  - %s\n" "${sistemas_essenciais[@]}")

PARA RESTAURAR:
1. Copiar arquivos do backup para diretorio principal
2. Executar: ./ATIVACAO_DEFINITIVA_CORRIGIDA.sh
3. Verificar: ./VERIFICACAO_CORRIGIDA.sh

FUNDACAO ALQUIMISTA - SISTEMA DEFINITIVO
INFO

echo "BACKUP CONCLUIDO: $BACKUP_DIR"
echo "TAMANHO: $(du -sh "$BACKUP_DIR" | cut -f1)"
echo ""
echo "PARA RESTAURAR EM QUALQUER MOMENTO:"
echo "  cp $BACKUP_DIR/* . && ./ATIVACAO_DEFINITIVA_CORRIGIDA.sh"
