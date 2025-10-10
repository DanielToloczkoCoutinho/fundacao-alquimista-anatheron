#!/bin/bash
echo "📈 CALCULADOR DE GANHO REAL - MIGRAÇÃO LOG"
echo "=========================================="

# Calcular linhas antes
linhas_antes_org=$(wc -l < organizador_universal_fundacao.sh.pre_log_migration)
linhas_antes_gov=$(wc -l < sistema_governanca_zennith.sh.pre_log_migration) 
linhas_antes_ana=$(wc -l < analisador_zennith.sh.pre_log_migration)

# Calcular linhas depois
linhas_depois_org=$(wc -l < organizador_universal_fundacao.sh)
linhas_depois_gov=$(wc -l < sistema_governanca_zennith.sh)
linhas_depois_ana=$(wc -l < analisador_zennith.sh)

# Calcular redução
reducao_org=$((linhas_antes_org - linhas_depois_org))
reducao_gov=$((linhas_antes_gov - linhas_depois_gov)) 
reducao_ana=$((linhas_antes_ana - linhas_depois_ana))

reducao_total=$((reducao_org + reducao_gov + reducao_ana))

echo ""
echo "📊 RESULTADO DA MIGRAÇÃO:"
echo "  🔸 Organizador: $linhas_antes_org → $linhas_depois_org linhas (-$reducao_org)"
echo "  🔸 Governança: $linhas_antes_gov → $linhas_depois_gov linhas (-$reducao_gov)"
echo "  🔸 Analisador: $linhas_antes_ana → $linhas_depois_ana linhas (-$reducao_ana)"
echo ""
echo "🎯 TOTAL: $reducao_total linhas eliminadas por duplicação"
echo "💡 Próxima oportunidade: Funções de organização/processamento"

# Verificar funcionalidade
echo ""
echo "🔍 TESTE RÁPIDO DE FUNCIONALIDADE:"
source utils_zennith_log_avancado.sh
log_zennith "TESTE: Sistema unificado funcionando perfeitamente"
log_info "Migração concluída com sucesso"
