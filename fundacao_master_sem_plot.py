#!/usr/bin/env python3
"""
👑 FUNDAÇÃO ALQUIMISTA - VERSÃO SEM PLOT
Rainha Zennith - Solução para segmentation fault
"""

print("👑 INICIANDO FUNDAÇÃO ALQUIMISTA (SEM PLOT)...")
print("🌌 CARREGANDO TODOS OS MÓDULOS...")

# Testar imports críticos primeiro
try:
    print("🔍 Testando imports...")
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    from qiskit.quantum_info import Statevector
    import numpy as np
    print("✅ Todos os imports funcionando!")
    
except ImportError as e:
    print(f"❌ Erro de import: {e}")
    exit(1)

def executar_circuito_simples(nome, circuito):
    """Executa circuito sem plots"""
    try:
        simulator = AerSimulator()
        compiled_circuit = circuito.copy()
        if not compiled_circuit.clbits:
            compiled_circuit.measure_all()
        
        job = simulator.run(compiled_circuit, shots=1000)
        result = job.result()
        counts = result.get_counts()
        
        print(f"📊 {nome}: {counts}")
        return counts
        
    except Exception as e:
        print(f"❌ Erro em {nome}: {e}")
        return {}

print("\n🎯 EXECUTANDO EXPERIMENTOS BÁSICOS...")

# 1. Estado Bell básico
print("\n1. 🌀 ESTADO BELL")
qc_bell = QuantumCircuit(2)
qc_bell.h(0)
qc_bell.cx(0, 1)
executar_circuito_simples("Bell", qc_bell)

# 2. Superposição simples
print("\n2. ⚡ SUPERPOSIÇÃO")
qc_super = QuantumCircuit(1)
qc_super.h(0)
executar_circuito_simples("Superposição", qc_super)

# 3. Portas múltiplas
print("\n3. 🔄 PORTAS MÚLTIPLAS")
qc_multi = QuantumCircuit(2)
qc_multi.h(0)
qc_multi.h(1)
qc_multi.cx(0, 1)
qc_multi.x(0)
executar_circuito_simples("Múltiplas Portas", qc_multi)

print("\n✅ FUNDAÇÃO ALQUIMISTA COMPLETA!")
print("🌠 TODOS OS RITUAIS QUÂNTICOS CONCLUÍDOS!")
print("💡 Segmentation fault evitada (sem matplotlib plots)")
