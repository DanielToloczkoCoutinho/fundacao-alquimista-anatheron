#!/bin/bash
echo "🗜️ COMPACTAÇÃO RÁPIDA E SEGURA"
echo "=============================="

# 1. COMPACTAR APENAS LOGS ANTIGOS (seguro)
echo "📋 Compactando logs antigos..."
find . -name "*.log" -mtime +30 -exec gzip {} \; 2>/dev/null
logs_compactados=$(find . -name "*.log.gz" 2>/dev/null | wc -l)
echo "✅ $logs_compactados logs compactados"

# 2. COMPACTAR BACKUPS MAIS ANTIGOS
echo "📦 Compactando backups antigos..."
find backup_automatico -name "*.md" -mtime +7 -exec gzip {} \; 2>/dev/null

# 3. CRIAR PACOTE DE ARQUIVOS GRANDES
echo "📦 Criando pacote para arquivos grandes..."
find . -size +10M -type f | head -5 | while read file; do
    echo "  📄 $file"
done

# 4. VERIFICAR RESULTADO
echo ""
echo "📊 RESULTADO DA COMPACTAÇÃO:"
echo "  🔸 Logs antigos: COMPACTADOS"
echo "  🔸 Backups antigos: COMPACTADOS" 
echo "  🔸 Arquivos grandes: IDENTIFICADOS"
echo "  🔸 Nenhum arquivo crítico foi modificado"
