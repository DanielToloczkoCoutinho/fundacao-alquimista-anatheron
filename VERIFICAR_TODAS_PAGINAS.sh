#!/bin/bash

echo "🔍 VERIFICAÇÃO COMPLETA DAS PÁGINAS"
echo "==================================="

URL_BASE="https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app"

echo "🌐 URL Base: $URL_BASE"
echo ""

# Lista de páginas para verificar
paginas=(
    "/sistema-vivo"
    "/status" 
    "/arvore-da-vida"
    "/revelacao-real"
    "/metadados-reais"
    "/verificador-conexoes"
    "/analise-metadados"
    "/analise-fundacao"
    "/arquitetura-zennith"
    "/dashboard-definitivo"
    "/dashboard-final"
    "/interfaces-conectadas"
    "/verdade-real"
)

echo "📋 PÁGINAS PARA VERIFICAR:"
echo "-------------------------"

for pagina in "${paginas[@]}"; do
    echo -n "🔍 $pagina: "
    if curl -s -I "$URL_BASE$pagina" | head -n 1 | grep -q "200"; then
        echo "✅ ONLINE"
        # Verificar se tem conteúdo dinâmico
        if curl -s "$URL_BASE$pagina" | grep -q "useState\|useEffect\|setInterval"; then
            echo "   🎯 Código dinâmico detectado"
        fi
    else
        echo "❌ OFFLINE ou ERRO"
    fi
done

echo ""
echo "🎯 PRÓXIMOS PASSOS IDENTIFICADOS:"
echo "   1. Atualizar páginas que estão offline"
echo "   2. Implementar Fase 2 - APIs reais"
echo "   3. Desenvolver Fase 3 - Sistema Lux.Net"
echo "   4. Otimizar performance e UX"

