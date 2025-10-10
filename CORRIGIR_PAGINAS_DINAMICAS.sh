#!/bin/bash

echo "🔄 CORRIGINDO PÁGINAS PARA DINÂMICAS"
echo "==================================="

# Adicionar export dynamic nas páginas principais
for pagina in central modulo-303 sistema-vivo status; do
    if [ -f "app/$pagina/page.js" ]; then
        echo "🔧 Corrigindo $pagina..."
        # Verificar se já tem o export dynamic
        if ! grep -q "export const dynamic" "app/$pagina/page.js"; then
            # Adicionar no final do arquivo
            echo "" >> "app/$pagina/page.js"
            echo "export const dynamic = 'force-dynamic'" >> "app/$pagina/page.js"
            echo "✅ $pagina - export dynamic adicionado"
        else
            echo "✅ $pagina - já é dinâmica"
        fi
    fi
done

echo ""
echo "🚀 DEPLOY RÁPIDO COM PÁGINAS DINÂMICAS..."
npm run build && npx vercel --prod --force

