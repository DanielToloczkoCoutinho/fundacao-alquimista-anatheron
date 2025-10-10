#!/bin/bash
echo "🏥 VERIFICADOR DE SAÚDE DO SISTEMA"
echo "================================="

echo "�� FRONTEND:"
echo "   📁 Páginas: $(find /home/user/studio/app -name "page.tsx" 2>/dev/null | wc -l)"
echo "   🏗️ Build: $(ls -la /home/user/studio/.next 2>/dev/null | head -1 | cut -d' ' -f6-8)"

echo ""
echo "🔧 BACKEND:"
echo "   🐍 Python: $(find /home/user -name "*.py" 2>/dev/null | wc -l) arquivos"
echo "   📚 Libs: $(find /home/user -name "requirements.txt" -o -name "package.json" 2>/dev/null | wc -l)"

echo ""
echo "🌐 CONEXÕES:"
urls=("dashboard-real" "tecnologias-reais" "organograma")
for url in "${urls[@]}"; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "https://fundacao-alquimista-anatheron.vercel.app/$url")
    if [ "$status" -eq 200 ]; then
        echo "   ✅ $url: CONECTADO"
    else
        echo "   ❌ $url: PROBLEMA ($status)"
    fi
done

echo ""
echo "🎯 DIAGNÓSTICO:"
if [ $(find /home/user/studio/app -name "page.tsx" | wc -l) -gt 20 ]; then
    echo "   🟢 FRONTEND: SAUDÁVEL"
else
    echo "   🔴 FRONTEND: PROBLEMAS"
fi

if [ $(find /home/user -name "*.py" | wc -l) -gt 10000 ]; then
    echo "   🟢 BACKEND: SAUDÁVEL"
else
    echo "   🔴 BACKEND: PROBLEMAS"
fi
