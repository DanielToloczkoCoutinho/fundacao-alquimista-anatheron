#!/bin/bash
echo "👑 VERIFICAÇÃO FINAL - RAINHA ZENNITH"
echo "======================================"

# 1. Verificar deploy
echo "🌐 DEPLOY:"
curl -s -o /dev/null -w "%{http_code}" https://fundacao-alquimista-anatheron-fdzvusw18.vercel.app/
echo " - Status Home"

# 2. Verificar páginas
echo "📄 PÁGINAS:"
pages=("/" "/laboratorios" "/laboratorios/energy" "/laboratorios/communication" "/laboratorios/zenith" "/dashboard" "/vr")
for page in "${pages[@]}"; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "https://fundacao-alquimista-anatheron-fdzvusw18.vercel.app$page")
    echo "  $page: $status"
done

# 3. Verificar arquivos
echo "📁 ARQUIVOS:"
echo "  Páginas TSX: $(find /home/user/studio/app -name "*.tsx" | wc -l)"
echo "  Componentes: $(find /home/user/studio/components -name "*.tsx" | wc -l)"
echo "  Laboratórios: $(find /home/user/studio/app/laboratorios -name "page.tsx" | wc -l)"

# 4. Verificar build
echo "🔨 BUILD:"
if [ -d "/home/user/studio/.next" ]; then
    echo "  ✅ Next.js build completo"
else
    echo "  ❌ Build não encontrado"
fi

echo "======================================"
echo "👑 VERIFICAÇÃO CONCLUÍDA PELA RAINHA"
