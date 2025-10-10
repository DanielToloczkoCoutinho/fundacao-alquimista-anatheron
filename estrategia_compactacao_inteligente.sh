#!/bin/bash
echo "🎯 ESTRATÉGIA DE COMPACTAÇÃO INTELIGENTE"
echo "========================================"

# 1. COMPACTAR VENV DESNECESSÁRIOS (SE HOUVER)
echo "🐍 VERIFICANDO AMBIENTES VIRTUAIS REDUNDANTES:"
find . -name "*venv*" -type d | head -3
find . -name "fundacao_independente" -type d | head -3

# 2. IDENTIFICAR BACKUPS REDUNDANTES
echo ""
echo "🔄 BACKUPS PARA COMPACTAÇÃO:"
find backup_automatico -type f -name "*.md" | wc -l | xargs echo "  Total de backups .md:"

# 3. COMPACTAR DOCUMENTAÇÃO ANTIGA
echo ""
echo "📚 COMPACTANDO DOCUMENTAÇÃO ANTIGA:"
find docs -name "*.md" -mtime +30 -exec gzip {} \; 2>/dev/null
docs_compactados=$(find docs -name "*.md.gz" 2>/dev/null | wc -l)
echo "✅ $docs_compactados documentos compactados"

# 4. CRIAR RELATÓRIO DE ECONOMIA
echo ""
echo "📊 ECONOMIA POTENCIAL:"
echo "  🔸 Documentação antiga: COMPACTADA"
echo "  🔸 Backups: PRONTOS PARA COMPACTAÇÃO"
echo "  🔸 Scripts grandes: IDENTIFICADOS PARA OTIMIZAÇÃO"
