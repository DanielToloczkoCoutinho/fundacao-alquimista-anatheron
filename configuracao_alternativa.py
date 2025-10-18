#!/usr/bin/env python3
"""
🔄 CONFIGURAÇÃO ALTERNATIVA IBM QUANTUM
🔧 Tentando abordagem diferente
"""

import os
from qiskit_ibm_runtime import QiskitRuntimeService

print("🔄 CONFIGURAÇÃO ALTERNATIVA IBM QUANTUM")
print("=" * 40)

# LIMPAR CONFIGURAÇÕES EXISTENTES
print("1. 🧹 LIMPANDO CONFIGURAÇÕES EXISTENTES...")
config_files = [
    os.path.expanduser("~/.qiskit/qiskit-rc"),
    os.path.expanduser("~/.qiskit/qiskit-rc.yaml"),
    os.path.expanduser("~/.qiskit/qiskit-rc.json"),
]

for config_file in config_files:
    if os.path.exists(config_file):
        os.remove(config_file)
        print(f"   ✅ Removido: {config_file}")

# TENTAR CONFIGURAÇÃO SIMPLES
print("\n2. 🔧 CONFIGURAÇÃO SIMPLES...")
CHAVE = "ApiKey-19033191-d209-4a47-b427-e2c094a3cdf0"  # Chave mais nova

try:
    # Método mais simples - apenas token
    QiskitRuntimeService.save_account(
        token=CHAVE,
        overwrite=True
    )
    print("   ✅ Configuração simples salva")
    
    # Tentar carregar
    service = QiskitRuntimeService()
    print("   🔗 Serviço carregado")
    
    # Listar backends
    backends = service.backends()
    print(f"   🌌 Backends: {len(backends)} encontrados")
    
    for backend in backends[:3]:
        print(f"      🔧 {backend.name}")
        
except Exception as e:
    print(f"   ❌ Configuração simples falhou: {e}")

# TENTAR COM IBMProvider (abordagem alternativa)
print("\n3. 🔄 TENTANDO IBMProvider...")
try:
    from qiskit_ibm_provider import IBMProvider
    
    # Salvar conta no IBMProvider
    IBMProvider.save_account(
        token=CHAVE,
        overwrite=True
    )
    print("   ✅ IBMProvider configurado")
    
    # Carregar provider
    provider = IBMProvider()
    print("   🔗 Provider carregado")
    
    # Listar backends
    backends = provider.backends()
    print(f"   🌌 Backends IBMProvider: {len(backends)}")
    
    for backend in backends[:3]:
        status = backend.status()
        print(f"      🔧 {backend.name}: {status.pending_jobs} jobs")
        
except Exception as e:
    print(f"   ❌ IBMProvider falhou: {e}")

print("\n🔍 CONCLUSÃO DA INVESTIGAÇÃO:")
print("💡 As chaves podem estar:")
print("   - Expiradas (150 auths na chave antiga)")
print("   - Revogadas no portal IBM")
print("   - Com problemas de permissão")
print("🌌 Recomendação: Criar NOVA chave no portal IBM")
