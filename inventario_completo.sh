#!/bin/bash
echo "📊 INVENTÁRIO DA FUNDAÇÃO ALQUIMISTA UNIFICADA"
echo "=============================================="

# LOCALIZAÇÃO ATUAL
echo "📍 LOCALIZAÇÃO: /home/user/studio/fundacao-alquimista"
echo "📏 TAMANHO TOTAL: $(du -sh . | cut -f1)"

# CONTAGEM DETALHADA
echo ""
echo "📈 ESTATÍSTICAS DETALHADAS:"
echo "📄 Documentos/Markdown: $(find . -name "*.md" -o -name "*.txt" -o -name "*.json" | wc -l)"
echo "⚡ Scripts Python: $(find . -name "*.py" | wc -l)"
echo "🔧 Scripts Shell: $(find . -name "*.sh" | wc -l)"
echo "🌐 Arquivos Next.js: $(find . -name "*.js" -o -name "*.jsx" -o -name "*.ts" -o -name "*.tsx" | wc -l)"
echo "📁 Diretórios: $(find . -type d | wc -l)"
echo "📦 Arquivos totais: $(find . -type f | wc -l)"

# ESTRUTURA PRINCIPAL
echo ""
echo "🏗️ ESTRUTURA PRINCIPAL:"
for dir in app public scripts modulos docs components lib; do
    if [ -d "$dir" ]; then
        echo "   📁 $dir: $(find "$dir" -type f | wc -l) arquivos"
    fi
done

# CONFIGURAÇÕES CRÍTICAS
echo ""
echo "⚙️ CONFIGURAÇÕES CRÍTICAS:"
for config in package.json next.config.js tailwind.config.js postcss.config.js; do
    if [ -f "$config" ]; then
        echo "   ✅ $config: PRESENTE"
    else
        echo "   ❌ $config: AUSENTE"
    fi
done

# SCRIPTS EXECUTÁVEIS
echo ""
echo "🚀 SCRIPTS EXECUTÁVEIS:"
find . -name "*.sh" -executable | head -10 | while read script; do
    echo "   🔧 $(basename "$script")"
done
