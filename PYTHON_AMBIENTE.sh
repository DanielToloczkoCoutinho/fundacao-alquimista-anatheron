#!/bin/bash
# 🐍 PYTHON DO AMBIENTE - ENTRA DIRETO
# ⚛️ Entra diretamente no Python DO AMBIENTE (fundacao_venv)

cd ~/fundacao-alquimista-anatheron
source /tmp/fundacao_venv/bin/activate

echo "🐍 INICIANDO PYTHON DO AMBIENTE QUÂNTICO..."
echo "=========================================="
echo "🔧 Ambiente: $(which python3)"
echo "⚛️  Carregando bibliotecas quânticas..."
echo ""

# Entrar DIRETAMENTE no Python interativo DO AMBIENTE
python3 -i -c "
from qiskit import QuantumCircuit, __version__ as qver
from qiskit_aer import AerSimulator
import numpy as np

print('🌌 PYTHON QUÂNTICO - FUNDAÇÃO ALQUIMISTA')
print('=' * 45)
print(f'✅ Qiskit {qver} carregado')
print('✅ Aer Simulator carregado') 
print('✅ NumPy carregado')
print('')

# Executar demonstração automática
print('🚀 EXECUTANDO DEMONSTRAÇÃO...')
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)  
qc.cx(1, 2)
qc.measure_all()

result = AerSimulator().run(qc, shots=50).result()
counts = result.get_counts()
print(f'📊 Demonstração: {counts}')
print('')

print('🎉 AMBIENTE QUÂNTICO PRONTO!')
print('💫 Você está no Python interativo do ambiente')
print('🔧 Digite seus comandos quânticos abaixo:')
print('')
"
