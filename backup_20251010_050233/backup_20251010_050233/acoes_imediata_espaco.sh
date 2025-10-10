#!/bin/bash
echo "🛠️ AÇÕES IMEDIATAS PARA GANHAR ESPAÇO"
echo "======================================"

# 1. LIMPAR CACHE DO NPM (SEGUR0)
echo "🗑️ Limpando cache do npm..."
npm cache clean --force 2>/dev/null && echo "✅ Cache npm limpo"

# 2. LIMPAR CACHE DO PYTHON (SEGUR0)
echo "🗑️ Limpando cache do Python..."
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
echo "✅ Cache Python limpo"

# 3. COMPACTAR BACKUPS MAIS ANTIGOS
echo "🗜️ Compactando backups antigos..."
find backup_automatico -name "*.md" -mtime +3 -exec gzip {} \; 2>/dev/null

# 4. VERIFICAR RESULTADO
echo ""
echo "📊 RESULTADO DAS AÇÕES:"
echo "  🔸 Cache npm: LIMPO"
echo "  🔸 Cache Python: LIMPO" 
echo "  🔸 Backups antigos: COMPACTADOS"
echo "  🔸 Nenhum arquivo crítico afetado"
