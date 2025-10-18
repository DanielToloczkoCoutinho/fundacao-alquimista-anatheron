#!/bin/bash
# 🐍 PYTHON QUÂNTICO DIRETO
# ⚛️ Acesso imediato ao Python com Qiskit carregado

cd ~/fundacao-alquimista-anatheron
source /tmp/fundacao_venv/bin/activate

# Executar Python com imports pré-carregados
python3 -i -c "
print('')
print('🐍 PYTHON QUÂNTICO - FUNDAÇÃO ALQUIMISTA')
print('=' * 45)
print('⚛️  Todos os imports já carregados:')
print('   • QuantumCircuit, AerSimulator')
print('   • numpy, matplotlib')
print('')

from qiskit import QuantumCircuit, __version__ as qiskit_ver
from qiskit_aer import AerSimulator
import numpy as np

print(f'✅ Qiskit {qiskit_ver} carregado')
print('✅ NumPy carregado')
print('✅ Aer Simulator carregado')
print('')

# Criar variáveis úteis já disponíveis
simulator = AerSimulator()

print('💡 Variáveis disponíveis:')
print('   - simulator = AerSimulator()')
print('   - qc = QuantumCircuit(2) # Crie seus circuitos')
print('   - np # NumPy para cálculos')
print('')

print('🚀 PRONTO PARA COMPUTAÇÃO QUÂNTICA!')
print('')
"
