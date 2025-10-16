#!/bin/bash
echo "🔍 REDUNDÂNCIAS NIX E QUANTUM"
echo "============================="

# VERIFICAR DUPLICATAS ENTRE QUANTUM_VENV E FUNDAÇÃO
echo "🔄 COMPARAÇÃO QUANTUM_VENV vs FUNDAÇÃO:"
echo "   Quantum Venv: $(find /home/user/quantum_venv -name "*.py" | wc -l) arquivos Python"
echo "   Fundação: $(find . -name "*.py" | wc -l) arquivos Python"

# VERIFICAR SE QUANTUM_VENV É NECESSÁRIO
echo ""
echo "🤔 QUANTUM_VENV É ESSENCIAL?"
find /home/user/quantum_venv -name "qiskit*" | head -5
find . -name "qiskit*" | head -5

# VERIFICAR CONFIGURAÇÕES DUPLICADAS
echo ""
echo "⚙️ CONFIGURAÇÕES DUPLICADAS:"
find /home/user -name "*.nix" -type f | head -10
