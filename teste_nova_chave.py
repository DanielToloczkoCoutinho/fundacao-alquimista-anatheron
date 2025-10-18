#!/usr/bin/env python3
"""
🔑 TESTE DA NOVA CHAVE - FUNDAÇÃO ALQUIMISTA3
⚛️ Teste imediato da chave recém-criada
"""

from qiskit_ibm_runtime import QiskitRuntimeService
import requests
import json

print("🔑 TESTE DA NOVA CHAVE - FUNDAÇÃO ALQUIMISTA3")
print("=" * 50)

# SUA NOVA CHAVE - Cole o token completo aqui
NOVA_CHAVE = "URrlwXAer9lgleo7K3aANFUPyWbFL9HIUv8UZmdWXV3c"

print(f"🔑 Nova chave: {NOVA_CHAVE[:20]}...")

# PRIMEIRO: Testar a chave DIRETAMENTE na API
print("\n1. 🌐 TESTE DIRETO NA API IBM...")
headers = {
    "Authorization": f"Bearer {NOVA_CHAVE}",
    "Content-Type": "application/json"
}

try:
    response = requests.get(
        "https://auth.quantum-computing.ibm.com/api/users/me",
        headers=headers,
        timeout=10
    )
    
    print(f"   📡 Status: {response.status_code}")
    
    if response.status_code == 200:
        user_data = response.json()
        print("   ✅ CHAVE VÁLIDA!")
        print(f"   👤 Usuário: {user_data.get('username', 'N/A')}")
        print(f"   📧 Email: {user_data.get('email', 'N/A')}")
        print(f"   🆔 ID: {user_data.get('id', 'N/A')}")
        
        # AGORA configurar no Qiskit
        print("\n2. 🔧 CONFIGURANDO NO QISKIT...")
        try:
            QiskitRuntimeService.save_account(
                token=NOVA_CHAVE,
                overwrite=True
            )
            print("   ✅ Configuração salva!")
            
            # Testar serviço
            service = QiskitRuntimeService()
            print("   🔗 Serviço carregado!")
            
            # Listar backends
            backends = service.backends()
            print(f"   🌌 Backends disponíveis: {len(backends)}")
            
            print("\n3. 🔧 BACKENDS PRINCIPAIS:")
            for backend in backends[:5]:
                if hasattr(backend, 'num_qubits'):
                    status = backend.status()
                    print(f"   🖥️  {backend.name:20} | 🔢 {backend.num_qubits:3d} qubits | 📊 {status.pending_jobs:4d} jobs")
            
            print("\n🎉 NOVA CHAVE FUNCIONANDO PERFEITAMENTE!")
            print("🚀 FUNDAÇÃO ALQUIMISTA CONECTADA AO IBM QUANTUM!")
            
        except Exception as e:
            print(f"   ❌ Erro na configuração Qiskit: {e}")
            
    elif response.status_code == 401:
        print("   ❌ CHAVE INVÁLIDA ou NÃO AUTORIZADA")
        print("   💡 Verifique se copiou a chave COMPLETA")
    else:
        print(f"   ⚠️ Status inesperado: {response.status_code}")
        print(f"   📄 Resposta: {response.text[:200]}")

except Exception as e:
    print(f"   ❌ Erro de conexão: {e}")

# SALVAR A CHAVE PARA USO FUTURO
print(f"\n💾 SALVANDO CONFIGURAÇÃO...")
config = {
    "chave": NOVA_CHAVE,
    "nome": "Fundação Alquimista3", 
    "data_teste": "2025-10-17",
    "status": "TESTADA"
}

with open('chave_fundacao3.json', 'w') as f:
    json.dump(config, f, indent=2)

print("✅ Configuração salva em 'chave_fundacao3.json'")
