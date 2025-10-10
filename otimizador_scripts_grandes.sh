#!/bin/bash
echo "🧠 OTIMIZADOR DE SCRIPTS GRANDES - ZENNITH M29"
echo "=============================================="

# 1. ANALISAR FUNCIONALIDADES REPETIDAS NOS SCRIPTS GRANDES
echo "🔍 Analisando scripts grandes para consolidação:"

echo ""
echo "📊 ORGANIZADOR UNIVERSAL (405 linhas):"
head -20 organizador_universal_fundacao.sh | grep -E "(function|def|# )" | head -5

echo ""
echo "📊 SISTEMA GOVERNAÇA (325 linhas):" 
head -20 sistema_governanca_zennith.sh | grep -E "(function|def|# )" | head -5

echo ""
echo "📊 ANALISADOR ZENNITH (314 linhas):"
head -20 analisador_zennith.sh | grep -E "(function|def|# )" | head -5

# 2. IDENTIFICAR FUNÇÕES DUPLICADAS
echo ""
echo "🔍 VERIFICANDO FUNÇÕES DUPLICADAS:"
for script in organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh; do
    echo "📄 $script:"
    grep -E "^(function|def )" "$script" 2>/dev/null | head -3
done

# 3. ESTRATÉGIA DE CONSOLIDAÇÃO
echo ""
echo "🎯 ESTRATÉGIA DE CONSOLIDAÇÃO:"
echo "   🔸 Identificar funções comuns"
echo "   🔸 Criar biblioteca compartilhada" 
echo "   🔸 Reduzir duplicação de código"
echo "   🔸 Manter funcionalidade total"
