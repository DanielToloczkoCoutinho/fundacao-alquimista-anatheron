#!/bin/bash
echo "🌐 Verificando deploy no Vercel..."
urls=(
  "https://fundacao-alquimista.vercel.app"
  "https://fundacao-alquimista.vercel.app/dashboard"
  "https://fundacao-alquimista.vercel.app/status"
)
for url in "${urls[@]}"; do
  echo -n "• $url: "
  status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  [ "$status_code" = "200" ] && echo "✅ ONLINE" || echo "❌ OFFLINE"
done
