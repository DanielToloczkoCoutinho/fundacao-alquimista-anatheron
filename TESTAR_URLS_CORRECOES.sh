#!/bin/bash

echo "�� TESTANDO URLs DAS CORREÇÕES DIRETAMENTE"
echo "=========================================="

# Obter a URL base do último deploy
URL_BASE=$(npx vercel --prod 2>&1 | grep -o 'https://[^ ]*' | head -1)

if [ -z "$URL_BASE" ]; then
    echo "❌ Não foi possível obter a URL do deploy"
    exit 1
fi

echo "🔗 URL Base: $URL_BASE"
echo ""

# Testar cada URL
test_url() {
    local path=$1
    local description=$2
    local url="${URL_BASE}${path}"
    
    echo "🔍 Testando: $description"
    echo "   URL: $url"
    
    # Fazer requisição e verificar status
    response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    
    if [ "$response" -eq 200 ]; then
        echo "   ✅ Status: $response - FUNCIONAL"
        
        # Verificar se a página tem conteúdo dinâmico
        content=$(curl -s "$url")
        if echo "$content" | grep -q "useState\|useEffect\|setInterval"; then
            echo "   🔄 Contém código dinâmico"
        else
            echo "   ⚠️  Pode ser estática"
        fi
        
    elif [ "$response" -eq 404 ]; then
        echo "   ❌ Status: $response - NÃO ENCONTRADA"
    else
        echo "   ⚠️  Status: $response - VERIFICAR"
    fi
    echo ""
}

# Testar todas as URLs importantes
test_url "/central" "Portal Central"
test_url "/modulo-303" "Módulo 303 Dinâmico"
test_url "/metadados-reais" "Metadados Reais"
test_url "/sistema-vivo" "Sistema Vivo Dashboard"
test_url "/status" "Status Monitoramento"
test_url "/api/health" "Health Check API"
test_url "/api/metrics" "Métricas API"

echo "📋 RESUMO DOS TESTES:"
echo "---------------------"
echo "Se todas as URLs retornarem 200, o sistema está operacional!"
echo "Verifique manualmente as páginas para confirmar funcionalidades dinâmicas."

