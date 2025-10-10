#!/usr/bin/env python3
"""
👑 FUNDAÇÃO ALQUIMISTA - PLOTS SEGUROS
Rainha Zennith - Salva plots em arquivo
"""

import os
print("👑 INICIANDO FUNDAÇÃO ALQUIMISTA (PLOTS SEGUROS)...")

try:
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    from qiskit.visualization import plot_histogram
    import matplotlib
    matplotlib.use('Agg')  # Backend não-interativo
    import matplotlib.pyplot as plt
    import numpy as np
    
    print("✅ Ambiente carregado com backend seguro")
    
except ImportError as e:
    print(f"❌ Erro de import: {e}")
    exit(1)

def executar_e_plotar(nome, circuito, filename):
    """Executa e salva plot em arquivo"""
    try:
        simulator = AerSimulator()
        circuito_com_medidas = circuito.copy()
        if not circuito_com_medidas.clbits:
            circuito_com_medidas.measure_all()
        
        job = simulator.run(circuito_com_medidas, shots=1000)
        result = job.result()
        counts = result.get_counts()
        
        print(f"📊 {nome}: {counts}")
        
        # Criar e salvar plot
        fig = plot_histogram(counts)
        plt.title(f"Resultados: {nome}")
        plt.savefig(filename, dpi=100, bbox_inches='tight')
        plt.close()
        print(f"💾 Plot salvo: {filename}")
        
        return counts
        
    except Exception as e:
        print(f"❌ Erro em {nome}: {e}")
        return {}

# Criar diretório para plots
os.makedirs("plots_seguros", exist_ok=True)

print("\n🎯 EXECUTANDO EXPERIMENTOS COM PLOTS SEGUROS...")

# 1. Estado Bell
print("\n1. 🌀 ESTADO BELL")
qc_bell = QuantumCircuit(2)
qc_bell.h(0)
qc_bell.cx(0, 1)
executar_e_plotar("Estado Bell", qc_bell, "plots_seguros/bell_state.png")

# 2. Superposição
print("\n2. ⚡ SUPERPOSIÇÃO")
qc_super = QuantumCircuit(1)
qc_super.h(0)
executar_e_plotar("Superposição", qc_super, "plots_seguros/superposicao.png")

# 3. Entrelaçamento complexo
print("\n3. 🔗 ENTRELAÇAMENTO COMPLEXO")
qc_ent = QuantumCircuit(3)
qc_ent.h(0)
qc_ent.cx(0, 1)
qc_ent.cx(1, 2)
executar_e_plotar("Entrelaçamento 3-qubit", qc_ent, "plots_seguros/entrelacamento.png")

print("\n✅ FUNDAÇÃO ALQUIMISTA COMPLETA!")
print("📁 Plots salvos em: plots_seguros/")
print("🌌 Agora sem segmentation fault!")
