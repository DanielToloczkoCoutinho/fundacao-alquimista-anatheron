#!/usr/bin/env python3
"""
🧪 TESTE BASIC SIMULATOR - Rainha Zennith
Solução temporária enquanto corrigimos o Aer
"""

print("🧪 INICIANDO TESTE COM BASIC SIMULATOR...")

try:
    from qiskit import QuantumCircuit, transpile
    from qiskit.providers.basic_provider import BasicProvider
    from qiskit.visualization import plot_histogram
    import matplotlib.pyplot as plt
    
    print("✅ BasicProvider importado com sucesso!")
    
    # Criar circuito Bell simples
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    
    print("🔮 Circuito Bell criado:")
    print(qc)
    
    # Usar BasicProvider
    provider = BasicProvider()
    backend = provider.get_backend('basic_simulator')
    
    # Executar
    job = backend.run(transpile(qc, backend))
    result = job.result()
    counts = result.get_counts()
    
    print("📊 Resultados do circuito Bell:")
    print(counts)
    
    # Plot simples
    plt.bar(counts.keys(), counts.values())
    plt.title("Estado Bell - Basic Simulator")
    plt.xlabel("Estado")
    plt.ylabel("Contagens")
    plt.show()
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
except Exception as e:
    print(f"❌ Erro durante execução: {e}")
