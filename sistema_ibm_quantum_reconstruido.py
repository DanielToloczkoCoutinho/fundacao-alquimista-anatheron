#!/usr/bin/env python3
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
import sys

print("🌌 SISTEMA QUÂNTICO RECONSTRUÍDO - FUNDAÇÃO ALQUIMISTA")
print("================================================")

try:
    # Configurar serviço
    service = QiskitRuntimeService(channel='ibm_quantum')
    backend = service.least_busy(operational=True, simulator=False)
    print(f"✅ Backend selecionado: {backend.name}")

    # Criar circuito Bell
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    print("✅ Circuito Bell criado")

    # Executar no IBM Quantum
    sampler = Sampler(backend=backend)
    job = sampler.run(qc, shots=1000)
    result = job.result()
    counts = result.quasi_dists[0].binary_probabilities()
    print(f"🎉 Resultados do IBM Quantum: {counts}")
except Exception as e:
    print(f"❌ Erro ao executar no IBM Quantum: {e}")
    sys.exit(1)
