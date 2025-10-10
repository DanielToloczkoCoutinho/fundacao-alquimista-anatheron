#!/bin/bash
echo "🔍 VERIFICANDO TODAS AS INTERFACES"
echo "================================="

urls=(
  "https://fundacao-alquimista-anatheron.vercel.app/dashboard-real-interativo"
  "https://fundacao-alquimista-anatheron.vercel.app/verdade-real"
  "https://fundacao-alquimista-anatheron.vercel.app/quantum-interface"
  "https://fundacao-alquimista-anatheron.vercel.app/visualizacao-3d"
  "https://fundacao-alquimista-anatheron.vercel.app/blockchain-dashboard"
)

echo "🌐 TESTANDO INTERFACES:"
for url in "${urls[@]}"; do
  status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$status_code" -eq 200 ]; then
    echo "   ✅ $url - ONLINE"
  else
    echo "   ❌ $url - OFFLINE ($status_code)"
  fi
done

echo ""
echo "🎨 RESUMO DAS INTERFACES:"
echo "   📊 Dashboard Interativo - Gráficos em tempo real"
echo "   �� Verdade Real - Dados verificados do backend" 
echo "   ⚛️ Quantum Interface - Circuitos quânticos"
echo "   🎮 Visualização 3D - Sistemas 3D e gaming"
echo "   ⛓️ Blockchain Dashboard - Sistemas descentralizados"
echo ""
echo "💡 DICA: Acesse as URLs para ver a diferença entre 'apenas letras' e 'interfaces reais'!"
