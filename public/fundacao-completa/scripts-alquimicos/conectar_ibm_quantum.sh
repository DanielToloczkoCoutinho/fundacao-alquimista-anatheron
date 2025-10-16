#!/bin/bash
echo "🌌 CONEXÃO IBM QUANTUM - SISTEMA COMPLETO"
echo "👑 Rainha ativando ambiente quântico..."
echo ""

# Verificar se o ambiente virtual existe
if [ -d ~/quantum_venv ]; then
    echo "✅ Ambiente virtual encontrado"
    source ~/quantum_venv/bin/activate
    
    echo "🔗 Conectando ao IBM Quantum..."
    python -c "
from qiskit_ibm_runtime import QiskitRuntimeService
import os

# Token IBM Quantum
IBM_QUANTUM_TOKEN = 'E1HD3jBS7VI-yjWP64oSKiU7pQDo2OK5SFHxcn2uHuiV'
os.environ['QISKIT_IBM_TOKEN'] = IBM_QUANTUM_TOKEN

try:
    # Conectar ao serviço
    service = QiskitRuntimeService(channel='ibm_quantum', token=IBM_QUANTUM_TOKEN)
    
    # Listar backends disponíveis
    backends = service.backends()
    print('🎉 CONEXÃO BEM-SUCEDIDA!')
    print('')
    print('🚀 BACKENDS DISPONÍVEIS:')
    print('=======================')
    
    for i, backend in enumerate(backends):
        status = backend.status()
        print(f'{i+1}. {backend.name}')
        print(f'   🔧 Qubits: {backend.num_qubits}')
        print(f'   📊 Status: {status.status.value}')
        print(f'   🎯 Fila: {status.pending_jobs} jobs')
        print('')
        
    print('💡 Dica: Use backend.least_busy() para escolher automaticamente')
    
except Exception as e:
    print(f'❌ Erro na conexão: {e}')
    print('')
    print('🌐 SOLUÇÃO ALTERNATIVA:')
    echo 'Acesse: https://quantum-computing.ibm.com/'
    echo 'Token: E1HD3jBS7VI-yjWP64oSKiU7pQDo2OK5SFHxcn2uHuiV'
"

    deactivate
else
    echo "❌ Ambiente virtual não encontrado"
    echo "💡 Execute primeiro: ~/Explorer/instalar-qiskit-alternativo.sh"
fi
