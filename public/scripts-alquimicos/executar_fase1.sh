#!/bin/bash
# 🎯 DIRECIONAMENTO: /home/user/fundacao-alquimista-limpa
echo "🔄 FASE 1 - SINCRONIZAÇÃO TOTAL DA BASE"
echo "📍 LOCAL: /home/user/fundacao-alquimista-limpa"
echo "=============================================="

cd /home/user/fundacao-alquimista-limpa

echo "🔍 Verificando scripts disponíveis..."
ls -la ./scripts/ | head -10

if [ -f "./scripts/sincronizar-tudo.sh" ]; then
    echo "✅ ENCONTRADO: sincronizar-tudo.sh"
    echo "⚡ EXECUTANDO SINCRONIZAÇÃO..."
    chmod +x ./scripts/sincronizar-tudo.sh
    ./scripts/sincronizar-tudo.sh
else
    echo "❌ sincronizar-tudo.sh não encontrado na Fundação"
    echo "📋 Scripts disponíveis:"
    find ./scripts/ -name "*.sh" -type f | head -10
fi
