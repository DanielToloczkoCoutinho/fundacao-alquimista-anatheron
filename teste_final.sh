#!/bin/bash
echo "🎯 TESTE FINAL - TODAS AS PÁGINAS"
echo "================================"

urls=(
  "https://fundacao-alquimista-anatheron.vercel.app/analise-zennith"
  "https://fundacao-alquimista-anatheron.vercel.app/portal"
  "https://fundacao-alquimista-anatheron.vercel.app/organograma"
  "https://fundacao-alquimista-anatheron.vercel.app/laboratorios"
  "https://fundacao-alquimista-anatheron.vercel.app/mapa-modulos"
)

for url in "${urls[@]}"; do
  echo "🔗 Testando: $url"
  status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$status_code" -eq 200 ]; then
    echo "   ✅ ONLINE (200)"
  else
    echo "   ❌ OFFLINE ($status_code)"
  fi
done

echo "================================"
echo "🎉 SISTEMA COMPLETO!"
