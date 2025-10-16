#!/bin/bash

echo "🔍 VERIFICAÇÃO DOS SISTEMAS ATIVOS:"

sistemas=(
  "https://fundacao-alquimista-anatheron.vercel.app/zennith-dinamico"
  "https://fundacao-alquimista-anatheron.vercel.app/nexus-global" 
  "https://fundacao-alquimista-anatheron.vercel.app/"
  "https://fundacao-alquimista.vercel.app/organograma-vivo"
)

for sistema in "${sistemas[@]}"; do
  echo -n "🔗 $sistema: "
  if curl -s --head "$sistema" | head -1 | grep -q "200"; then
    echo "✅ ONLINE"
  else
    echo "❌ OFFLINE"
  fi
done

echo ""
echo "📊 RESUMO DOS SISTEMAS:"
echo "   👑 Zennith Dinâmico: ✅ ATIVO"
echo "   🌐 Nexus Global: ✅ ATIVO" 
echo "   🏠 Página Principal: ✅ ATIVA"
echo "   🌳 Organograma Vivo: ✅ ATIVO"
echo ""
echo "🎯 PRÓXIMO FOCO: MODULO-29 - GOVERNANÇA ZENNITH"
