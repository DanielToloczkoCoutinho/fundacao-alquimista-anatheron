#!/bin/bash

echo "🔍 ANÁLISE PROFUNDA DO SISTEMA ALQUIMISTA"
echo "=========================================="
echo "📊 Verificando cada página e suas conexões..."
echo ""

SISTEMA_URL="https://fundacao-alquimista-anatheron-58nmzylbj.vercel.app"

# Função para análise detalhada de cada página
analisar_pagina() {
    local pagina=$1
    local nome=$2
    local url="$SISTEMA_URL$pagina"
    
    echo "🔎 ANALISANDO: $nome"
    echo "   🌐 URL: $url"
    
    # Fazer requisição e analisar conteúdo
    conteudo=$(curl -s "$url")
    
    # Verificar se página carrega
    if [ -z "$conteudo" ]; then
        echo "   ❌ PÁGINA VAZIA OU INACESSÍVEL"
        return 1
    fi
    
    # Análise de conteúdo
    echo "   📊 Análise de conteúdo:"
    
    # Verificar elementos dinâmicos
    if echo "$conteudo" | grep -q "useState\|useEffect"; then
        echo "   ✅ Contém React Hooks (Dinâmico)"
    else
        echo "   ⚠️  Possivelmente estático"
    fi
    
    # Verificar dados específicos
    if echo "$conteudo" | grep -q "OPERACIONAL\|ONLINE"; then
        echo "   ✅ Status operacional presente"
    fi
    
    # Verificar se tem logs/atualizações
    if echo "$conteudo" | grep -q "logs\|atualizações\|tempo real"; then
        echo "   🔄 Elementos de tempo real detectados"
    fi
    
    # Verificar interatividade
    if echo "$conteudo" | grep -q "onClick\|onChange\|button"; then
        echo "   🖱️  Elementos interativos presentes"
    fi
    
    # Tamanho do conteúdo
    tamanho=$(echo "$conteudo" | wc -c)
    echo "   📏 Tamanho: $tamanho bytes"
    
    echo ""
}

# Analisar cada página principal
echo "📋 PÁGINAS PRINCIPAIS:"
echo "======================"
analisar_pagina "/central" "Portal Central"
analisar_pagina "/modulo-303" "Módulo 303 - Realidade Quântica"
analisar_pagina "/sistema-vivo" "Sistema Vivo - Dashboard"
analisar_pagina "/metadados-reais" "Metadados Reais - Captura"
analisar_pagina "/status" "Status do Sistema"
analisar_pagina "/api/health" "API Health"
analisar_pagina "/api/metrics" "API Metrics"

# Testar funcionalidades específicas
echo "🧪 TESTES ESPECÍFICOS:"
echo "======================"

# Testar se as APIs retornam JSON válido
echo "🔧 Testando APIs:"
health_response=$(curl -s "$SISTEMA_URL/api/health")
if echo "$health_response" | grep -q '"status":"operational"'; then
    echo "   ✅ API Health funcionando"
else
    echo "   ❌ API Health com problema"
fi

metrics_response=$(curl -s "$SISTEMA_URL/api/metrics") 
if echo "$metrics_response" | grep -q '"circuitos_quantico"'; then
    echo "   ✅ API Metrics funcionando"
else
    echo "   ❌ API Metrics com problema"
fi

# Verificar arquivos no build
echo ""
echo "📁 VERIFICAÇÃO DE ARQUIVOS:"
echo "==========================="
echo "Arquivos no diretório app/:"
find app -name "*.js" -type f | head -10 | while read file; do
    echo "   📄 $file"
done

echo ""
echo "🔍 VERIFICANDO CONTEÚDO DINÂMICO NOS ARQUIVOS:"
for file in app/modulo-303/page.js app/sistema-vivo/page.js app/metadados-reais/page.js; do
    if [ -f "$file" ]; then
        echo "📄 $file:"
        echo "   - useState: $(grep -c "useState" "$file")"
        echo "   - useEffect: $(grep -c "useEffect" "$file")" 
        echo "   - setInterval/setTimeout: $(grep -c "setInterval\|setTimeout" "$file")"
    fi
done

