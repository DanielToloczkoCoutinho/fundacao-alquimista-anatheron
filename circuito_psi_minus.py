# 👑 ESTADO |Ψ⁻⟩ = (|01⟩ - |10⟩)/√2
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print("🌌 CRIANDO |Ψ⁻⟩...")
qc = QuantumCircuit(2, 2)
qc.x(1)
qc.h(0)
qc.cx(0, 1)
qc.z(0)
qc.measure_all()

simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print(f"🎯 RESULTADOS: {counts}")

total = sum(counts.values())
corr = (counts.get('01', 0) + counts.get('10', 0)) / total * 100
print(f"🧪 CORRELAÇÃO: {corr:.2f}%")
