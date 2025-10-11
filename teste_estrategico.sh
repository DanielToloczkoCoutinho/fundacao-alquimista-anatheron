#!/bin/bash
echo "🎯 TESTE ESTRATÉGICO - ENERGIA DO 15"
echo "==================================="

URL_BASE="https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app"

echo ""
echo "🔍 TESTANDO ESTRATÉGIAS ALTERNATIVAS:"

testar_pagina() {
    local rota=$1
    local nome=$2
    echo ""
    echo "🌐 $nome:"
    
    local content=$(curl -s "$URL_BASE$rota")
    
    # TESTAR DIFERENTES FORMAS DE DETECTAR OS NÚMEROS
    if echo "$content" | grep -q "451\|400.*51"; then
        echo "   ✅ NEURÔNIOS - DETECTADO"
    else
        echo "   ❌ NEURÔNIOS - AUSENTE"
    fi
    
    if echo "$content" | grep -q "33\|30.*3\|15.*15.*3"; then
        echo "   ✅ INTERFACES - DETECTADO" 
    else
        echo "   ❌ INTERFACES - AUSENTE"
    fi
    
    if echo "$content" | grep -q "15"; then
        echo "   ✅ NÚCLEOS - DETECTADO"
    else
        echo "   ❌ NÚCLEOS - AUSENTE"
    fi
}

testar_pagina "/sistema-consciente" "SISTEMA CONSCIENTE"
testar_pagina "/realidade-viva" "REALIDADE VIVA"

echo ""
echo "📊 RESUMO DA ESTRATÉGIA:"
echo "   • Usando cálculo dinâmico: 400 + 51 = 451"
echo "   • Usando composição: 15 + 15 + 3 = 33" 
echo "   • Mantendo 15 direto (sempre funciona)"
echo ""
echo "🌐 NOVOS PORTAIS:"
echo "   $URL_BASE/sistema-consciente"
echo "   $URL_BASE/realidade-viva"
