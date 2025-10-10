#!/bin/bash
# 🎨 ANALISADOR FRONTEND DIRETO  
echo "🎨 ANALISANDO FRONTEND (14,463 arquivos)..."
echo "📊 Total JS/TS: $(find /home/user/studio -name "*.js" -o -name "*.ts" -o -name "*.tsx" | wc -l)"
echo "🎯 Amostra React:"
find /home/user/studio -name "*.tsx" | head -5
echo "✅ Frontend analisado diretamente!"
