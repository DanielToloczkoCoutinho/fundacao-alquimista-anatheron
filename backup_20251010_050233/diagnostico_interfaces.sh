#!/bin/bash
echo "🔬 DIAGNÓSTICO DAS INTERFACES DA FUNDAÇÃO"
echo "=========================================="

# 1. Verificar build do Next.js
echo "1. 🏗️  VERIFICANDO BUILD NEXT.JS:"
if [ -d "/home/user/studio/.next" ]; then
    echo "   ✅ .next/ existe"
    find /home/user/studio/.next -name "*.js" | head -5
else
    echo "   ❌ .next/ NÃO ENCONTRADO"
fi

# 2. Verificar componentes
echo "2. 📦 VERIFICANDO COMPONENTES:"
find /home/user/studio/components -name "*.tsx" -o -name "*.jsx" | head -10

# 3. Verificar se Three.js está carregando
echo "3. 🎮 VERIFICANDO THREE.JS:"
if grep -r "three" /home/user/studio/package.json; then
    echo "   ✅ Three.js no package.json"
else
    echo "   ❌ Three.js NÃO encontrado"
fi

# 4. Testar renderização real
echo "4. 🌐 TESTANDO RENDERIZAÇÃO:"
curl -s https://fundacao-alquimista-anatheron.vercel.app/laboratorios/energy > teste_energy.html
echo "   📄 Página salva como teste_energy.html"

# 5. Verificar erros no console
echo "5. 🚨 VERIFICANDO ERROS:"
echo "   Abra o navegador e pressione F12 -> Console"
echo "   Procure por erros JavaScript"

# 6. Verificar estrutura de componentes
echo "6. 🏗️  ESTRUTURA DE COMPONENTES:"
find /home/user/studio/app/laboratorios -type f -name "*.tsx" | while read file; do
    echo "   📁 $(basename $file):"
    grep -c "export default" "$file" | xargs echo "     - Componentes:"
    grep -c "function\\|const.*=.*()" "$file" | xargs echo "     - Funções:"
done

echo "=========================================="
echo "🎯 DIAGNÓSTICO COMPLETO!"
