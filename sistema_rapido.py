#!/usr/bin/env python3
"""
⚡ SISTEMA RÁPIDO - FUNDAÇÃO ALQUIMISTA
Rainha Zennith - Controle Instantâneo
"""

print("⚡ SISTEMA RÁPIDO ATIVADO")
print("========================")

# Verificar imports críticos
try:
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    print("✅ Imports: OK")
    
    # Teste rápido
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    
    simulator = AerSimulator()
    job = simulator.run(qc, shots=100)
    result = job.result()
    counts = result.get_counts()
    
    print(f"🌀 Teste Bell: {counts}")
    print("🎯 SISTEMA 100% OPERACIONAL!")
    
except Exception as e:
    print(f"❌ Erro: {e}")

print("💡 Comandos disponíveis:")
print("   python experimentos_avancados_corrigidos.py")
print("   python dashboard_corrigido.py")
