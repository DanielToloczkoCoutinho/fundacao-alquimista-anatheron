# 👑 ESTADO |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print("🌌 CRIANDO |Φ⁺⟩...")
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])  # CORREÇÃO: Medir específico

simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print(f"🎯 RESULTADOS: {counts}")

# Análise
total = sum(counts.values())
corr = (counts.get('00', 0) + counts.get('11', 0)) / total * 100
print(f"🧪 CORRELAÇÃO: {corr:.2f}%")

if corr > 80:
    print("💫 EMRANHAMENTO CONFIRMADO!")
