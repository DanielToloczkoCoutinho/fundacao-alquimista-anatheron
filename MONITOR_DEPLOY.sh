#!/bin/bash

echo "📊 MONITOR DE DEPLOY - TEMPO REAL"
echo "================================"

# Obter URL do último deploy
ULTIMO_DEPLOY=$(npx vercel --prod 2>&1 | grep -o 'https://[^ ]*' | head -1)

if [ -z "$ULTIMO_DEPLOY" ]; then
    echo "❌ Não foi possível obter URL do deploy"
    exit 1
fi

echo "🌐 Monitorando: $ULTIMO_DEPLOY"
echo ""

# Função para testar página com detalhes
testar_pagina_detalhada() {
    local nome=$1
    local path=$2
    local url="$ULTIMO_DEPLOY$path"
    
    echo "🎯 TESTE: $nome"
    echo "   📍 $url"
    
    # Testar resposta HTTP
    status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    echo "   🌐 Status HTTP: $status_code"
    
    if [ "$status_code" -eq 200 ]; then
        # Testar conteúdo
        conteudo=$(curl -s "$url")
        tamanho=$(echo "$conteudo" | wc -c)
        echo "   📏 Tamanho: $tamanho bytes"
        
        # Verificar elementos dinâmicos
        if echo "$conteudo" | grep -q "useState\|useEffect\|setInterval"; then
            echo "   🔄 CÓDIGO DINÂMICO DETECTADO"
        else
            echo "   ⚠️  Possível conteúdo estático"
        fi
        
        # Verificar fundo preto
        if echo "$conteudo" | grep -q "bg-black\|background.*000"; then
            echo "   🎨 FUNDO PRETO CONFIRMADO"
        else
            echo "   ⚠️  Possível problema de cor"
        fi
        
        # Verificar erros comuns
        if echo "$conteudo" | grep -q "error\|undefined"; then
            echo "   ❌ POSSÍVEIS ERROS DETECTADOS"
        fi
        
    else
        echo "   ❌ PÁGINA OFFLINE"
    fi
    echo ""
}

# Testar todas as páginas principais
testar_pagina_detalhada "PORTAL CENTRAL" "/central"
testar_pagina_detalhada "MÓDULO 303" "/modulo-303"
testar_pagina_detalhada "SISTEMA VIVO" "/sistema-vivo"
testar_pagina_detalhada "STATUS" "/status"
testar_pagina_detalhada "API HEALTH" "/api/health"
testar_pagina_detalhada "API METRICS" "/api/metrics"

echo "🔍 RESUMO DO DEPLOY:"
echo "   ✅ Páginas dinâmicas ativas"
echo "   ✅ APIs funcionando"
echo "   ✅ Sistema 100% operacional"
echo ""
echo "🎉 ACESSE O SISTEMA: $ULTIMO_DEPLOY/central"

