#!/bin/bash
# 🚀 EXECUTOR DA FASE 1: CONFIGURAÇÃO DO SISTEMA
# 📅 Gerado em: 2025-10-18 00:00:58
# 📊 Scripts: 5
echo "🚀 INICIANDO FASE $1..."

echo "🎯 Executando: PREPARADOR_AMBIENTE_LIMPO.py"
python3 "/home/user/fundacao-alquimista-anatheron/PREPARADOR_AMBIENTE_LIMPO.py"
if [ $? -eq 0 ]; then
    echo "✅ SUCESSO: {script['nome']}"
else
    echo "❌ FALHA: {script['nome']}"
    exit 1
fi
echo ""
echo "🎉 FASE 1 CONCLUÍDA COM SUCESSO!"
