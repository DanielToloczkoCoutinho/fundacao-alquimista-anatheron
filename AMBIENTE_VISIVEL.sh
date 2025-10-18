#!/bin/bash
# 👁️ AMBIENTE VISÍVEL - MOSTRA QUE ESTÁ NO (fundacao_venv)
# 🎯 Entra no ambiente E mostra visualmente que está nele

cd ~/fundacao-alquimista-anatheron

# Ativar ambiente
source /tmp/fundacao_venv/bin/activate

# Configurar PS1 para mostrar o ambiente VISUALMENTE
export PS1="(fundacao_venv) \[\033[1;32m\]\u@\h\[\033[0m\]:\[\033[1;34m\]\w\[\033[0m\]\$ "

echo ""
echo "👁️  AMBIENTE VISUAL - FUNDAÇÃO ALQUIMISTA"
echo "========================================"
echo "🎯 AMBIENTE (fundacao_venv) ATIVADO VISUALMENTE!"
echo "📁 Diretório: $(pwd)"
echo "🐍 Python: $(which python3)"
echo "⚛️  Qiskit: $(python3 -c 'from qiskit import __version__; print(__version__)' 2>/dev/null)"
echo ""

# Teste rápido
python3 -c "
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)  
qc.measure_all()
result = AerSimulator().run(qc, shots=5).result()
print('✅ Teste quântico rápido: OK')
"

echo ""
echo "🌌 AGORA VOCÊ VÊ: (fundacao_venv) no seu prompt!"
echo "💡 Digite 'python3' para Python ou execute scripts"
echo "🔧 Use 'deactivate' para sair do ambiente visual"
echo ""

# Manter shell com prompt personalizado
exec $SHELL
