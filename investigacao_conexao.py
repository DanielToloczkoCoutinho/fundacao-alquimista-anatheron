#!/usr/bin/env python3
"""
🔍 INVESTIGAÇÃO DA CONEXÃO IBM QUANTUM
🕵️‍♂️ Diagnóstico completo do problema
"""

import requests
import json
import os
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_provider import IBMProvider

print("🔍 INVESTIGAÇÃO DA CONEXÃO IBM QUANTUM")
print("=" * 50)

# TESTAR CONEXÃO COM INTERNET PRIMEIRO
print("1. 📡 TESTANDO CONEXÃO COM INTERNET...")
try:
    response = requests.get("https://quantum-computing.ibm.com", timeout=10)
    print("   ✅ Internet: OK")
    print(f"   🔗 Status: {response.status_code}")
except Exception as e:
    print(f"   ❌ Internet: FALHA - {e}")
    exit(1)

# VERIFICAR VARIÁVEIS DE AMBIENTE
print("\n2. 🔧 VERIFICANDO VARIÁVEIS DE AMBIENTE...")
qiskit_rc = os.path.expanduser("~/.qiskit/qiskit-rc")
if os.path.exists(qiskit_rc):
    print("   ✅ Arquivo qiskit-rc encontrado")
    with open(qiskit_rc, 'r') as f:
        print(f"   📄 Conteúdo: {f.read()}")
else:
    print("   ❌ Arquivo qiskit-rc NÃO encontrado")

# VERIFICAR CONFIGURAÇÃO SALVA
print("\n3. 📋 VERIFICANDO CONFIGURAÇÃO SALVA...")
try:
    service = QiskitRuntimeService()
    account = service._account
    print("   ✅ Configuração carregada")
    print(f"   🔑 Channel: {account.channel}")
    print(f"   🏢 Instance: {account.instance}")
    print(f"   🌐 URL: {account.url}")
except Exception as e:
    print(f"   ❌ Configuração: {e}")

# TESTAR DIRETAMENTE COM REQUESTS
print("\n4. 🌐 TESTANDO API DIRETAMENTE...")
CHAVES = [
    "ApiKey-c965c4fe-e0e9-4d5c-ba65-dd061b4093e1",
    "ApiKey-19033191-d209-4a47-b427-e2c094a3cdf0"
]

for i, chave in enumerate(CHAVES, 1):
    print(f"\n   🔑 Testando chave {i}: {chave[:10]}...")
    
    headers = {
        "Authorization": f"Bearer {chave}",
        "Content-Type": "application/json"
    }
    
    # Tentar diferentes endpoints
    endpoints = [
        "https://auth.quantum-computing.ibm.com/api/users/me",
        "https://api.quantum-computing.ibm.com/Network",
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint, headers=headers, timeout=10)
            print(f"      🌐 {endpoint}: Status {response.status_code}")
            if response.status_code == 200:
                print(f"      ✅ CHAVE VÁLIDA! Resposta: {len(response.text)} bytes")
                if "users/me" in endpoint:
                    user_data = response.json()
                    print(f"      👤 Usuário: {user_data.get('username', 'N/A')}")
                    print(f"      📧 Email: {user_data.get('email', 'N/A')}")
            elif response.status_code == 401:
                print(f"      ❌ CHAVE INVÁLIDA ou EXPIRADA")
            else:
                print(f"      ⚠️ Status inesperado: {response.status_code}")
        except Exception as e:
            print(f"      ❌ Erro: {e}")

# VERIFICAR VERSÕES DAS BIBLIOTECAS
print("\n5. 📦 VERIFICANDO VERSÕES...")
try:
    import qiskit_ibm_runtime
    import qiskit
    print(f"   ✅ Qiskit: {qiskit.__version__}")
    print(f"   ✅ Qiskit IBM Runtime: {qiskit_ibm_runtime.__version__}")
except Exception as e:
    print(f"   ❌ Erro versões: {e}")

print("\n🔍 DIAGNÓSTICO COMPLETO!")
print("💡 Possíveis causas:")
print("   - Chaves API expiradas ou revogadas")
print("   - Problema de autenticação no servidor IBM")
print("   - Versão incompatível da biblioteca")
print("   - Bloqueio de rede/firewall")
