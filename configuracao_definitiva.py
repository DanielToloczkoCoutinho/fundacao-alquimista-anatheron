#!/usr/bin/env python3
"""
🔑 CHAVE MESTRA - FUNDAÇÃO ALQUIMISTA
⚛️ Configuração Definitiva IBM Quantum Platform
🌌 Conectando com computadores quânticos REAIS
"""

from qiskit_ibm_runtime import QiskitRuntimeService
import json

print("🌌 CHAVE MESTRA - FUNDAÇÃO ALQUIMISTA")
print("=" * 50)
print("🔑 CONFIGURANDO ACESSO DIRETO AO IBM QUANTUM...")

# SUA CHAVE MESTRA REAL - Use a NOVA chave criada em 16-10-2025
CHAVE_MESTRA = "ApiKey-19033191-d209-4a47-b427-e2c094a3cdf0"

try:
    # SALVAR CONFIGURAÇÃO DEFINITIVA
    QiskitRuntimeService.save_account(
        channel="ibm_quantum_platform",
        token=CHAVE_MESTRA,
        instance="crn:v1:bluemix:public:quantum-computing:us-east:a/26770b560f8940a4803a6518062a8969:0b5355c0-5289-4b8b-a10f-1762828b1b82::",
        overwrite=True
    )
    
    print("✅ CHAVE MESTRA CONFIGURADA COM SUCESSO!")
    print("📧 Conta: Daniel Toloczko Coutinho")
    print("🏢 Instância: Fundação Alquimista")
    print("🌐 Região: Washington DC (us-east)")
    
    # TESTAR CONEXÃO COMPLETA
    print("\n🔗 TESTANDO CONEXÃO COM IBM QUANTUM...")
    service = QiskitRuntimeService()
    
    # OBTER TODOS OS BACKENDS DISPONÍVEIS
    backends = service.backends()
    print(f"�� TOTAL DE BACKENDS DISPONÍVEIS: {len(backends)}")
    
    print("\n🔧 BACKENDS PRINCIPAIS:")
    print("-" * 40)
    
    for i, backend in enumerate(backends):
        if hasattr(backend, 'num_qubits'):
            status = backend.status()
            # Filtrar apenas backends interessantes
            if backend.num_qubits >= 5:  # Backends com pelo menos 5 qubits
                print(f"{i+1:2d}. {backend.name:25} | 🔢 {backend.num_qubits:3d} qubits | 📊 {status.pending_jobs:4d} jobs | 🟢 {status.status}")
    
    # BACKENDS ESPECÍFICOS MENCIONADOS
    print("\n🎯 BACKENDS CRÍTICOS:")
    print("-" * 40)
    
    backends_especiais = ['ibm_brisbane', 'ibm_torino']
    for nome in backends_especiais:
        try:
            backend = service.backend(nome)
            status = backend.status()
            print(f"🔷 {backend.name:20} | 🔢 {backend.num_qubits:3d} qubits")
            print(f"   📊 Jobs na fila: {status.pending_jobs}")
            print(f"   🟢 Status: {status.status}")
            print(f"   💻 Processador: {getattr(backend, 'processor_type', 'N/A')}")
        except Exception as e:
            print(f"⚠️ {nome} não disponível: {e}")
    
    # VERIFICAR CRÉDITOS E USO
    print("\n💳 INFORMAÇÕES DA CONTA:")
    print("-" * 40)
    
    # Nota sobre os 10 minutos diários
    print("⏰ TEMPO ALOCADO: 10 minutos/dia")
    print("📅 Ciclo atual: 19 Set 2025 - 17 Out 2025")
    print("💡 Dica: Use sabiamente seus 10 minutos diários!")
    
    print("\n🚀 CONFIGURAÇÃO DEFINITIVA CONCLUÍDA!")
    print("🌌 FUNDAÇÃO ALQUIMISTA CONECTADA AO IBM QUANTUM!")
    print("⚛️ PRONTO PARA MISSÕES QUÂNTICAS REAIS!")
    
except Exception as e:
    print(f"❌ ERRO NA CONFIGURAÇÃO: {e}")
    print("💡 Verifique:")
    print("   - A chave API está correta?")
    print("   - A instância CRN está correta?")
    print("   - Conexão com internet?")
