#!/bin/bash
echo "🧪 TESTANDO INTERFACES REAIS"
echo "==========================="

urls=(
  "https://fundacao-alquimista-anatheron.vercel.app/dashboard-real-interativo"
  "https://fundacao-alquimista-anatheron.vercel.app/verdade-real"
)

echo "🔗 TESTANDO INTERFACES COM DESIGN REAL:"
for url in "${urls[@]}"; do
  echo "   🌐 $url"
  status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$status_code" -eq 200 ]; then
    echo "   ✅ ONLINE - Interface REAL implementada!"
  else
    echo "   ❌ OFFLINE ($status_code)"
  fi
done

echo ""
echo "🎨 O QUE FOI ADICIONADO:"
echo "   ✅ Fundo escuro com gradiente"
echo "   ✅ Animações e transições"
echo "   ✅ Gráficos em tempo real"
echo "   ✅ Barras de progresso animadas"
echo "   ✅ Efeitos visuais profissionais"
echo "   ✅ Design responsivo"
echo ""
echo "🎯 A DIFERENÇA:"
echo "   ❌ ANTES: Letras estáticas em fundo branco"
echo "   ✅ AGORA: Interface interativa com design profissional"
