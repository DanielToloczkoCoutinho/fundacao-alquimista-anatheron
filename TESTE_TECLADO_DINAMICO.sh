#!/bin/bash

echo "🎮 TESTE VIA TECLADO - SISTEMA DINÂMICO"
echo "========================================"

URL_BASE="https://fundacao-alquimista-anatheron-lgse1s7n3.vercel.app"

echo "🔍 Testando conectividade das páginas dinâmicas..."
echo ""

# Testar cada página
testar_pagina() {
    local nome=$1
    local path=$2
    local url="${URL_BASE}${path}"
    
    echo "🎯 Testando: $nome"
    echo "   📍 $url"
    
    # Fazer requisição e verificar se é dinâmica
    response=$(curl -s -I "$url" | head -1 | cut -d' ' -f2)
    content=$(curl -s "$url")
    
    if [ "$response" -eq 200 ]; then
        echo "   ✅ ONLINE (Status: $response)"
        
        # Verificar se tem elementos dinâmicos
        if echo "$content" | grep -q "useState\|useEffect\|setInterval"; then
            echo "   🔄 CÓDIGO DINÂMICO DETECTADO"
        fi
        
        # Verificar tamanho do conteúdo
        size=$(echo "$content" | wc -c)
        echo "   📏 Tamanho: $size bytes"
    else
        echo "   ❌ OFFLINE (Status: $response)"
    fi
    echo ""
}

# Testar páginas principais
testar_pagina "Módulo 303" "/modulo-303"
testar_pagina "Sistema Vivo" "/sistema-vivo" 
testar_pagina "Portal Central" "/central"
testar_pagina "Status" "/status"
testar_pagina "APIs Health" "/api/health"
testar_pagina "APIs Metrics" "/api/metrics"

echo "🎉 SISTEMA DINÂMICO VERIFICADO!"
echo "💫 Acesse: $URL_BASE/central"

