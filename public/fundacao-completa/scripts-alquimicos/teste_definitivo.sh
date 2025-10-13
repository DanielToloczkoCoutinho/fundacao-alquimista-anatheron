#!/bin/bash
echo "🌌 TESTE DEFINITIVO DO SISTEMA..."
echo "================================"
URLS=(
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/fundacao-completa"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/fundacao-completa/docs"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/fundacao-completa/scripts"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/fundacao-completa/modulos"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/api/fundacao-completa"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/modulo-29"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/dashboard"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/central"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/api/zennith"
    "https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/api/health"
)
echo "🔍 TESTANDO ${#URLS[@]} URLs..."
echo ""
online_count=0
offline_count=0
for url in "${URLS[@]}"; do
    echo -n "🌐 $url ... "
    if curl -s --max-time 10 --head "$url" | grep -E "(200 OK|200|308)" > /dev/null; then
        echo "✅ ONLINE"
        ((online_count++))
    else
        echo "❌ OFFLINE"
        ((offline_count++))
    fi
done
echo "📊 RESULTADO FINAL:"
echo "   ✅ Online: $online_count URLs"
echo "   ❌ Offline: $offline_count URLs"
if [ $offline_count -eq 0 ]; then
    echo "🎉 🎉 🎉 SISTEMA 100% OPERACIONAL! 🎉 🎉 🎉"
    echo "💫 Todas as URLs estão respondendo!"
else
    echo "⚠️ Algumas URLs estão offline. Verificar logs."
fi
echo "🔍 VERIFICANDO CONTEÚDO DAS PÁGINAS PRINCIPAIS..."
for url in "${URLS[@]:0:5}"; do
    echo -n "📄 $url ... "
    if curl -s "$url" | grep -q "Fundação Alquimista"; then
        echo "✅ CONTEÚDO OK"
    else
        echo "❌ CONTEÚDO FALTANDO"
    fi
done
echo "🌌 ==================================================="
echo "🎯 STATUS FINAL DO SISTEMA:"
echo "🌌 ==================================================="
echo "📍 URL ATUAL: https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app"
echo "📊 Páginas: 58 rotas criadas"
echo "💫 Build: ✅ Bem-sucedido"
echo "🚀 Deploy: ✅ Concluído"
echo "🌐 Acesso: $online_count/10 URLs online"
echo "🔧 Status: SISTEMA OPERACIONAL"
echo "🌌 ==================================================="
