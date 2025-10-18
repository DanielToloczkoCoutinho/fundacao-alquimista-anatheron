#!/usr/bin/env python3
"""
🌌 MISSÃO FUNDAÇÃO - VERSÃO CORRIGIDA
⚛️ Circuito funcionando corretamente
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print("🌌 MISSÃO FUNDAÇÃO ALQUIMISTA - VERSÃO CORRIGIDA")
print("=" * 50)

def criar_portal_alquimico():
    """Cria o portal quântico da Fundação - VERSÃO CORRIGIDA"""
    qc = QuantumCircuit(3, 3, name="Portal_Fundacao")
    
    # Portal de entrada
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(1, 2)
    
    # Transformações alquímicas
    qc.ry(np.pi/4, 0)
    qc.rz(np.pi/3, 1) 
    qc.rx(np.pi/6, 2)
    
    # Medição CORRIGIDA - especificar registros
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

# EXECUÇÃO PRINCIPAL
print("�� INICIANDO MISSÃO CORRIGIDA...")

# 1. Criar circuito CORRETO
circuito = criar_portal_alquimico()
print("✅ Portal Alquímico criado (CORRETO)")

# DESENHO CORRETO - sem parâmetro 'text'
print("📋 DIAGRAMA DO CIRCUITO:")
print(circuito.draw())

# 2. Executar simulação
print("\n🔧 EXECUTANDO SIMULAÇÃO...")
backend_sim = AerSimulator()
resultado = backend_sim.run(circuito, shots=1000).result()
counts = resultado.get_counts()

print(f"📊 RESULTADOS: {counts}")

# 3. Análise dos resultados
print("\n�� ANÁLISE DOS RESULTADOS:")
total_shots = sum(counts.values())
for estado, contagem in sorted(counts.items()):
    porcentagem = (contagem / total_shots) * 100
    print(f"   {estado}: {contagem} shots ({porcentagem:.1f}%)")

print("\n🎉 MISSÃO FUNDAÇÃO CONCLUÍDA COM SUCESSO!")
print("🌌 SISTEMA OPERACIONAL COM SIMULADOR LOCAL!")
print("💡 IBM Quantum será configurado posteriormente")
