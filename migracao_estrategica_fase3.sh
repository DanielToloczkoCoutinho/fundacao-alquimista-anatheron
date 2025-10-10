#!/bin/bash
echo "🎯 MIGRAÇÃO ESTRATÉGICA - FASE 3"
echo "================================"

# 1. BACKUP COMPLETO
echo "📦 Criando backup estratégico..."
cp organizador_universal_fundacao.sh organizador_universal_fundacao.sh.pre_fase3

# 2. ANALISAR A FUNÇÃO organize_por_tecnologias EM DETALHE
echo "🔍 Analisando função organize_por_tecnologias para divisão..."

# Extrair a função completa
sed -n '204,408p' organizador_universal_fundacao.sh > funcao_organizar_temp.sh

# Analisar estrutura
echo "📊 Estrutura da função:"
echo "  Linhas totais: $(wc -l < funcao_organizar_temp.sh)"
echo "  Blocos if: $(grep -c "if" funcao_organizar_temp.sh)"
echo "  Loops for: $(grep -c "for" funcao_organizar_temp.sh)"
echo "  Casos case: $(grep -c "case" funcao_organizar_temp.sh)"

# 3. IDENTIFICAR PONTOS DE DIVISÃO
echo ""
echo "🧩 Identificando pontos de divisão natural:"

# Encontrar seções lógicas
grep -n "##.*##" funcao_organizar_temp.sh | head -10
grep -n "# .*" funcao_organizar_temp.sh | head -10

# 4. ESTRATÉGIA DE DIVISÃO
echo ""
echo "🎯 ESTRATÉGIA DE DIVISÃO:"
echo "  1. Identificar 3-5 blocos lógicos principais"
echo "  2. Extrair cada bloco como função separada"
echo "  3. Manter função principal como orquestradora"
echo "  4. Reduzir função original em 60-70%"

# 5. MIGRAÇÃO GRADUAL
echo ""
echo "🔄 Preparando migração gradual..."
cat > plano_divisao_funcao.txt << 'DIVISAOEOF'
# PLANO DE DIVISÃO - organize_por_tecnologias
# ===========================================

BLOCO 1: Detecção de tecnologias (linhas 210-250)
  → Função: detectar_tecnologias_arquivo()

BLOCO 2: Categorização por tipo (linhas 251-300)  
  → Função: categorizar_por_tipo()

BLOCO 3: Organização física (linhas 301-350)
  → Função: executar_organizacao_fisica()

BLOCO 4: Geração de relatório (linhas 351-408)
  → Função: gerar_relatorio_organizacao()

FUNÇÃO PRINCIPAL: organize_por_tecnologias() (orquestração)
  → Reduzida para ~50 linhas
DIVISAOEOF

echo "✅ Plano de divisão criado"

# 6. EXECUTAR MIGRAÇÃO CONTROLADA
echo ""
echo "🛡️ Executando migração controlada..."

# Primeiro: Adicionar imports
sed -i '1a\source utils_zennith_processamento.sh' organizador_universal_fundacao.sh

echo ""
echo "📈 ESTIMATIVA FASE 3:"
echo "  🔸 Função atual: 204 linhas"
echo "  🔸 Após divisão: ~50 linhas (principal) + 150 linhas (sub-funções)"
echo "  🔸 Redução líquida: ~100 linhas"
echo "  🔸 Ganho total com Fase 2+3: ~118 linhas"

echo ""
echo "🎯 PRÓXIMO: Executar divisão da função (manual para segurança)"
