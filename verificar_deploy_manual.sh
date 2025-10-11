#!/bin/bash
URL="https://fundacao-alquimista-anatheron-iujsuency.vercel.app"
echo "🌐 Verificando deploy manual..."
curl -s -f "$URL" >/dev/null && echo "🎉 ✅ SISTEMA ONLINE!" || echo "⏳ Carregando..."
echo "🔗 Acesse: $URL"
