#!/bin/bash
# 🚀 INICIALIZADOR DEFINITIVO CORRETO - FUNDAÇÃO ALQUIMISTA
# 🌌 Usa ambiente Nix comprovadamente funcional

echo "🌌 FUNDAÇÃO ALQUIMISTA - INICIALIZADOR DEFINITIVO"
echo "================================================="

# SEMPRE usar o venv que funciona com Nix
VENV_PATH="/tmp/fundacao_venv"

if [ ! -d "$VENV_PATH" ]; then
    echo "❌ Ambiente nao encontrado. Execute primeiro:"
    echo "   nix-shell .idx/dev_hibrido.nix"
    echo "   source /tmp/fundacao_venv/bin/activate"
    exit 1
fi

# Ativar venv funcional
source $VENV_PATH/bin/activate

echo "🔍 VERIFICACAO DO SISTEMA DEFINITIVO:"
python3 -c "
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print('✅ NumPy:', np.__version__)
print('✅ Qiskit: OPERACIONAL')
print('✅ Aer Simulator: FUNCIONANDO')

# Teste definitivo
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure_all()
result = AerSimulator().run(qc, shots=100).result()
print('✅ Teste quantico: CONCLUIDO')

print('')
print('🎉 SISTEMA FUNDACAO ALQUIMISTA: DEFINITIVAMENTE OPERACIONAL!')
"

echo ""
echo "💡 COMANDOS DISPONIVEIS:"
echo "   python3 sistema_fundacao_definitivo.py  # Sistema principal"
echo "   python3 missao_corrigida.py             # Missoes basicas"
echo ""
echo "🚀 AMBIENTE PRONTO PARA MISSOES QUANTICAS!"
