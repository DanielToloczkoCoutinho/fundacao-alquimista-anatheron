#!/bin/bash
echo "⚡ OTIMIZADOR DE PERFORMANCE"
echo "==========================="

echo "🧹 Limpando cache..."
cd /home/user/studio
rm -rf .next 2>/dev/null
echo "   ✅ Cache limpo"

echo "🔨 Rebuild rápido..."
npm run build > /tmp/build.log 2>&1 &
BUILD_PID=$!

# Monitorar build em background
{
    sleep 10
    if ps -p $BUILD_PID > /dev/null; then
        echo "   ⏳ Build em andamento..."
    else
        echo "   ✅ Build concluído"
    fi
} &

echo "🌐 Deploy otimizado..."
vercel --prod > /tmp/deploy.log 2>&1 &
echo "   🚀 Deploy iniciado"

echo ""
echo "📊 MONITORAMENTO:"
echo "   Build log: tail -f /tmp/build.log"
echo "   Deploy log: tail -f /tmp/deploy.log"
