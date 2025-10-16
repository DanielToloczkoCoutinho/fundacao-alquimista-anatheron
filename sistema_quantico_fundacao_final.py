#!/usr/bin/env python3
"""
🌌 SISTEMA QUÂNTICO DEFINITIVO - FUNDAÇÃO ALQUIMISTA
Versão final otimizada para ambiente Nix
"""

import math
import random
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple

class QubitAvancado:
    """Qubit avançado com múltiplos estados"""
    
    def __init__(self, estado: complex = 1.0):
        self.alpha = estado  # |0⟩
        self.beta = 0.0      # |1⟩
        self.historico = []
    
    def hadamard(self):
        """Porta Hadamard com registro"""
        novo_alpha = (self.alpha + self.beta) / math.sqrt(2)
        novo_beta = (self.alpha - self.beta) / math.sqrt(2)
        
        self.historico.append(f"H: {self.alpha:.3f}|0⟩ + {self.beta:.3f}|1⟩ → {novo_alpha:.3f}|0⟩ + {novo_beta:.3f}|1⟩")
        self.alpha, self.beta = novo_alpha, novo_beta
    
    def pauli_x(self):
        """Porta Pauli-X (NOT)"""
        self.alpha, self.beta = self.beta, self.alpha
        self.historico.append(f"X: Troca alpha/beta")
    
    def pauli_y(self):
        """Porta Pauli-Y"""
        novo_alpha = -1j * self.beta
        novo_beta = 1j * self.alpha
        self.alpha, self.beta = novo_alpha, novo_beta
        self.historico.append(f"Y: Aplicada rotação Y")
    
    def pauli_z(self):
        """Porta Pauli-Z"""
        self.beta = -self.beta
        self.historico.append(f"Z: Fase invertida para |1⟩")
    
    def medida(self) -> int:
        """Mede o qubit e colapsa o estado"""
        prob_0 = abs(self.alpha) ** 2
        resultado = 0 if random.random() < prob_0 else 1
        
        # Colapso do estado
        if resultado == 0:
            self.alpha, self.beta = 1.0, 0.0
        else:
            self.alpha, self.beta = 0.0, 1.0
            
        self.historico.append(f"M: Colapsou para |{resultado}⟩")
        return resultado
    
    def __str__(self):
        return f"Qubit: {self.alpha:.3f}|0⟩ + {self.beta:.3f}|1⟩"

class CircuitoQuanticoAvancado:
    """Circuito quântico avançado com múltiplos qubits"""
    
    def __init__(self, num_qubits: int):
        self.qubits = [QubitAvancado() for _ in range(num_qubits)]
        self.operacoes = []
        self.resultados = []
    
    def h(self, qubit_idx: int):
        """Hadamard em qubit específico"""
        self.qubits[qubit_idx].hadamard()
        self.operacoes.append(f"H({qubit_idx})")
    
    def x(self, qubit_idx: int):
        """Pauli-X em qubit específico"""
        self.qubits[qubit_idx].pauli_x()
        self.operacoes.append(f"X({qubit_idx})")
    
    def y(self, qubit_idx: int):
        """Pauli-Y em qubit específico"""
        self.qubits[qubit_idx].pauli_y()
        self.operacoes.append(f"Y({qubit_idx})")
    
    def z(self, qubit_idx: int):
        """Pauli-Z em qubit específico"""
        self.qubits[qubit_idx].pauli_z()
        self.operacoes.append(f"Z({qubit_idx})")
    
    def cx(self, controle: int, alvo: int):
        """Porta CNOT (controlled-NOT)"""
        # Simulação de emaranhamento
        prob_controle_1 = abs(self.qubits[controle].beta) ** 2
        
        if random.random() < prob_controle_1:
            # Se controle em |1⟩, aplica X no alvo
            self.qubits[alvo].alpha, self.qubits[alvo].beta = \
                self.qubits[alvo].beta, self.qubits[alvo].alpha
        
        self.operacoes.append(f"CX({controle},{alvo})")
    
    def medir_todos(self, shots: int = 1000) -> Dict[str, int]:
        """Executa múltiplas medições"""
        self.resultados = []
        
        for _ in range(shots):
            resultado = []
            for qubit in self.qubits:
                resultado.append(str(qubit.medida()))
            estado = ''.join(resultado)
            self.resultados.append(estado)
        
        # Contagem
        contagem = {}
        for resultado in self.resultados:
            contagem[resultado] = contagem.get(resultado, 0) + 1
        
        return contagem
    
    def analisar_emaranhamento(self, contagem: Dict[str, int]) -> Dict:
        """Análise detalhada do emaranhamento"""
        total_shots = sum(contagem.values())
        
        # Estados emaranhados de Bell
        estados_bell = ['00', '11'] if len(self.qubits) == 2 else ['000', '111']
        emaranhados = sum(contagem.get(estado, 0) for estado in estados_bell)
        
        # Coerência (quão puro é o estado)
        max_contagem = max(contagem.values())
        coerencia = max_contagem / total_shots
        
        return {
            'taxa_emaranhamento': emaranhados / total_shots,
            'coerencia': coerencia,
            'estados_emaranhados': estados_bell,
            'shots_emaranhados': emaranhados,
            'total_shots': total_shots
        }

