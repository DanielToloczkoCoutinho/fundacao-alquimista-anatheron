
#!/usr/bin/env python3
"""
🌌 CIRCUITOS QUÂNTICOS UNIFICADOS - FUNDAÇÃO ALQUIMISTA
⚛️ Versão otimizada e desaglomerada
🎯 Execução sequencial eficiente
"""

print("🌌 INICIANDO CIRCUITOS QUÂNTICOS UNIFICADOS...")
print("=" * 50)

# Importações otimizadas
try:
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator
    from qiskit.visualization import plot_histogram
    import matplotlib.pyplot as plt
    print("✅ QISKIT IMPORTADO COM SUCESSO")
except ImportError as e:
    print(f"❌ ERRO NAS IMPORTAÇÕES: {e}")
    exit(1)

def executar_circuito_simples(nome, circuito, shots=1024):
    """Executar circuito de forma otimizada"""
    print(f"\n🔧 EXECUTANDO: {nome}")
    
    try:
        # Simulador otimizado
        simulador = AerSimulator()
        
        # Compilar circuito
        circuito_compilado = transpile(circuito, simulador)
        
        # Executar
        job = simulador.run(circuito_compilado, shots=shots)
        resultado = job.result()
        counts = resultado.get_counts()
        
        print(f"   📊 RESULTADOS: {counts}")
        return counts
        
    except Exception as e:
        print(f"   ❌ ERRO: {e}")
        return None

print("\n🚀 CRIANDO CIRCUITOS BÁSICOS...")

# 1. Circuito |Ψ⁺⟩
print("\n1. 🌌 CIRCUITO |Ψ⁺⟩ (Psi Plus)")
qc_psi_plus = QuantumCircuit(2)
qc_psi_plus.h(0)
qc_psi_plus.cx(0, 1)
qc_psi_plus.measure_all()
result_psi_plus = executar_circuito_simples("|Ψ⁺⟩", qc_psi_plus)

# 2. Circuito |Φ⁻⟩  
print("\n2. 🌌 CIRCUITO |Φ⁻⟩ (Phi Minus)")
qc_phi_minus = QuantumCircuit(2)
qc_phi_minus.h(0)
qc_phi_minus.cx(0, 1)
qc_phi_minus.z(1)
qc_phi_minus.measure_all()
result_phi_minus = executar_circuito_simples("|Φ⁻⟩", qc_phi_minus)

# 3. Teletransporte Quântico (Simplificado)
print("\n3. 🚀 TELETRANSPORTE QUÂNTICO (Simplificado)")
qc_teleport = QuantumCircuit(3, 3)
qc_teleport.h(1)
qc_teleport.cx(1, 2)
qc_teleport.cx(0, 1)
qc_teleport.h(0)
qc_teleport.measure([0, 1], [0, 1])
qc_teleport.cx(1, 2)
qc_teleport.cz(0, 2)
qc_teleport.measure(2, 2)
result_teleport = executar_circuito_simples("Teletransporte", qc_teleport)

print("\n" + "="*50)
print("🎉 CIRCUITOS UNIFICADOS EXECUTADOS COM SUCESSO!")
print("📊 RESUMO:")
print(f"   • |Ψ⁺⟩: {result_psi_plus}")
print(f"   • |Φ⁻⟩: {result_phi_minus}") 
print(f"   • Teletransporte: {result_teleport}")
print("🌌 EXECUÇÃO CONCLUÍDA!")
