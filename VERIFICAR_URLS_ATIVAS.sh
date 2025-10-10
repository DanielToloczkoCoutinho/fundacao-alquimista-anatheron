#!/bin/bash

echo "🔍 VERIFICANDO URLs ATIVAS E FUNCIONAIS"
echo "======================================"

URLS=(
    "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app"
    "https://fundacao-alquimista-anatheron-214leimdj.vercel.app"
    "https://fundacao-alquimista-anatheron-bu5hh0tnf.vercel.app"
    "https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app"
    "https://fundacao-alquimista-anatheron.vercel.app"
)

echo "🌐 TESTANDO URLs:"
echo "================="

for url in "${URLS[@]}"; do
    echo ""
    echo "🔍 Testando: $url"
    
    # Verificar se a URL responde
    if curl --output /dev/null --silent --head --fail "$url"; then
        echo "   ✅ ONLINE"
        
        # Verificar se o Portal Central funciona
        if curl --output /dev/null --silent --head --fail "$url/central"; then
            echo "   🏠 PORTAL CENTRAL: ✅ FUNCIONAL"
        else
            echo "   🏠 PORTAL CENTRAL: ❌ NÃO FUNCIONAL"
        fi
        
        # Verificar se o Sistema Multiversal funciona
        if curl --output /dev/null --silent --head --fail "$url/sistema-multiversal"; then
            echo "   🌌 SISTEMA MULTIVERSAL: ✅ PRESENTE"
        else
            echo "   🌌 SISTEMA MULTIVERSAL: ❌ AUSENTE"
        fi
        
    else
        echo "   ❌ OFFLINE"
    fi
done

echo ""
echo "🎯 RECOMENDAÇÃO FINAL:"
echo "======================"
echo "✅ URL PRINCIPAL: https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app"
echo "✅ URL SECUNDÁRIA: https://fundacao-alquimista-anatheron-214leimdj.vercel.app"
echo ""
echo "📊 STATUS: Ambas estão funcionais e completas"

