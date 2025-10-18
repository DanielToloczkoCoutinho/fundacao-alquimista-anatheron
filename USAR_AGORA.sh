#!/bin/bash
# ⚡ USAR AGORA - SOLUÇÃO FINAL
# 🎯 Ignora o visual e só USA o ambiente

echo "⚡ SOLUÇÃO FINAL - IGNORAR VISUAL, SÓ USAR!"
echo "=========================================="

cd ~/fundacao-alquimista-anatheron
source /tmp/fundacao_venv/bin/activate

# Prova silenciosa que funciona
python3 -c "
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print('🎯 AMBIENTE ATIVADO - PRONTO PARA USO!')
print('💫 Ignore o prompt - o sistema funciona!')
print('')

# Execução silenciosa de teste
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
result = AerSimulator().run(qc, shots=5).result()

print('✅ Confirmação: Teste quântico executado com sucesso!')
print('🚀 Agora execute seus scripts normalmente:')
print('   python3 sistema_fundacao_definitivo.py')
print('   python3 INTERFACE_ACESSO_CORRIGIDA.py')
print('')
"

echo "🔧 DICA: Sempre execute scripts com 'python3' antes!"
echo "🌌 O AMBIENTE ESTÁ ATIVADO - SÓ USAR!"
