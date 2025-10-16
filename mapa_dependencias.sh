#!/bin/bash
echo "🗺️ MAPA DE DEPENDÊNCIAS E MÓDULOS"
echo "================================"

# ANÁLISE DE MÓDULOS PYTHON
echo "🐍 MÓDULOS PYTHON:"
find . -name "*.py" -exec grep -h "^import\|^from" {} \; | sort | uniq | head -15

# ANÁLISE DE IMPORTAÇÕES JAVASCRIPT
echo ""
echo "📜 IMPORTAÇÕES JAVASCRIPT/REACT:"
find . -name "*.js" -o -name "*.jsx" -o -name "*.ts" -o -name "*.tsx" | head -5 | while read file; do
    echo "   📄 $(basename "$file"):"
    grep -h "import.*from" "$file" 2>/dev/null | head -3 | sed 's/^/      ➤ /'
done

# DEPENDÊNCIAS DO PACKAGE.JSON
echo ""
echo "📦 DEPENDÊNCIAS NPM:"
if [ -f "package.json" ]; then
    grep -A 20 '"dependencies"' package.json | grep -v '"dependencies"' | head -10
fi
