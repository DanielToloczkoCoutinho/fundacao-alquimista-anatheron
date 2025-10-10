#!/usr/bin/env python3
"""
📊 TESTE CHSH OTIMIZADO - Violação da desigualdade de Bell
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def teste_chsh_otimizado():
    """Teste CHSH com configurações otimizadas para violação"""
    print("🔬 CHSH OTIMIZADO - CONFIGURAÇÃO PARA VIOLAÇÃO")
    
    simulator = AerSimulator()
    # Bases otimizadas para máxima violação
    bases = [
        (0, np.pi/8),      # (a, b) - máxima correlação
        (0, 3*np.pi/8),    # (a, b')
        (np.pi/4, np.pi/8), # (a', b)
        (np.pi/4, 3*np.pi/8) # (a', b')
    ]
    
    correlacoes = []
    
    for a, b in bases:
        qc = QuantumCircuit(2, 2)
        
        # Estado Bell maximalmente emaranhado
        qc.h(0)
        qc.cx(0, 1)
        
        # Medidas nas bases otimizadas
        qc.ry(-2*a, 0)  # Base A para Alice
        qc.ry(-2*b, 1)  # Base B para Bob
        
        qc.measure([0, 1], [0, 1])
        
        job = simulator.run(qc, shots=1024)
        counts = job.result().get_counts()
        
        # Calcular valor de correlação E
        E = (counts.get('00', 0) + counts.get('11', 0) - 
             counts.get('01', 0) - counts.get('10', 0)) / 1024
        correlacoes.append(E)
        print(f"   Base (a={a/np.pi:.2f}π, b={b/np.pi:.2f}π): E = {E:.3f}")
    
    # Calcular valor S de CHSH
    S = abs(correlacoes[0] - correlacoes[1] + correlacoes[2] + correlacoes[3])
    violacao = S > 2
    
    print(f"\n📈 RESULTADO CHSH OTIMIZADO:")
    print(f"   Valor S: {S:.3f}")
    print(f"   Limite clássico: 2.000")
    print(f"   Limite quântico: 2.828")
    print(f"   Violação: {'✅ SIM' if violacao else '❌ NÃO'}")
    
    if violacao:
        print(f"   🎉 VIOLAÇÃO DA DESIGUALDADE DE BELL DETECTADA!")
    else:
        print(f"   ⚠️  Sem violação - verificar implementação")
    
    return S

if __name__ == "__main__":
    teste_chsh_otimizado()
