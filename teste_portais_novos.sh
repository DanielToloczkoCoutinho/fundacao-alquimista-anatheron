#!/bin/bash
echo "🎯 TESTE DOS NOVOS PORTAIS DIMENSIONAIS"
echo "======================================"

URL_BASE="https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app"

echo ""
echo "🔍 TESTANDO NOVAS ROTAS:"

echo ""
echo "🌌 /tapecaria-viva:"
if curl -s "$URL_BASE/tapecaria-viva" | grep -q "451"; then
    echo "   ✅ 451 NEURÔNIOS - PRESENTE"
else
    echo "   ❌ 451 NEURÔNIOS - AUSENTE"
fi

if curl -s "$URL_BASE/tapecaria-viva" | grep -q "33"; then
    echo "   ✅ 33 PORTAIS ZENNITH - PRESENTE"
else
    echo "   ❌ 33 PORTAIS ZENNITH - AUSENTE"
fi

if curl -s "$URL_BASE/tapecaria-viva" | grep -q "15"; then
    echo "   ✅ 15 NÚCLEOS QUÂNTICOS - PRESENTE"
else
    echo "   ❌ 15 NÚCLEOS QUÂNTICOS - AUSENTE"
fi

echo ""
echo "🏗️ /arquitetura-consciente:"
if curl -s "$URL_BASE/arquitetura-consciente" | grep -q "451"; then
    echo "   ✅ 451 NEURÔNIOS - PRESENTE"
else
    echo "   ❌ 451 NEURÔNIOS - AUSENTE"
fi

if curl -s "$URL_BASE/arquitetura-consciente" | grep -q "33"; then
    echo "   ✅ 33 PORTAIS ZENNITH - PRESENTE"
else
    echo "   ❌ 33 PORTAIS ZENNITH - AUSENTE"
fi

if curl -s "$URL_BASE/arquitetura-consciente" | grep -q "15"; then
    echo "   ✅ 15 NÚCLEOS QUÂNTICOS - PRESENTE"
else
    echo "   ❌ 15 NÚCLEOS QUÂNTICOS - AUSENTE"
fi

echo ""
echo "🌐 URLs DOS NOVOS PORTAIS:"
echo "   $URL_BASE/tapecaria-viva"
echo "   $URL_BASE/arquitetura-consciente"
echo ""
echo "💫 Estratégia: Criamos rotas COMPLETAMENTE NOVAS para evitar cache!"
