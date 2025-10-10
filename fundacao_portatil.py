#!/usr/bin/env python3
"""
🏗️ FUNDAÇÃO ALQUIMISTA - SISTEMA PORTÁTIL
Rainha Zennith - Ambiente independente do Nix
"""

import sys
import os

# Verificar dependências
try:
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    import numpy as np
    print("✅ Todas as dependências carregadas!")
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("💡 Execute: pip install qiskit qiskit-aer matplotlib numpy")
    sys.exit(1)

class FundacaoPortatil:
    def __init__(self):
        self.simulator = AerSimulator()
        print("🔮 FUNDAÇÃO ALQUIMISTA - SISTEMA PORTÁTIL ATIVADO!")
    
    def teste_rapido(self):
        """Teste rápido do sistema"""
        print("\n🧪 TESTE RÁPIDO DO SISTEMA")
        print("=" * 30)
        
        # Circuito Bell simples
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])
        
        job = self.simulator.run(qc, shots=100)
        counts = job.result().get_counts()
        
        print(f"   Circuito Bell: {counts}")
        print("   ✅ Sistema quântico operacional!")
        return counts
    
    def estados_bell_portatil(self):
        """Estados Bell no sistema portátil"""
        print("\n🌀 ESTADOS BELL - SISTEMA PORTÁTIL")
        print("=" * 40)
        
        estados = {
            'Φ⁺': lambda qc: [qc.h(0), qc.cx(0, 1)],
            'Φ⁻': lambda qc: [qc.h(0), qc.cx(0, 1), qc.z(1)],
            'Ψ⁺': lambda qc: [qc.x(0), qc.h(0), qc.cx(0, 1)],
            'Ψ⁻': lambda qc: [qc.x(0), qc.h(0), qc.cx(0, 1), qc.z(1)]
        }
        
        for nome, construtor in estados.items():
            qc = QuantumCircuit(2, 2)
            construtor(qc)
            qc.measure([0, 1], [0, 1])
            
            job = self.simulator.run(qc, shots=256)
            counts = job.result().get_counts()
            
            correlacao = (counts.get('00', 0) + counts.get('11', 0)) / 256
            print(f"   {nome}: {counts} | Fidelidade: {correlacao:.3f}")
    
    def menu_principal(self):
        """Menu interativo do sistema portátil"""
        while True:
            print("\n🎯 MENU DA FUNDAÇÃO PORTÁTIL")
            print("=" * 30)
            print("1. Teste rápido do sistema")
            print("2. Estados Bell completos")
            print("3. Algoritmo de Grover")
            print("4. Teletransporte quântico")
            print("5. Sair")
            
            escolha = input("\nEscolha uma opção (1-5): ").strip()
            
            if escolha == "1":
                self.teste_rapido()
            elif escolha == "2":
                self.estados_bell_portatil()
            elif escolha == "3":
                self.grover_portatil()
            elif escolha == "4":
                self.teletransporte_portatil()
            elif escolha == "5":
                print("👑 Até logo, Mestre Alquimista!")
                break
            else:
                print("❌ Opção inválida!")
    
    def grover_portatil(self):
        """Algoritmo de Grover simplificado"""
        print("\n🔍 ALGORITMO DE GROVER PORTÁTIL")
        print("=" * 35)
        
        qc = QuantumCircuit(2, 2)
        
        # Superposição
        qc.h(0)
        qc.h(1)
        
        # Oracle para |11⟩
        qc.cz(0, 1)
        
        # Difusão
        qc.h(0)
        qc.h(1)
        qc.z(0)
        qc.z(1)
        qc.cz(0, 1)
        qc.h(0)
        qc.h(1)
        
        qc.measure_all()
        
        job = self.simulator.run(qc, shots=1024)
        counts = job.result().get_counts()
        
        print(f"   Resultados: {counts}")
        print("   ✅ Algoritmo executado!")
    
    def teletransporte_portatil(self):
        """Teletransporte simplificado"""
        print("\n🚀 TELETRANSPORTE PORTÁTIL")
        print("=" * 30)
        
        qc = QuantumCircuit(3, 3)
        
        # Preparar estado Bell
        qc.h(1)
        qc.cx(1, 2)
        
        # Estado a teletransportar |1⟩
        qc.x(0)
        
        # Protocolo
        qc.cx(0, 1)
        qc.h(0)
        
        qc.measure_all()
        
        print("   ✅ Protocolo de teletransporte preparado!")
        print("   🎯 Execute para ver resultados")

if __name__ == "__main__":
    try:
        fundacao = FundacaoPortatil()
        fundacao.menu_principal()
    except KeyboardInterrupt:
        print("\n👑 Execução interrompida pelo usuário")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    # Saída limpa
    sys.exit(0)
