#!/bin/bash

echo "🧪 TESTE DE DINAMISMO DAS PÁGINAS"
echo "================================"

URL_ATUAL="https://fundacao-alquimista-anatheron-lxluzjev8.vercel.app"

echo "🌐 Testando URL atual: $URL_ATUAL"
echo ""

testar_dinamismo() {
    local nome=$1
    local path=$2
    local url="$URL_ATUAL$path"
    
    echo "🎯 $nome:"
    echo "   📍 $url"
    
    # Fazer requisição e verificar conteúdo
    conteudo=$(curl -s "$url")
    
    if echo "$conteudo" | grep -q "useState\|useEffect\|setInterval"; then
        echo "   ✅ Código React dinâmico detectado"
    else
        echo "   ⚠️  Possívelmente estático"
    fi
    
    # Verificar se tem elementos que indicam dinamismo
    if echo "$conteudo" | grep -q "animate-pulse\|transition-all"; then
        echo "   🎨 Animações CSS detectadas"
    fi
    
    # Verificar tamanho
    tamanho=$(echo "$conteudo" | wc -c)
    echo "   📏 Tamanho: $tamanho bytes"
}

testar_dinamismo "Portal Central" "/central"
testar_dinamismo "Módulo 303" "/modulo-303"
testar_dinamismo "Sistema Vivo" "/sistema-vivo"
testar_dinamismo "Status" "/status"

echo ""
echo "🔍 OBSERVAÇÃO IMPORTANTE:"
echo "-------------------------"
echo "Mesmo que as páginas apareçam como '○ (Static)' no build,"
echo "elas podem ser DINÂMICAS no cliente se:"
echo ""
echo "✅ Tem 'use client' no topo"
echo "✅ Usam useState/useEffect"  
echo "✅ Tem setInterval/setTimeout"
echo "✅ Atualizam estado em tempo real"
echo ""
echo "O '○ (Static)' apenas significa que o HTML inicial é pré-renderizado,"
echo "mas o JavaScript no cliente torna-as dinâmicas!"

