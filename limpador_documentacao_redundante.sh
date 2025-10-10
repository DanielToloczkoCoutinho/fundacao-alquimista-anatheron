#!/bin/bash
echo "📚 LIMPEZA INTELIGENTE DE DOCUMENTAÇÃO REDUNDANTE"
echo "================================================="

# 1. IDENTIFICAR DOCUMENTOS DUPLICADOS EXATOS
echo "🔍 Procurando documentos duplicados exatos:"
find . -name "*.md" -exec md5sum {} + | sort | uniq -w32 -d | head -5

# 2. ANALISAR BACKUPS REDUNDANTES
echo ""
echo "🔄 BACKUPS REDUNDANTES DE zennith_rainha.md:"
find . -name "zennith_rainha.md" -exec ls -la {} \; | head -5

# 3. ESTRATÉGIA DE LIMPEZA SEGURA
echo ""
echo "🎯 ESTRATÉGIA DE LIMPEZA:"
echo "   🔸 Manter versão mais recente em /docs/"
echo "   🔸 Compactar versões antigas em backups"
echo "   🔸 Manter histórico, mas reduzir duplicação"

# 4. AÇÃO SEGURA - COMPACTAÇÃO
echo ""
echo "🗜️ Compactando backups antigos (seguro):"
find backup_automatico -name "zennith_rainha.md" -mtime +7 -exec gzip {} \; 2>/dev/null
echo "✅ Backups antigos compactados"

# 5. VERIFICAR RESULTADO
echo ""
echo "📊 DOCUMENTAÇÃO APÓS OTIMIZAÇÃO:"
find . -name "*.md" | wc -l | xargs echo "  Total de documentos .md:"
find . -name "zennith_rainha.md" | wc -l | xargs echo "  Cópias de zennith_rainha.md:"