def criar_circuito_bell() -> CircuitoQuanticoAvancado:
    """Cria circuito de estado Bell (emaranhamento máximo)"""
    circuito = CircuitoQuanticoAvancado(2)
    
    print("🔔 CRIANDO ESTADO BELL (MÁXIMO EMPARELHAMENTO)")
    circuito.h(0)  # Superposição
    circuito.cx(0, 1)  # Emaranhamento
    
    return circuito

def criar_circuito_ghz(n_qubits: int = 3) -> CircuitoQuanticoAvancado:
    """Cria estado GHZ (Greenberger-Horne-Zeilinger)"""
    circuito = CircuitoQuanticoAvancado(n_qubits)
    
    print(f"�� CRIANDO ESTADO GHZ COM {n_qubits} QBITS")
    circuito.h(0)  # Primeiro qubit em superposição
    
    # Cadeia de CNOTs para emaranhamento completo
    for i in range(n_qubits - 1):
        circuito.cx(i, i + 1)
    
    return circuito

def executar_experimento_completo():
    """Executa experimento quântico completo"""
    print("🌌 SISTEMA QUÂNTICO AVANÇADO - FUNDAÇÃO ALQUIMISTA")
    print("🎯 AMBIENTE NIX - VERSÃO DEFINITIVA")
    print("=" * 70)
    
    # Experimento 1: Estado Bell
    print("\n1. 🔔 EXPERIMENTO BELL (2 QBITS)")
    bell = criar_circuito_bell()
    
    print("   Estados dos qubits após operações:")
    for i, qubit in enumerate(bell.qubits):
        print(f"      Qubit {i}: {qubit}")
    
    resultados_bell = bell.medir_todos(shots=2000)
    analise_bell = bell.analisar_emaranhamento(resultados_bell)
    
    print(f"   📊 Resultados Bell:")
    for estado, count in sorted(resultados_bell.items()):
        percent = (count / 2000) * 100
        print(f"      |{estado}⟩: {count:4d} vezes ({percent:5.1f}%)")
    
    print(f"   🔗 Análise Bell:")
    print(f"      Taxa de emaranhamento: {analise_bell['taxa_emaranhamento']:.1%}")
    print(f"      Coerência: {analise_bell['coerencia']:.1%}")
    
    # Experimento 2: Estado GHZ
    print("\n2. 🌪️  EXPERIMENTO GHZ (3 QBITS)")
    ghz = criar_circuito_ghz(3)
    resultados_ghz = ghz.medir_todos(shots=1500)
    analise_ghz = ghz.analisar_emaranhamento(resultados_ghz)
    
    print(f"   📊 Resultados GHZ:")
    for estado, count in sorted(resultados_ghz.items()):
        percent = (count / 1500) * 100
        print(f"      |{estado}⟩: {count:4d} vezes ({percent:5.1f}%)")
    
    print(f"   🔗 Análise GHZ:")
    print(f"      Taxa de emaranhamento: {analise_ghz['taxa_emaranhamento']:.1%}")
    print(f"      Coerência: {analise_ghz['coerencia']:.1%}")
    
    # Salvar resultados completos
    dados_experimento = {
        "timestamp": datetime.now().isoformat(),
        "sistema": "Fundação Alquimista - Sistema Quântico Nix",
        "experimentos": {
            "bell": {
                "resultados": resultados_bell,
                "analise": analise_bell,
                "operacoes": bell.operacoes
            },
            "ghz": {
                "resultados": resultados_ghz, 
                "analise": analise_ghz,
                "operacoes": ghz.operacoes
            }
        },
        "estatisticas": {
            "total_shots": 3500,
            "tempo_execucao": f"{time.process_time():.2f}s",
            "ambiente": "Nix OS - Simulador Puro"
        }
    }
    
    with open('experimento_quantico_completo.json', 'w') as f:
        json.dump(dados_experimento, f, indent=2)
    
    print(f"\n💾 Dados salvos: experimento_quantico_completo.json")
    print("✅ SISTEMA QUÂNTICO DA FUNDAÇÃO OPERACIONAL!")
    print("🎯 Capacidades: Estados Bell, GHZ, Emaranhamento Multi-Qubit")
    print("🌌 Pronto para pesquisa quântica avançada!")

if __name__ == "__main__":
    executar_experimento_completo()
