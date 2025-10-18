#!/usr/bin/env python3
from qiskit_ibm_runtime import QiskitRuntimeService
import sys

print("🌌 CONFIGURANDO IBM QUANTUM - FUNDAÇÃO ALQUIMISTA")
print("================================================")

try:
    # Salvar credencial (substitua pela sua chave se necessário)
    QiskitRuntimeService.save_account(
        channel='ibm_quantum',
        token='TY-O9m0EFYATZjd8Gu33rhnLSbWvv94wnBekzFtGsqb8',
        overwrite=True
    )
    print("✅ Chave IBM Quantum salva!")
    
    # Testar conexão
    service = QiskitRuntimeService()
    backends = service.backends()
    print(f"✅ Backends disponíveis: {len(backends)}")
    
    for backend in backends[:3]:  # Mostrar apenas os 3 primeiros
        status = backend.status()
        print(f"   🔧 {backend.name}: {status.pending_jobs} jobs pendentes")
    
    print("🚀 CONEXÃO IBM QUANTUM ESTABELECIDA!")
    
except Exception as e:
    print(f"❌ Erro na configuração: {e}")
    print("💡 Você pode obter uma chave gratuita em: https://quantum-computing.ibm.com/")
