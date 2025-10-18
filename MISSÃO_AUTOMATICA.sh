#!/bin/bash
# ⚛️ MISSÃO QUÂNTICA AUTOMÁTICA
# 🚀 Entra DIRETAMENTE em uma missão quântica

cd ~/fundacao-alquimista-anatheron
source /tmp/fundacao_venv/bin/activate

python3 -c "
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

print('')
print('⚛️  MISSÃO QUÂNTICA AUTOMÁTICA - FUNDAÇÃO ALQUIMISTA')
print('=' * 55)
print('🚀 INICIANDO MISSÃO DIRETA...')
print('')

# Missão 1: Estado Bell
print('1. 🔮 CRIANDO ESTADO BELL...')
qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.cx(0, 1)
qc1.measure_all()

backend = AerSimulator()
result1 = backend.run(qc1, shots=100).result()
counts1 = result1.get_counts()
print(f'   📊 Resultado: {counts1}')

# Missão 2: Circuito Avançado
print('')
print('2. 🌟 CIRCUITO QUÂNTICO AVANÇADO...')
qc2 = QuantumCircuit(3)
qc2.h(0)
qc2.cx(0, 1)
qc2.cx(1, 2)
qc2.ry(np.pi/4, 0)
qc2.rz(np.pi/3, 1)
qc2.measure_all()

result2 = backend.run(qc2, shots=200).result()
counts2 = result2.get_counts()

# Mostrar top resultados
top3 = sorted(counts2.items(), key=lambda x: x[1], reverse=True)[:3]
print(f'   📊 Top 3 estados: {dict(top3)}')

print('')
print('🎉 MISSÃO CONCLUÍDA COM SUCESSO!')
print('🌌 VOCÊ ESTÁ NO AMBIENTE QUÂNTICO!')
print('')
print('�� Agora continue programando:')
print('   qc = QuantumCircuit(2)')
print('   qc.h(0)')
print('   qc.cx(0, 1)')
print('   result = backend.run(qc, shots=100).result()')
print('')

# Manter no Python interativo
print('🔧 Digite seus comandos quânticos ou Ctrl+D para sair')
" -i
