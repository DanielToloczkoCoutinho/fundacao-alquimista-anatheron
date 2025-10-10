#!/bin/bash
# 🧭 NAVEGADOR DA FUNDAÇÃO - SEMPRE SABER ONDE ESTÁ

echo "🧭 NAVEGADOR DA FUNDAÇÃO ALCHEMISTA"
echo "==================================="
echo "📅 $(date)"
echo ""

# Mostrar localização atual
echo "📍 VOCÊ ESTÁ EM:"
pwd
echo ""

# Mostrar organograma
echo "📁 ORGANOGRAMA PRINCIPAL:"
echo "   🏠 ~/studio/ (RAIZ)"
echo "   🔬 laboratorios_hierarquicos/ (TRABALHO PRINCIPAL)"
echo "   📚 docs/ (DOCUMENTAÇÃO)" 
echo "   ⚙️ SCRIPTS_CENTRALIZADOS/ (SCRIPTS ORGANIZADOS)"
echo "   🏛️ FUNDACAO_ORGANIZADA_DEFINITIVA/ (ESTRUTURA)"
echo ""

# Navegação rápida
case $1 in
    "trabalho")
        cd ~/studio/laboratorios_hierarquicos
        echo "🚀 NAVEGANDO PARA ÁREA DE TRABALHO PRINCIPAL"
        pwd
        ;;
    "docs")
        cd ~/studio/docs  
        echo "📚 NAVEGANDO PARA DOCUMENTAÇÃO"
        pwd
        ;;
    "scripts")
        cd ~/studio/SCRIPTS_CENTRALIZADOS
        echo "⚙️ NAVEGANDO PARA SCRIPTS"
        pwd
        ;;
    "raiz")
        cd ~/studio
        echo "🏠 NAVEGANDO PARA RAIZ"
        pwd
        ;;
    *)
        echo "🎯 COMANDOS DE NAVEGAÇÃO:"
        echo "  ./navegador_fundacao.sh trabalho  → laboratorios_hierarquicos/"
        echo "  ./navegador_fundacao.sh docs      → docs/"
        echo "  ./navegador_fundacao.sh scripts   → SCRIPTS_CENTRALIZADOS/"
        echo "  ./navegador_fundacao.sh raiz      → ~/studio/"
        echo ""
        echo "💡 Use sempre este navegador para não se perder!"
        ;;
esac
