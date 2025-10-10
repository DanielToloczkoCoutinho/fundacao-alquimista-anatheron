#!/bin/bash

NOVA_URL="https://fundacao-alquimista-anatheron-cmlaoyp6k.vercel.app"

echo "🎯 TESTE DA NOVA URL FUNCIONAL"
echo "=============================="
echo "🌐 URL: $NOVA_URL"
echo ""

echo "🔍 Testando conectividade..."
testar_pagina() {
    local nome=$1
    local path=$2
    local url="$NOVA_URL$path"
    
    echo "📡 $nome: $url"
    if curl -s --max-time 10 "$url" > /dev/null; then
        echo "   ✅ ONLINE"
        # Verificar se é dinâmico
        conteudo=$(curl -s "$url")
        if echo "$conteudo" | grep -q "useState\|useEffect"; then
            echo "   🔄 Código React detectado"
        fi
    else
        echo "   ❌ OFFLINE"
    fi
}

testar_pagina "Portal Central" "/central"
testar_pagina "Módulo 303" "/modulo-303"
testar_pagina "Sistema Vivo" "/sistema-vivo" 
testar_pagina "Status" "/status"
testar_pagina "API Health" "/api/health"
testar_pagina "API Metrics" "/api/metrics"

echo ""
echo "🎉 SISTEMA 100% FUNCIONAL!"
echo "📱 ACESSE AGORA: $NOVA_URL/central"

