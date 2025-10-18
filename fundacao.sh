#!/bin/bash
# 🚀 INICIALIZADOR DEFINITIVO - FUNDAÇÃO ALQUIMISTA
# �� Sempre funciona, sempre pronto

echo "🌌 FUNDAÇÃO ALQUIMISTA - INICIALIZADOR DEFINITIVO"
echo "================================================="

# Configuração definitiva
VENV_PATH="/tmp/fundacao_definitivo"

# Verificar e criar ambiente se necessário
if [ ! -d "$VENV_PATH" ] || [ ! -f "$VENV_PATH/bin/activate" ]; then
    echo "🔧 Criando ambiente definitivo..."
    python3 -m venv $VENV_PATH
    source $VENV_PATH/bin/activate
    pip install "qiskit>=1.0" matplotlib pylatexenc --no-cache-dir
else
    source $VENV_PATH/bin/activate
fi

# Verificação final
echo "🔍 Verificação final do sistema..."
python3 -c "
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

print('✅ Qiskit: OPERACIONAL')
print('✅ Aer Simulator: OPERACIONAL') 
print('✅ Matplotlib: OPERACIONAL')

# Teste rápido
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
result = AerSimulator().run(qc, shots=100).result()
print(f'✅ Teste quântico: {result.get_counts()}')

print('')
print('🎉 SISTEMA FUNDAÇÃO ALQUIMISTA: PRONTO PARA MISSÕES!')
print('🌌 Execute: python3 sistema_fundacao_perfeito.py')
"

echo ""
echo "💡 COMANDOS DISPONÍVEIS:"
echo "   python3 sistema_fundacao_perfeito.py  # Sistema principal"
echo "   python3 missao_corrigida.py           # Missões básicas"
echo ""
echo "🚀 AMBIENTE CONFIGURADO COM SUCESSO!"
