#!/usr/bin/env python3
from qiskit_ibm_runtime import QiskitRuntimeService
import sys

print("🌌 CONFIGURANDO IBM QUANTUM - FUNDAÇÃO ALQUIMISTA")
print("================================================")

try:
    QiskitRuntimeService.save_account(
        channel='ibm_quantum',
        token='TY-O9m0EFYATZjd8Gu33rhnLSbWvv94wnBekzFtGsqb8',
        overwrite=True
    )
    print("✅ Chave IBM Quantum salva!")
    service = QiskitRuntimeService()
    backends = service.backends()
    print("✅ Backends disponíveis:", [b.name for b in backends])
except Exception as e:
    print(f"❌ Erro ao configurar IBM Quantum: {e}")
    sys.exit(1)
