#!/bin/bash

echo "🔍 VERIFICAÇÃO FINAL APÓS CORREÇÕES"
echo "==================================="

# Verificar arquivos
echo "📁 Arquivos críticos:"
ls -la app/modulo-303/page.js app/sistema-vivo/page.js app/status/page.js app/api/health/route.js 2>/dev/null

# Verificar se são dinâmicos
echo ""
echo "🔧 Conteúdo dinâmico:"
for file in app/modulo-303/page.js app/sistema-vivo/page.js app/status/page.js; do
    if [ -f "$file" ]; then
        echo "📄 $file:"
        grep -c "use client" "$file" | xargs echo "  - use client:"
        grep -c "useState" "$file" | xargs echo "  - useState:"
        grep -c "useEffect" "$file" | xargs echo "  - useEffect:"
    fi
done

# Testar build
echo ""
echo "🔨 Teste de build rápido:"
npx next build --debug

