#!/usr/bin/env python3
"""
🔬 SISTEMA DE PESQUISA AUTÔNOMA CORRIGIDO
"""

import random
import time
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

class PesquisadorQuanticoAutonomo:
    def __init__(self):
        self.simulator = AerSimulator()
        self.ciclo = 0
        
    def superposicao_multipla(self):
        """Cria superposições com múltiplos qubits"""
        n = random.randint(2, 4)
        qc = QuantumCircuit(n, n)
        
        for i in range(n):
            qc.h(i)
            
        qc.measure(range(n), range(n))
        return qc
    
    def emaranhamento_bell_avancado(self):
        """Cria estados Bell em diferentes configurações"""
        qc = QuantumCircuit(2, 2)
        
        # Escolhe tipo de estado Bell aleatoriamente
        tipo = random.choice(['phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'])
        
        qc.h(0)
        qc.cx(0, 1)
        
        if tipo == 'phi_minus':
            qc.z(0)
        elif tipo == 'psi_plus':
            qc.x(1)
        elif tipo == 'psi_minus':
            qc.z(0)
            qc.x(1)
            
        qc.measure([0, 1], [0, 1])
        return qc
    
    def teste_chsh_otimizado(self):
        """Teste CHSH com configurações otimizadas"""
        bases = [
            (0, np.pi/8),
            (0, 3*np.pi/8),
            (np.pi/4, np.pi/8),
            (np.pi/4, 3*np.pi/8)
        ]
        
        correlacoes = []
        
        for a, b in bases:
            qc = QuantumCircuit(2, 2)
            qc.h(0)
            qc.cx(0, 1)
            qc.ry(-2*a, 0)
            qc.ry(-2*b, 1)
            qc.measure([0, 1], [0, 1])
            
            job = self.simulator.run(qc, shots=1024)
            counts = job.result().get_counts()
            
            E = (counts.get('00', 0) + counts.get('11', 0) - 
                 counts.get('01', 0) - counts.get('10', 0)) / 1024
            correlacoes.append(E)
        
        S = abs(correlacoes[0] - correlacoes[1] + correlacoes[2] + correlacoes[3])
        return S
    
    def algoritmo_grover_adaptativo(self):
        """Algoritmo de Grover com alvo aleatório"""
        n = 2  # 2 qubits para simplicidade
        alvo = random.randint(0, 3)  # |00⟩, |01⟩, |10⟩, |11⟩
        alvo_bin = format(alvo, f'0{n}b')
        
        qc = QuantumCircuit(n, n)
        
        # Superposição inicial
        for i in range(n):
            qc.h(i)
        
        # Oracle para o estado alvo
        for i in range(n):
            if alvo_bin[i] == '0':
                qc.x(i)
        
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
        
        for i in range(n):
            if alvo_bin[i] == '0':
                qc.x(i)
        
        # Difusão de Grover
        for i in range(n):
            qc.h(i)
            qc.x(i)
        
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
        
        for i in range(n):
            qc.x(i)
            qc.h(i)
        
        qc.measure(range(n), range(n))
        return qc, alvo_bin
    
    def experimento_aleatorio(self):
        """Seleciona experimento aleatório"""
        experimentos = [
            self.superposicao_multipla,
            self.emaranhamento_bell_avancado,
            self.algoritmo_grover_adaptativo
        ]
        
        return random.choice(experimentos)
    
    def executar_ciclo(self):
        """Executa um ciclo completo de pesquisa"""
        self.ciclo += 1
        print(f"\n🔄 CICLO {self.ciclo}")
        print("="*30)
        
        # Executa experimento aleatório
        exp = self.experimento_aleatorio()
        
        if exp == self.teste_chsh_otimizado:
            S = exp()
            print(f"📊 Teste CHSH: S = {S:.3f}")
            if S > 2.0:
                print("🎉 VIOLAÇÃO DETECTADA!")
            else:
                print("⚡ Resultado clássico")
                
        elif exp == self.algoritmo_grover_adaptativo:
            qc, alvo = exp()
            job = self.simulator.run(qc, shots=1024)
            counts = job.result().get_counts()
            print(f"🔍 Grover - Alvo: |{alvo}⟩")
            print(f"📊 Resultados: {counts}")
            
        else:
            qc = exp()
            job = self.simulator.run(qc, shots=1024)
            counts = job.result().get_counts()
            print(f"🧪 Experimento: {exp.__name__}")
            print(f"📊 Resultados: {counts}")
    
    def iniciar_pesquisa_continua(self, intervalo_minutos=2):
        """Inicia pesquisa contínua automática"""
        print("🚀 INICIANDO PESQUISA AUTÔNOMA CONTÍNUA")
        print(f"⏰ Intervalo: {intervalo_minutos} minutos")
        print("="*50)
        
        try:
            while True:
                self.executar_ciclo()
                print(f"\n💤 Aguardando {intervalo_minutos} minutos...")
                time.sleep(intervalo_minutos * 60)
                
        except KeyboardInterrupt:
            print(f"\n⏹️  Pesquisa interrompida após {self.ciclo} ciclos")

# Execução principal
if __name__ == "__main__":
    pesquisador = PesquisadorQuanticoAutonomo()
    pesquisador.iniciar_pesquisa_continua(intervalo_minutos=2)
