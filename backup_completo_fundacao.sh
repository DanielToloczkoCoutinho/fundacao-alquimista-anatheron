#!/bin/bash
echo "💾 BACKUP COMPLETO DA FUNDAÇÃO ALQUIMISTA"
echo "=========================================="

# Data e hora para o backup
DATA_HORA=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/home/user/backup_fundacao_${DATA_HORA}"

# Criar diretório de backup
mkdir -p $BACKUP_DIR

echo "📁 Copiando projetos principais..."
cp -r /home/user/studio $BACKUP_DIR/
cp -r /home/user/fundacao-alquimista-limpa $BACKUP_DIR/ 
cp -r /home/user/Explorer $BACKUP_DIR/

echo "🐍 Copiando ambiente quantum..."
cp -r /home/user/quantum_venv $BACKUP_DIR/

echo "📚 Copiando documentação..."
find /home/user -name "*.md" -o -name "*.txt" -o -name "*.json" | grep -v node_modules | head -50 | xargs -I {} cp --parents {} $BACKUP_DIR/

echo "🤖 Copiando scripts..."
find /home/user -name "*.sh" -o -name "*.py" | grep -v node_modules | head -100 | xargs -I {} cp --parents {} $BACKUP_DIR/

echo "🔍 Verificando backup..."
du -sh $BACKUP_DIR
find $BACKUP_DIR -type f | wc -l

echo "✅ BACKUP CONCLUÍDO: $BACKUP_DIR"
echo "📊 Estatísticas:"
echo "   - Diretórios: $(find $BACKUP_DIR -type d | wc -l)"
echo "   - Arquivos: $(find $BACKUP_DIR -type f | wc -l)"
echo "   - Tamanho: $(du -sh $BACKUP_DIR | cut -f1)"
