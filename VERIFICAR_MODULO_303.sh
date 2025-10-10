#!/bin/bash

echo "🔮 VERIFICAÇÃO ESPECÍFICA DO MÓDULO 303"
echo "========================================"

# Verificar o arquivo atual do Módulo 303
echo "📄 CONTEÚDO ATUAL DO MÓDULO 303:"
echo "--------------------------------"

if [ -f "app/modulo-303/page.js" ]; then
    echo "✅ Arquivo existe"
    echo ""
    echo "🔍 Estrutura do arquivo:"
    grep -n "useState\|useEffect\|setInterval\|return" app/modulo-303/page.js | head -20
    
    echo ""
    echo "📊 Verificando funcionalidades:"
    
    # Verificar se tem intervalos
    if grep -q "setInterval" app/modulo-303/page.js; then
        echo "   ✅ setInterval encontrado - deve atualizar automaticamente"
        # Mostrar o intervalo
        grep "setInterval" app/modulo-303/page.js | sed 's/^/   🕒 /'
    else
        echo "   ❌ setInterval NÃO encontrado - não vai atualizar automaticamente"
    fi
    
    # Verificar estados
    estados=$(grep -c "useState" app/modulo-303/page.js)
    echo "   📦 Estados (useState): $estados"
    
    # Verificar efeitos
    efeitos=$(grep -c "useEffect" app/modulo-303/page.js)
    echo "   🔄 Efeitos (useEffect): $efeitos"
    
else
    echo "❌ Arquivo não encontrado!"
fi

# Verificar se há problemas no código
echo ""
echo "🔧 ANALISANDO POSSÍVEIS PROBLEMAS:"
echo "----------------------------------"

# Verificar se o setInterval está dentro de useEffect
if grep -A5 "useEffect" app/modulo-303/page.js | grep -q "setInterval"; then
    echo "   ✅ setInterval está dentro de useEffect - CORRETO"
else
    echo "   ❌ setInterval pode estar fora de useEffect - PROBLEMA"
fi

# Verificar se tem return de cleanup
if grep -A10 "useEffect" app/modulo-303/page.js | grep -q "clearInterval"; then
    echo "   ✅ clearInterval encontrado - cleanup correto"
else
    echo "   ⚠️  clearInterval não encontrado - possível memory leak"
fi

