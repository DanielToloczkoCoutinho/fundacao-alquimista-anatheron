#!/bin/bash
echo "🎯 ZENNITH M29 - ANÁLISE AVANÇADA"
echo "================================"
echo "🔬 Módulo Ω ativado - Análise completa"

# ANÁLISE ESTRUTURAL COMPLETA
echo "📊 MAPEAMENTO ESTRUTURAL:"

# 1. Análise de scripts por complexidade
echo ""
echo "🧠 COMPLEXIDADE DE SCRIPTS:"
find . -name "*.sh" -o -name "*.py" | head -10 | while read script; do
    lines=$(wc -l < "$script")
    size=$(du -h "$script" | cut -f1)
    echo "  📄 $script: $lines linhas, $size"
done

# 2. Análise de dependências
echo ""
echo "🔗 DEPENDÊNCIAS IDENTIFICADAS:"
find . -name "*.json" -exec grep -l "dependencies\|devDependencies" {} \; | head -5

# 3. Análise de documentação
echo ""
echo "📚 DOCUMENTAÇÃO:"
find . -name "*.md" -o -name "*.txt" | wc -l | xargs echo "  Total de documentos:"

# 4. RELATÓRIO FINAL
echo ""
echo "📈 RELATÓRIO ZENNITH M29:"
echo "  🔹 Scripts ativos: $(find . -name "*.sh" -o -name "*.py" | wc -l)"
echo "  🔹 Documentação: $(find . -name "*.md" -o -name "*.txt" | wc -l)" 
echo "  🔹 Configurações: $(find . -name "*.json" -o -name "*.yaml" -o -name "*.yml" | wc -l)"
echo "  🔹 Espaço total: $(du -sh . | cut -f1)"
echo ""
echo "🎯 PRÓXIMOS PASSOS:"
echo "  1. Executar compactador inteligente"
echo "  2. Fazer commit otimizado no Git"
echo "  3. Manter apenas essenciais ativos"
