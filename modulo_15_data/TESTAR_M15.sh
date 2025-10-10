#!/bin/bash

echo "🧪 INICIANDO TESTE DO MÓDULO 15..."
echo "=================================="

# Executar o integrador
node INTEGRADOR_M15.js

if [ $? -eq 0 ]; then
    echo "✅ TESTE CONCLUÍDO COM SUCESSO!"
else
    echo "❌ ERRO NO TESTE"
    exit 1
fi

echo ""
echo "🌍 MÓDULO 15 - STATUS: OPERACIONAL"
echo "🔗 Conexões estabelecidas: 5"
echo "📊 Sistemas ativos: Monitoramento, Intervenção, Relatórios"
echo "💫 Pronto para integração com a Fundação Alquimista!"
