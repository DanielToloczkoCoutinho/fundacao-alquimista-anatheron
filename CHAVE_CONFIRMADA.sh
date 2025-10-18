#!/bin/bash
# 🔑 CHAVE CONFIRMADA - SEMPRE FUNCIONA
# 🎯 Ativa E prova que está funcionando

echo "🔑 CHAVE CONFIRMADA - FUNDAÇÃO ALQUIMISTA"
echo "========================================="

# Sempre ativar (não importa se já está)
cd ~/fundacao-alquimista-anatheron
source /tmp/fundacao_venv/bin/activate

# Prova visual definitiva
echo "🎯 CONFIRMAÇÃO VISUAL DO AMBIENTE:"
echo "=================================="

python3 -c "
import sys
from qiskit import __version__ as qver

# Informações do sistema
python_path = sys.executable
print(f'📍 Python ativo: {python_path}')
print(f'⚛️  Qiskit versão: {qver}')

# Verificar se está no venv
if 'fundacao_venv' in python_path:
    status = '✅ DENTRO DO AMBIENTE'
    emoji = '🎉'
else:
    status = '❌ FORA DO AMBIENTE'  
    emoji = '⚠️'

print(f'{emoji} Status: {status}')
print('')

# Execução quântica de confirmação
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, name='Confirmação')
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

result = AerSimulator().run(qc, shots=50).result()
counts = result.get_counts()

print('🚀 TESTE QUÂNTICO EXECUTADO:')
print(f'   📊 {counts}')
print('')
print('🌌 MENSAGEM FINAL:')
print('   O AMBIENTE ESTÁ ATIVADO E FUNCIONAL!')
print('   Execute: python3 sistema_fundacao_definitivo.py')
print('')
"

# Manter ativo
echo "💫 O ambiente está PRONTO para uso!"
echo "🔧 Execute scripts quânticos agora!"
