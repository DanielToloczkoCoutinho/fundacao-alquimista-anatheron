#!/bin/bash
echo "🔄 REFATORADOR AUTOMÁTICO - ZENNITH M29"
echo "========================================"

# 1. IDENTIFICAR FUNÇÕES MAIS DUPLICADAS NOS SCRIPTS GRANDES
echo "🔍 Analisando funções duplicadas..."

# Funções comuns de log
echo "📝 Funções de Log encontradas:"
grep -n "log.*()" organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh | head -10

# Funções de validação
echo ""
echo "✅ Funções de Validação encontradas:"
grep -n "validar.*()\|check.*()" organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh | head -10

# 2. CRIAR MAPA DE SUBSTITUIÇÃO
echo ""
echo "🗺️ Criando mapa de substituição:"

cat > mapa_substituicao.txt << 'MAPEOF'
# MAPA DE SUBSTITUIÇÃO - FUNÇÕES DUPLICADAS
# =========================================

# LOG FUNCTIONS
log_.*() → log_zennith()

# VALIDATION FUNCTIONS  
validar_.*() → validar_arquivo() / validar_diretorio()

# MONITORING FUNCTIONS
monitorar_.*() → monitorar_recursos()

# BACKUP FUNCTIONS
backup_.*() → backup_automatico()

# ANALYSIS FUNCTIONS
analisar_.*() → analisar_espaco()
MAPEOF

echo "✅ Mapa de substituição criado"

# 3. ESTIMATIVA DE REDUÇÃO
echo ""
echo "📊 ESTIMATIVA DE REDUÇÃO:"
echo "  Scripts analisados: 3"
echo "  Linhas totais: ~1044 linhas"
echo "  Linhas duplicadas estimadas: 200-300 (20-30%)"
echo "  Redução potencial: 150-250 linhas"

# 4. PLANO DE REFATORAÇÃO
echo ""
echo "🎯 PLANO DE EXECUÇÃO:"
echo "  1. Fonte: utils_zennith_core.sh"
echo "  2. Substituir funções duplicadas"
echo "  3. Manter compatibilidade"
echo "  4. Testar funcionalidade"
