#!/bin/bash
echo "🧠 CONSOLIDADOR PRÁTICO DE SCRIPTS GRANDES"
echo "==========================================="

# 1. ANALISAR FUNCIONALIDADES COMUNS NOS 3 SCRIPTS PRINCIPAIS
echo "🔍 Analisando funcionalidades comuns:"

echo ""
echo "📊 ORGANIZADOR UNIVERSAL (405 linhas):"
echo "   Funções principais:"
grep -E "^(function|def |# FUNÇÃO|# SEÇÃO)" organizador_universal_fundacao.sh | head -8

echo ""
echo "📊 SISTEMA GOVERNAÇA (325 linhas):"
echo "   Funções principais:"
grep -E "^(function|def |# FUNÇÃO|# SEÇÃO)" sistema_governanca_zennith.sh | head -8

echo ""
echo "📊 ANALISADOR ZENNITH (314 linhas):"
echo "   Funções principais:"  
grep -E "^(function|def |# FUNÇÃO|# SEÇÃO)" analisador_zennith.sh | head -8

# 2. IDENTIFICAR FUNÇÕES DUPLICADAS
echo ""
echo "🔄 FUNÇÕES POTENCIALMENTE DUPLICADAS:"
for func in "log_" "analisar_" "processar_" "validar_"; do
    echo "🔍 Funções com '$func':"
    grep -h "function $func\|def $func" organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh 2>/dev/null | head -3
done

# 3. ESTRATÉGIA DE CONSOLIDAÇÃO
echo ""
echo "🎯 PLANO DE CONSOLIDAÇÃO:"
echo "   FASE 1: Identificar 5-10 funções mais duplicadas"
echo "   FASE 2: Criar biblioteca compartilhada (utils_zennith.sh)"
echo "   FASE 3: Refatorar scripts para usar biblioteca"
echo "   FASE 4: Reduzir código duplicado em ~30%"
