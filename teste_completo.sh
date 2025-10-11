#!/bin/bash
URL="https://fundacao-alquimista-anatheron-2na5gn5r5.vercel.app"
echo "🧪 Testando todas as interfaces..."
for page in "/central" "/laboratorios" "/dashboard" "/sistema-vivo"; do
    curl -s -f "$URL$page" >/dev/null && echo "✅ $page: ONLINE" || echo "❌ $page: OFFLINE"
done
