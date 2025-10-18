# 👑 ESTADO |Φ⁻⟩ = (|00⟩ - |11⟩)/√2
from qiskit import # 🔮 CIRCUITO OTIMIZADO PARA IBM QUANTUM
QuantumCircuit
from qiskit_aer import AerSimulator

print("🌌 CRIANDO |Φ⁻⟩...")
qc = # 🔮 CIRCUITO OTIMIZADO PARA IBM QUANTUM
QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.z(0)
qc.measure_all()

simulator = AerSimulator()
# 🌌 TRANSPILAÇÃO OTIMIZADA
circuito_otimizado = transpile(circuito, optimization_level=3)
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print(f"🎯 RESULTADOS: {counts}")

total = sum(counts.values())
corr = (counts.get('00', 0) + counts.get('11', 0)) / total * 100
print(f"🧪 CORRELAÇÃO: {corr:.2f}%")
