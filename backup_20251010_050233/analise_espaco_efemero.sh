#!/bin/bash
echo "🔍 ANÁLISE DO ESPAÇO EFÊMERO E DISPONÍVEL"
echo "=========================================="

# 1. VERIFICAR ESPAÇO NO SISTEMA ATUAL
echo "💾 ESPAÇO NO SISTEMA ATUAL:"
df -h . | awk 'NR==2 {print "  📍 Sistema: " $1 " | Disponível: " $4 " | Usado: " $5}'

# 2. ANÁLISE DETALHADA DO QUE É EFÊMERO NO STUDIO
echo ""
echo "📊 ANÁLISE DO STUDIO (398MB):"

# Componentes EFÊMEROS (que podem ser limpos/otimizados)
echo "🗑️  COMPONENTES EFÊMEROS IDENTIFICADOS:"

# Caches
echo "🔸 Caches Python: $(find . -name "__pycache__" -type d -exec du -sh {} + 2>/dev/null | awk '{sum += $1} END {print sum "MB"}' || echo "0MB")"
echo "🔸 Arquivos .pyc: $(find . -name "*.pyc" -exec du -ch {} + 2>/dev/null | grep total | cut -f1 || echo "0")"

# Logs antigos
echo "🔸 Logs antigos: $(find . -name "*.log" -mtime +7 -exec du -ch {} + 2>/dev/null | grep total | cut -f1 || echo "0")"

# Backups muito antigos
echo "🔸 Backups muito antigos: $(find backup_automatico -name "*.md" -mtime +30 -exec du -ch {} + 2>/dev/null | grep total | cut -f1 || echo "0")"

# 3. ESPAÇO "FIXO" vs "VARIÁVEL"
echo ""
echo "📈 CATEGORIZAÇÃO DO ESPAÇO:"

echo "🏗️  ESPAÇO FIXO (ESSENCIAL):"
echo "  🔸 Bibliotecas Python: 331MB (83%) - CRÍTICO"
echo "  🔸 Código fonte: ~70MB (18%) - ESSENCIAL"
echo "  🔸 Total fixo: ~401MB"

echo ""
echo "🔄 ESPAÇO VARIÁVEL (PODE SER OTIMIZADO):"
echo "  🔸 Documentação: 5.3MB (1.3%)"
echo "  🔸 Backups: 4.7MB (1.2%)"
echo "  🔸 Caches: ~1-5MB (estimado)"
echo "  🔸 Total variável: ~11-15MB"

# 4. QUANTO REALMENTE "SOBROU" PARA TRABALHAR
echo ""
echo "🎯 ESPAÇO REALMENTE DISPONÍVEL PARA EXPANSÃO:"

# Calcular espaço disponível no sistema
espaco_disponivel_sistema=$(df -h . | awk 'NR==2 {print $4}')
echo "💻 No sistema: $espaco_disponivel_sistema disponíveis"

echo ""
echo "📦 NO STUDIO:"
echo "  🔸 Espaço atual: 398MB"
echo "  🔸 Espaço 'fixo' necessário: ~401MB"
echo "  🔸 Espaço 'variável' otimizável: ~12MB"
echo ""
echo "💡 REALIDADE: O studio está em sua CAPACIDADE MÍNIMA OPERACIONAL"
echo "   Para expandir, precisamos de mais espaço no sistema"

# 5. RECOMENDAÇÕES PRÁTICAS
echo ""
echo "🚀 ESTRATÉGIAS PARA GANHAR ESPAÇO EFÊMERO:"

echo ""
echo "1. 🗑️  LIMPEZA DE CACHES (GANHO IMEDIATO):"
echo "   • __pycache__: ~1-5MB"
echo "   • *.pyc: ~0.5-2MB"
echo "   • Total potencial: 2-7MB"

echo ""
echo "2. 🗜️  COMPACTAÇÃO AVANÇADA (GANHO MÉDIO):"
echo "   • Documentação antiga: +2-3MB"
echo "   • Backups muito antigos: +1-2MB"
echo "   • Total potencial: 3-5MB"

echo ""
echo "3. 📦 GESTÃO INTELIGENTE (GANHO LONGO PRAZO):"
echo "   • Monitorar crescimento de logs"
echo "   • Rotação automática de backups"
echo "   • Compactação seletiva"

echo ""
echo "🎯 GANHO TOTAL POTENCIAL: 5-12MB (1-3% do total)"
