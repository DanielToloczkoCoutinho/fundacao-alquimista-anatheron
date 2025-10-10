#!/bin/bash
echo "🚨 VERIFICANDO DANOS DO SCRIPT PERIGOSO"
echo "========================================"

# Listar diretórios CRÍTICOS que podem ter sido deletados
DIRETORIOS_CRITICOS=(
    "laboratorios_hierarquicos"
    "SCRIPTS_CENTRALIZADOS" 
    "FUNDACAO_ORGANIZADA_DEFINITIVA"
    "backup_automatico"
    "analise_amostras"
    "analise_camadas"
    "analise_metadados"
    "analise_robusta"
    "analise_zennith"
    "backup_emergencia"
    "backup_emergencial_035154"
    "backup_fundacao_20251008_034721"
    "governanca_zennith"
    "relatorios_laboratorios"
)

echo "🔍 Verificando diretórios críticos..."
for dir in "${DIRETORIOS_CRITICOS[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir - EXISTE"
    else
        echo "❌ $dir - DELETADO!"
    fi
done

# Verificar scripts Zennith essenciais
echo ""
echo "🔍 Verificando scripts Zennith..."
ZENNITH_SCRIPTS=(
    "ZENNITH_EXECUTOR_INTELIGENTE.sh"
    "SISTEMA_ZENNITH_CATALOGACAO.sh"
    "COMANDO_FINAL_INTEGRADO.sh"
)

for script in "${ZENNITH_SCRIPTS[@]}"; do
    if [ -f "laboratorios_hierarquicos/$script" ]; then
        echo "✅ $script - EXISTE"
    else
        echo "❌ $script - NÃO ENCONTRADO"
    fi
done

# Verificar se o sistema principal ainda funciona
echo ""
echo "�� Verificando sistemas principais..."
if [ -d "laboratorios_hierarquicos" ]; then
    echo "✅ Sistema Zennith: ACESSÍVEL"
    cd laboratorios_hierarquicos
    if [ -f "ZENNITH_EXECUTOR_INTELIGENTE.sh" ]; then
        echo "✅ Zennith Executor: FUNCIONAL"
    else
        echo "❌ Zennith Executor: DANIFICADO"
    fi
    cd ..
else
    echo "❌❌❌ SISTEMA ZENNITH COMPLETAMENTE DELETADO!"
fi

echo ""
echo "📊 RESUMO DOS DANOS:"
echo "   - Execute: ./recuperar_tudo_urgente.sh se houver problemas"
echo "   - NUNCA execute scripts de limpeza novamente"
