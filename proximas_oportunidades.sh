#!/bin/bash
echo "🔍 PRÓXIMAS OPORTUNIDADES DE CONSOLIDAÇÃO"
echo "========================================="

echo "📊 Após migração de log, identificar próximos candidatos:"

# 1. FUNÇÕES DE ORGANIZAÇÃO/PROCESSAMENTO
echo ""
echo "🧩 Funções de Processamento:"
grep -n "organizar_.*()" organizador_universal_fundacao.sh | head -5
grep -n "processar_.*()" sistema_governanca_zennith.sh analisador_zennith.sh | head -5

# 2. FUNÇÕES DE RELATÓRIO/SAÍDA
echo ""
echo "📋 Funções de Relatório:"
grep -n "gerar_.*()\|criar_.*()" organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh | head -5

# 3. FUNÇÕES DE VALIDAÇÃO (se existirem)
echo ""
echo "✅ Funções de Validação:"
grep -n "validar.*()\|verificar.*()" organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh | head -5

# 4. ESTRATÉGIA DE FASE 3
echo ""
echo "🎯 ESTRATÉGIA FASE 3:"
echo "  1. Consolidar funções de processamento similares"
echo "  2. Criar utils_zennith_processamento.sh" 
echo "  3. Migrar gradualmente"
echo "  4. Meta: Reduzir +100 linhas adicionais"
