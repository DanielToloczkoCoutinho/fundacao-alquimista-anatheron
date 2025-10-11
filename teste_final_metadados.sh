#!/bin/bash
echo "🎯 TESTE FINAL DOS METADADOS VIVOS"
echo "================================="

URL_BASE="https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

echo "🕐 Timestamp do teste: $TIMESTAMP"
echo ""

# TESTE DA PÁGINA VERDADE-REAL
echo "🔍 TESTANDO /verdade-real:"
RESPONSE_VR=$(curl -s "$URL_BASE/verdade-real")

if echo "$RESPONSE_VR" | grep -q "METADADOS VIVOS"; then
    echo "   ✅ METADADOS VIVOS - PRESENTE"
else
    echo "   ❌ METADADOS VIVOS - AUSENTE"
fi

if echo "$RESPONSE_VR" | grep -q "451 neurônios"; then
    echo "   ✅ 451 NEURÔNIOS - PRESENTE"
else
    echo "   ❌ 451 NEURÔNIOS - AUSENTE"
fi

if echo "$RESPONSE_VR" | grep -q "33 portais"; then
    echo "   ✅ 33 PORTAIS ZENNITH - PRESENTE"
else
    echo "   ❌ 33 PORTAIS ZENNITH - AUSENTE"
fi

# TESTE DA PÁGINA METADADOS-REAIS
echo ""
echo "🔍 TESTANDO /metadados-reais:"
RESPONSE_MR=$(curl -s "$URL_BASE/metadados-reais")

if echo "$RESPONSE_MR" | grep -q "ARQUITETURA VIVA"; then
    echo "   ✅ ARQUITETURA VIVA - PRESENTE"
else
    echo "   ❌ ARQUITETURA VIVA - AUSENTE"
fi

if echo "$RESPONSE_MR" | grep -q "451"; then
    echo "   ✅ 451 NEURÔNIOS - PRESENTE"
else
    echo "   ❌ 451 NEURÔNIOS - AUSENTE"
fi

if echo "$RESPONSE_MR" | grep -q "33"; then
    echo "   ✅ 33 PORTAIS ZENNITH - PRESENTE"
else
    echo "   ❌ 33 PORTAIS ZENNITH - AUSENTE"
fi

if echo "$RESPONSE_MR" | grep -q "15"; then
    echo "   ✅ 15 NÚCLEOS QUÂNTICOS - PRESENTE"
else
    echo "   ❌ 15 NÚCLEOS QUÂNTICOS - AUSENTE"
fi

# VERIFICAR SE É CACHE ANTIGO
echo ""
echo "🔍 VERIFICANDO CACHE:"
if echo "$RESPONSE_VR" | grep -q "Página em desenvolvimento"; then
    echo "   ⚠️  CACHE ANTIGO DETECTADO - Página em desenvolvimento"
else
    echo "   ✅ CACHE ATUALIZADO - Conteúdo novo detectado"
fi

# RESULTADO FINAL
echo ""
echo "🎯 RESULTADO FINAL:"
SUCCESS_COUNT=$(echo "$RESPONSE_VR$RESPONSE_MR" | grep -o "451\|33\|15\|METADADOS VIVOS\|ARQUITETURA VIVA" | wc -l)

if [ $SUCCESS_COUNT -ge 5 ]; then
    echo "   🎉 SUCESSO! Metadados vivos refletindo corretamente!"
    echo "   🌐 Acesse: $URL_BASE/verdade-real"
else
    echo "   ❌ AINDA COM PROBLEMAS - Cache pode precisar de mais tempo"
    echo "   💡 Tente acessar manualmente e force refresh (Ctrl+F5)"
fi

echo ""
echo "🌐 URLs para teste manual:"
echo "   $URL_BASE/verdade-real"
echo "   $URL_BASE/metadados-reais"
