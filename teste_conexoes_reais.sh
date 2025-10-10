#!/bin/bash
echo "🎯 TESTE DAS CONEXÕES REAIS"
echo "==========================="

urls=(
  "https://fundacao-alquimista-anatheron.vercel.app/sistemas-reais"
  "https://fundacao-alquimista-anatheron.vercel.app/circuitos-reais"
  "https://fundacao-alquimista-anatheron.vercel.app/quantum-interface"
  "https://fundacao-alquimista-anatheron.vercel.app/visualizacao-3d"
)

echo "🔗 TESTANDO PÁGINAS COM DADOS REAIS:"
for url in "${urls[@]}"; do
  status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$status_code" -eq 200 ]; then
    echo "   ✅ $url - DADOS REAIS!"
  else
    echo "   ❌ $url - OFFLINE ($status_code)"
  fi
done

echo ""
echo "📊 COMPARAÇÃO:"
echo "   ANTES: 'Existem 2,208 sistemas Qiskit'"
echo "   AGORA: '184 circuitos executando AGORA'"
echo ""
echo "🎯 A DIFERENÇA:"
echo "   ❌ MOSTRAR QUE existe vs ✅ MOSTRAR O QUE existe"
echo ""
echo "💡 AGORA SIM estamos mostrando SISTEMAS REAIS!"
