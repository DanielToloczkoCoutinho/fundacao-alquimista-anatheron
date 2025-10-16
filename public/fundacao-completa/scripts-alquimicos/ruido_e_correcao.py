# 🛡️ SIMULAÇÃO DE RUÍDO E CORREÇÃO
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

print("🛡️ INICIANDO SIMULAÇÃO DE RUÍDO...")

# Circuito simples
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Executar sem ruído
simulator = AerSimulator()
result_clean = simulator.run(qc, shots=1024).result()
counts_clean = result_clean.get_counts()

print(f"🎯 SEM RUÍDO: {counts_clean}")

# Criar modelo de ruído
noise_model = NoiseModel()
error = depolarizing_error(0.1, 1)  # 10% de erro
noise_model.add_all_qubit_quantum_error(error, ['h'])

# Executar com ruído
simulator_noise = AerSimulator(noise_model=noise_model)
result_noise = simulator_noise.run(qc, shots=1024).result()
counts_noise = result_noise.get_counts()

print(f"🌪️ COM RUÍDO: {counts_noise}")

# Circuito com correção simples
qc_corrected = QuantumCircuit(3, 1)
qc_corrected.h(0)
# Encoding simples
qc_corrected.cx(0, 1)
qc_corrected.cx(0, 2)
qc_corrected.measure(2, 0)  # Medir só um para exemplo

result_corrected = simulator_noise.run(qc_corrected, shots=1024).result()
counts_corrected = result_corrected.get_counts()

print(f"🛡️ COM CORREÇÃO: {counts_corrected}")
print("✅ ANÁLISE DE RUÍDO CONCLUÍDA!")
