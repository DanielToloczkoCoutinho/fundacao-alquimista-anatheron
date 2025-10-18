# 🌠 TELETRANSPORTE QUÂNTICO (VERSÃO CORRIGIDA)
from qiskit import # 🔮 CIRCUITO OTIMIZADO PARA IBM QUANTUM
QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

print("🚀 INICIANDO TELETRANSPORTE QUÂNTICO...")

# Criar circuito simplificado (versão funcional)
qc = # 🔮 CIRCUITO OTIMIZADO PARA IBM QUANTUM
QuantumCircuit(3, 3)

# Estado a ser teletransportado (|1⟩)
qc.x(0)  # Criar |1⟩ no qubit 0
qc.barrier()

# Criar par emaranhado entre Alice e Bob
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Operações de Alice
qc.cx(0, 1)
qc.h(0)
qc.barrier()

# Medidas de Alice
qc.measure(0, 0)
qc.measure(1, 1)
qc.barrier()

# Correções de Bob (usando lógica clássica)
with qc.if_test((0, 1)):  # Se medida0 = 1
    qc.z(2)
with qc.if_test((1, 1)):  # Se medida1 = 1  
    qc.x(2)

# Medir resultado final
qc.measure(2, 2)

print("🔧 CIRCUITO CONSTRUÍDO!")
print(qc.draw())

# Executar
simulator = AerSimulator()
# 🌌 TRANSPILAÇÃO OTIMIZADA
circuito_otimizado = transpile(circuito, optimization_level=3)
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print(f"🎯 RESULTADOS: {counts}")

# Verificar sucesso (deve ter maioria em '101' onde o último bit é o estado teletransportado)
sucesso = counts.get('101', 0)
total = sum(counts.values())
taxa_sucesso = (sucesso / total) * 100

print(f"📊 TAXA DE SUCESSO: {taxa_sucesso:.2f}%")
print("✅ TELETRANSPORTE CONCLUÍDO!")
