#!/bin/bash

echo "🚀 VERIFICAÇÃO IMEDIATA DO DEPLOY"
echo "================================"
echo "🌌 Verificando se todas as páginas estão online..."
echo ""

URL_BASE="https://fundacao-alquimista-anatheron-dqiej3rdu.vercel.app"

# Lista de páginas para verificar
paginas=(
    "/"
    "/central" 
    "/modulo-303"
    "/revelacao-real"
    "/metadados-reais"
    "/arvore-da-vida"
    "/sistema-vivo"
    "/dashboard-final"
    "/dashboard-definitivo"
    "/arquitetura-zennith"
    "/interfaces-conectadas"
    "/verdade-real"
    "/analise-fundacao"
    "/analise-metadados"
    "/verificador-conexoes"
)

echo "📊 VERIFICANDO ${#paginas[@]} PÁGINAS..."
echo ""

for pagina in "${paginas[@]}"; do
    url="${URL_BASE}${pagina}"
    echo -n "🔍 ${pagina} ... "
    
    # Verificação simples com curl
    if curl -s --head --fail "$url" > /dev/null 2>&1; then
        echo "✅ ONLINE"
    else
        echo "❌ OFFLINE"
    fi
done

echo ""
echo "🎯 ACESSO DIRETO AO PORTAL CENTRAL:"
echo "🌐 $URL_BASE/central"
echo ""
echo "💫 TODAS AS PÁGINAS DEVEM ESTAR ACESSÍVEIS!"
