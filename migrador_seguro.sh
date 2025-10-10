#!/bin/bash
echo "🛡️ MIGRADOR SEGURO - ZENNITH M29"
echo "================================"

# CARREGAR BIBLIOTECA
source utils_zennith_core.sh

# BACKUP DOS SCRIPTS ORIGINAIS
echo "📦 Criando backup dos scripts originais..."
cp organizador_universal_fundacao.sh organizador_universal_fundacao.sh.backup
cp sistema_governanca_zennith.sh sistema_governanca_zennith.sh.backup  
cp analisador_zennith.sh analisador_zennith.sh.backup

echo "✅ Backups criados"
echo ""
echo "🎯 PRONTO PARA MIGRAÇÃO!"
echo "   Execute manualmente para garantir segurança"
echo "   ou use: ./migrador_automatico.sh (mais agressivo)"
