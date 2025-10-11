#!/bin/bash
echo "🌐 VERIFICAÇÃO DO DEPLOY NEXUS"
echo "==============================="

echo "🔗 Testando URLs..."
echo ""

# TESTAR URL PRINCIPAL
echo "1. 🌐 URL Principal:"
if curl -s --head https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app | head -n 1 | grep -q "200"; then
    echo "   ✅ ONLINE"
else
    echo "   ❌ OFFLINE"
fi

# TESTAR PÁGINA NEXUS
echo ""
echo "2. 🎯 Página Nexus:"
NEXUS_STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app/nexus)
if [ "$NEXUS_STATUS" = "200" ]; then
    echo "   ✅ ONLINE (HTTP $NEXUS_STATUS)"
    echo "   🔗 https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app/nexus"
elif [ "$NEXUS_STATUS" = "404" ]; then
    echo "   ❌ NÃO ENCONTRADA (HTTP 404)"
    echo "   ⚠️  O deploy pode ainda estar em andamento"
else
    echo "   🔄 STATUS: HTTP $NEXUS_STATUS"
fi

# TESTAR OUTRAS PÁGINAS
echo ""
echo "3. 📊 Outras páginas:"
for page in dashboard metadados-reais docs/manifesto_quantico; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app/$page")
    if [ "$STATUS" = "200" ]; then
        echo "   ✅ /$page: ONLINE"
    else
        echo "   🔄 /$page: HTTP $STATUS"
    fi
done

echo ""
echo "🎯 RECOMENDAÇÃO:"
if [ "$NEXUS_STATUS" = "200" ]; then
    echo "   🚀 ACESSE AGORA: https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app/nexus"
else
    echo "   ⏳ Aguarde 2-3 minutos e teste novamente"
    echo "   🔄 O deploy automático do Vercel está em progresso"
fi
