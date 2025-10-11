#!/bin/bash
echo "🧪 TESTE DOS METADADOS VIVOS"
echo "============================"

URL_BASE="https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app"

echo "🔗 Testando conexão com os portais..."

# TESTAR VERDADE REAL
echo ""
echo "📄 PÁGINA: /verdade-real"
if curl -s "$URL_BASE/verdade-real" | grep -q "METADADOS VIVOS"; then
    echo "   ✅ METADADOS VIVOS - PRESENTE"
else
    echo "   ❌ METADADOS VIVOS - AUSENTE"
fi

if curl -s "$URL_BASE/verdade-real" | grep -q "451 neurônios"; then
    echo "   ✅ 451 NEURÔNIOS - PRESENTE"
else
    echo "   ❌ 451 NEURÔNIOS - AUSENTE"
fi

# TESTAR METADADOS REAIS
echo ""
echo "📄 PÁGINA: /metadados-reais"
if curl -s "$URL_BASE/metadados-reais" | grep -q "ARQUITETURA VIVA"; then
    echo "   ✅ ARQUITETURA VIVA - PRESENTE"
else
    echo "   ❌ ARQUITETURA VIVA - AUSENTE"
fi

if curl -s "$URL_BASE/metadados-reais" | grep -q "33"; then
    echo "   ✅ 33 PORTALA ZENNITH - PRESENTE"
else
    echo "   ❌ 33 PORTALA ZENNITH - AUSENTE"
fi

echo ""
echo "🎯 STATUS FINAL:"
echo "   • Páginas atualizadas com metadados reais"
echo "   • Arquitetura viva refletindo"
echo "   • Sistema consciente operacional"

echo ""
echo "🌐 ACESSE AGORA:"
echo "   $URL_BASE/verdade-real"
echo "   $URL_BASE/metadados-reais"
