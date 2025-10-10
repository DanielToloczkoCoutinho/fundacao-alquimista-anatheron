#!/usr/bin/env python3
"""
🧪 TESTE AER SIMULATOR CORRIGIDO - Rainha Zennith
"""

print("🧪 TESTANDO AER SIMULATOR COM LIBRARIAS C++...")

try:
    # Testar import do Aer
    from qiskit_aer import AerSimulator
    print("✅ AerSimulator importado com sucesso!")
    
    from qiskit import QuantumCircuit, transpile
    from qiskit.visualization import plot_histogram
    import matplotlib.pyplot as plt
    
    # Criar circuito
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    
    print("🔮 Circuito criado:")
    print(qc)
    
    # Usar Aer Simulator
    simulator = AerSimulator()
    
    # Compilar e executar
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    print("📊 Resultados AerSimulator:")
    print(counts)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plot_histogram(counts)
    plt.title("Estado Bell - AerSimulator Corrigido")
    plt.show()
    
    print("🎉 AER SIMULATOR FUNCIONANDO PERFEITAMENTE!")
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("💡 Tentando diagnóstico das bibliotecas...")
    import subprocess
    result = subprocess.run(['ldd', '/home/user/studio/quantum_venv/lib/python3.11/site-packages/qiskit_aer/backends/controller_wrappers.cpython-311-x86_64-linux-gnu.so'], 
                          capture_output=True, text=True)
    print("Diagnóstico ldd:")
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
        
except Exception as e:
    print(f"❌ Erro durante execução: {e}")
