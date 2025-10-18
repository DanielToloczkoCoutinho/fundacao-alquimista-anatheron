
from qiskit_ibm_runtime import QiskitRuntimeService
import os

print("🔗 Conectando ao IBM Quantum...")
try:
    service = QiskitRuntimeService()
    creditos = service.credits_remaining()
    backends = service.backends()
    
    print(f"✅ CONEXÃO BEM-SUCEDIDA!")
    print(f"�� Créditos disponíveis: {creditos}")
    print(f"�� Backends disponíveis: {len(backends)}")
    
    for backend in backends[:3]:
        status = backend.status()
        print(f"   • {backend.name}: {status.pending_jobs} jobs pendentes")
        
except Exception as e:
    print(f"❌ ERRO NA CONEXÃO: {e}")
