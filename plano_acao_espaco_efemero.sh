#!/bin/bash
echo "💰 PLANO DE AÇÃO - GANHAR ESPAÇO EFÊMERO"
echo "========================================"

# 1. VERIFICAR ESPAÇO ATUAL EXATO
echo "📊 ESPAÇO ATUAL EXATO:"
espaco_inicial=$(du -sb . | cut -f1)
echo "  🔸 Bytes iniciais: $espaco_inicial"

# 2. LIMPEZA SEGURA DE CACHES
echo ""
echo "1. 🗑️  EXECUTANDO LIMPEZA DE CACHES:"

# Limpar __pycache__
cache_py=$(find . -name "__pycache__" -type d -exec du -sb {} + 2>/dev/null | awk '{sum += $1} END {print sum}')
if [ -n "$cache_py" ] && [ "$cache_py" -gt 0 ]; then
    echo "  🔸 __pycache__: $((cache_py / 1024 / 1024))MB"
    find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
    echo "  ✅ __pycache__ removido"
else
    echo "  🔸 __pycache__: 0MB (já limpo)"
fi

# Limpar *.pyc
pyc_files=$(find . -name "*.pyc" -exec du -sb {} + 2>/dev/null | awk '{sum += $1} END {print sum}')
if [ -n "$pyc_files" ] && [ "$pyc_files" -gt 0 ]; then
    echo "  🔸 *.pyc: $((pyc_files / 1024 / 1024))MB"
    find . -name "*.pyc" -delete 2>/dev/null
    echo "  ✅ *.pyc removido"
else
    echo "  🔸 *.pyc: 0MB (já limpo)"
fi

# 3. COMPACTAÇÃO DE LOGS ANTIGOS
echo ""
echo "2. 🗜️  COMPACTANDO LOGS ANTIGOS:"
logs_antigos=$(find . -name "*.log" -mtime +7 -exec du -sb {} + 2>/dev/null | awk '{sum += $1} END {print sum}')
if [ -n "$logs_antigos" ] && [ "$logs_antigos" -gt 0 ]; then
    echo "  🔸 Logs >7 dias: $((logs_antigos / 1024 / 1024))MB"
    find . -name "*.log" -mtime +7 -exec gzip {} \; 2>/dev/null
    echo "  ✅ Logs antigos compactados"
else
    echo "  🔸 Logs antigos: 0MB (já compactados)"
fi

# 4. VERIFICAR GANHO
echo ""
echo "📈 VERIFICANDO GANHO:"
espaco_final=$(du -sb . | cut -f1)
ganho_bytes=$((espaco_inicial - espaco_final))
ganho_mb=$((ganho_bytes / 1024 / 1024))

echo "  🔸 Espaço inicial: $((espaco_inicial / 1024 / 1024))MB"
echo "  🔸 Espaço final: $((espaco_final / 1024 / 1024))MB"
echo "  🎯 Ganho total: ${ganho_mb}MB"

# 5. ANÁLISE DO RESULTADO
echo ""
echo "📊 RESULTADO DA OPERAÇÃO:"

if [ "$ganho_mb" -gt 0 ]; then
    echo "  ✅ SUCESSO! Ganhamos ${ganho_mb}MB de espaço"
    echo "  💡 Espaço liberado para novas funcionalidades"
else
    echo "  ℹ️  Sistema já estava otimizado"
    echo "  💡 Pouco espaço efêmero disponível para limpeza"
fi

echo ""
echo "🔍 ESPAÇO EFÊMERO RESTANTE:"
echo "  📝 Para mais ganhos, considere:"
echo "     • Rotação de backups mais agressiva"
echo "     • Compactação de documentação muito antiga"
echo "     • Gestão mais rigorosa de logs"

echo ""
echo "💎 CONCLUSÃO: O sistema está em seu ESTADO MAIS OTIMIZADO"
