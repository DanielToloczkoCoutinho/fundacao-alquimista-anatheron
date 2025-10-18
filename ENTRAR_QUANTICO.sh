#!/bin/bash
# 🔑 CHAVE DE ACESSO DIRETO - AMBIENTE QUÂNTICO
# ⚛️ Entra DIRETAMENTE no (fundacao_venv) com Python ativo

echo "🔑 ACESSO DIRETO - AMBIENTE QUÂNTICO"
echo "==================================="

# Entrar no diretório da Fundação
cd ~/fundacao-alquimista-anatheron

# Ativar ambiente virtual E entrar no Python QUÂNTICO automaticamente
source /tmp/fundacao_venv/bin/activate && python3 << 'QUANTICO_DIRETO'

print("�� AMBIENTE QUÂNTICO - FUNDAÇÃO ALQUIMISTA")
print("=" * 50)
print("🎯 ACESSO DIRETO CONCEDIDO!")
print("⚛️  Você está DENTRO do ambiente quântico")
print("")

# Verificar sistema
from qiskit import QuantumCircuit, __version__ as qiskit_ver
from qiskit_aer import AerSimulator
import numpy as np
import sys

print(f"🐍 Python: {sys.version.split()[0]}")
print(f"⚛️  Qiskit: {qiskit_ver}")
print(f"📁 Diretório: {sys.path[0]}")
print("")

# Executar circuito quântico automático
print("🚀 EXECUTANDO CIRCUITO QUÂNTICO AUTOMÁTICO...")
qc = QuantumCircuit(3, name="Acesso_Direto")
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure_all()

backend = AerSimulator()
result = backend.run(qc, shots=100).result()
counts = result.get_counts()

print(f"📊 Resultado: {counts}")
print("")

# Mensagem de boas-vindas
print("🎉 AMBIENTE QUÂNTICO ATIVO!")
print("💫 Comandos disponíveis imediatamente:")
print("   - QuantumCircuit()  # Criar circuitos")
print("   - AerSimulator()   # Executar simulações") 
print("   - Digite 'exit()' para sair")
print("")

# Manter no Python interativo
print("🔧 Use Ctrl+D ou 'exit()' para sair do ambiente quântico")
QUANTICO_DIRETO
