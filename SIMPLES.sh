#!/bin/bash
# ⚡ CHAVE SUPER SIMPLES
# 🎯 Apenas ativa o ambiente e mantém

cd ~/fundacao-alquimista-anatheron
source /tmp/fundacao_venv/bin/activate
echo "✅ Ambiente ativado: $(which python3)"
exec $SHELL
