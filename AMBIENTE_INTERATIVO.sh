#!/bin/bash
# 🔧 AMBIENTE INTERATIVO QUÂNTICO
# 🎯 Entra no Python interativo com tudo carregado

echo "🔧 INICIANDO AMBIENTE INTERATIVO QUÂNTICO..."
cd ~/fundacao-alquimista-anatheron
source /tmp/fundacao_venv/bin/activate

# Criar script temporário com imports
cat > /tmp/quantum_env.py << 'IMPORTS'
print("🔧 CARREGANDO AMBIENTE QUÂNTICO...")
print("=" * 40)

# Imports principais
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

print("✅ QuantumCircuit, AerSimulator carregados")
print("✅ NumPy, Matplotlib carregados")
print("")

# Configurações úteis
simulator = AerSimulator()
print("🔧 Variáveis configuradas:")
print("   - simulator = AerSimulator()")
print("   - np = numpy")
print("   - plt = matplotlib.pyplot")
print("")

# Função útil rápida
def circuito_rapido(n_qubits=2):
    '''Cria circuito quântico rápido'''
    qc = QuantumCircuit(n_qubits)
    for i in range(n_qubits):
        qc.h(i)
    for i in range(n_qubits-1):
        qc.cx(i, i+1)
    qc.measure_all()
    return qc

print("💡 Função disponível: circuito_rapido(n_qubits)")
print("   Exemplo: qc = circuito_rapido(3)")
print("   result = simulator.run(qc, shots=100).result()")
print("   counts = result.get_counts()")
print("")

print("🎉 AMBIENTE QUÂNTICO PRONTO!")
print("🚀 Comece a programar!")
print("")
IMPORTS

# Entrar no Python interativo com o ambiente carregado
python3 -i /tmp/quantum_env.py
