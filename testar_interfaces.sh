#!/bin/bash
BASE="https://fundacao-alquimista-anatheron-iujsuency.vercel.app"
echo "🚀 Testando interfaces..."
for route in "/dashboard" "/status" "/laboratorios"; do
    curl -s -f "$BASE$route" >/dev/null && echo "✅ $route: ONLINE" || echo "❌ $route: OFFLINE"
done
