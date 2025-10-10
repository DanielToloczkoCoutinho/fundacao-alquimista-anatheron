#!/bin/bash
echo "🔍 VERIFICADOR DE COMPATIBILIDADE"
echo "================================"

# 1. VERIFICAR SE AS FUNÇÕES EXISTEM NOS SCRIPTS
echo "📋 Funções sendo usadas atualmente:"

for script in organizador_universal_fundacao.sh sistema_governanca_zennith.sh analisador_zennith.sh; do
    echo ""
    echo "📄 $script:"
    echo "  📝 Log functions: $(grep -c "log.*(" "$script")"
    echo "  ✅ Validation functions: $(grep -c "validar.*(\|check.*(" "$script")"  
    echo "  📊 Monitor functions: $(grep -c "monitorar.*(" "$script")"
    echo "  💾 Backup functions: $(grep -c "backup.*(" "$script")"
done

# 2. CRIAR SCRIPT DE MIGRAÇÃO SEGURO
echo ""
echo "🛡️ Criando migrador seguro..."

cat > migrador_seguro.sh << 'MIGRAEOF'
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
MIGRAEOF

chmod +x migrador_seguro.sh

# 3. RELATÓRIO FINAL
echo ""
echo "📈 RELATÓRIO DE PRONTIDÃO:"
echo "  ✅ Biblioteca core criada: utils_zennith_core.sh"
echo "  ✅ Mapa de substituição criado"
echo "  ✅ Migrador seguro preparado"
echo "  🔄 Próximo: Executar migração controlada"
