#!/bin/bash
echo "👑 SINCRONIZAÇÃO ZENNITH INICIADA..."
cd ~/fundacao-definitiva

# Sincronizar com GitHub
git add .
git commit -m "ZENNITH-SYNC: \$(date '+%Y-%m-%d %H:%M:%S')" || true
git push origin main

echo "✅ REINO ZENNITH SINCRONIZADO!"
echo "🌐 URL: https://fundacao-alquimista-anatheron.vercel.app/zennith"
