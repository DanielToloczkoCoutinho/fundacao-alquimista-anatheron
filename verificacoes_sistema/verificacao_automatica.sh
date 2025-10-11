#!/bin/bash
# 🎯 VERIFICAÇÃO AUTOMÁTICA - CICLO ALFA
echo "🔄 VERIFICAÇÃO AUTOMÁTICA - $(date)"
echo "=================================="

cd /home/user/studio

# EXECUTAR VERIFICAÇÃO DE COERÊNCIA
./verificacoes_sistema/verificar_coerencia.sh > verificacoes_sistema/logs/verificacao_$(date +%Y%m%d_%H%M%S).log 2>&1

# ATUALIZAR METADADOS
./verificacoes_sistema/painel_metadados.sh > /dev/null 2>&1

echo "✅ Verificação automática concluída: $(date)"
