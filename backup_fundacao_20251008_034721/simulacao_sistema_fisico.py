# 🔬 SIMULAÇÃO DE SISTEMA FÍSICO (SPINS)
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

print("🔬 INICIANDO SIMULAÇÃO DE SISTEMA FÍSICO...")

# Simular sistema de 2 spins com interação
def criar_sistema_ising(n_qubits=2, interacao=1.0):
    qc = QuantumCircuit(n_qubits, n_qubits)
    
    # Estado inicial aleatório
    for i in range(n_qubits):
        qc.rx(np.random.random() * np.pi, i)
    
    # Interação tipo Ising
    for i in range(n_qubits-1):
        qc.rzz(interacao, i, i+1)  # Interação ZZ
    
    # Medir todos os spins
    qc.measure(range(n_qubits), range(n_qubits))
    return qc

# Criar e simular sistema
qc_ising = criar_sistema_ising()
simulator = AerSimulator()
result = simulator.run(qc_ising, shots=1024).result()
counts = result.get_counts()

print(f"🎯 DISTRIBUIÇÃO DE SPINS: {counts}")

# Análise de correlação
total = sum(counts.values())
correlacao = (counts.get('00', 0) + counts.get('11', 0)) / total * 100
print(f"🧲 CORRELAÇÃO ENTRE SPINS: {correlacao:.2f}%")

if correlacao > 60:
    print("💫 FORTE CORRELAÇÃO DETECTADA!")
else:
    print("⚗️ CORRELAÇÃO MODERADA")

print("✅ SIMULAÇÃO CONCLUÍDA!")
