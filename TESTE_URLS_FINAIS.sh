#!/bin/bash

echo "🧪 TESTE DAS URLs FINAIS FUNCIONAIS"
echo "==================================="

URL_MINIMA="https://fundacao-alquimista-anatheron-fbbb3hrqm.vercel.app"
URL_CORRIGIDA="https://fundacao-alquimista-anatheron-flcviz6ke.vercel.app"

testar_url() {
    local url=$1
    local nome=$2
    
    echo "🔍 Testando: $nome"
    echo "   🌐 $url"
    
    if curl -s --max-time 10 "$url" > /dev/null; then
        echo "   ✅ ONLINE"
        
        # Testar páginas específicas
        for pagina in "/central" "/modulo-303" "/sistema-vivo" "/status"; do
            if curl -s --max-time 5 "$url$pagina" > /dev/null; then
                echo "      ✅ $pagina - OK"
            else
                echo "      ❌ $pagina - FALHOU"
            fi
        done
    else
        echo "   ❌ OFFLINE"
    fi
    echo ""
}

echo "📊 COMPARAÇÃO DAS URLs:"
echo "======================="
testar_url "$URL_MINIMA" "SISTEMA MÍNIMO"
testar_url "$URL_CORRIGIDA" "SISTEMA CORRIGIDO COMPLETO"

echo "🎯 RECOMENDAÇÃO FINAL:"
echo "======================"
echo "💫 Use a URL CORRIGIDA COMPLETA para ter todas as funcionalidades:"
echo "   🔗 $URL_CORRIGIDA/central"
echo ""
echo "📱 ACESSE AGORA E TESTE:"
echo "   - Portal Central: $URL_CORRIGIDA/central"
echo "   - Módulo 303: $URL_CORRIGIDA/modulo-303"
echo "   - Sistema Vivo: $URL_CORRIGIDA/sistema-vivo"
echo "   - Status: $URL_CORRIGIDA/status"

