#!/bin/bash
echo "🔍 MONITOR MÓDULO 303 - $(date)"
curl -s https://fundacao-alquimista-anatheron-em9s1t83d.vercel.app/modulo-303 > /dev/null && echo "✅ ONLINE" || echo "❌ OFFLINE"
