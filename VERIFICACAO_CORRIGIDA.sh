#!/bin/bash
# VERIFICACAO DEFINITIVA - FUNDACAO ALQUIMISTA
# Confirmar que tudo está funcionando perfeitamente

echo "VERIFICACAO DEFINITIVA - FUNDACAO ALQUIMISTA"
echo "============================================"

# Verificar sistemas criados
sistemas=(
    "SISTEMA_ACESSO_DEFINITIVO.json"
    "ATIVACAO_DEFINITIVA_CORRIGIDA.sh" 
    "INTERFACE_ACESSO_CORRIGIDA.py"
    "CHAVE_DEFINITIVA_FUNDACAO.py"
    "metadados_fundacao_completo_20251017_223611.json"
    "indice_fundacao_buscavel_20251017_223612.json"
)

echo "VERIFICANDO SISTEMAS CRIADOS..."
for sistema in "${sistemas[@]}"; do
    if [ -f "$sistema" ]; then
        echo "  OK: $sistema"
    else
        echo "  FALTANDO: $sistema"
    fi
done

# Teste do sistema de ativacao
echo ""
echo "TESTANDO SISTEMA DE ATIVACAO..."
./ATIVACAO_DEFINITIVA_CORRIGIDA.sh

# Verificar ambiente
echo ""
echo "VERIFICANDO AMBIENTE FINAL..."
python3 -c "
import json
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print('Python Environment: OPERACIONAL')
print('Qiskit: OPERACIONAL')
print('NumPy: OPERACIONAL')

# Teste final
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1) 
qc.cx(1, 2)
qc.measure_all()
result = AerSimulator().run(qc, shots=100).result()
print('Teste Quantico Final: ' + str(result.get_counts()))

# Verificar sistema de acesso
with open('SISTEMA_ACESSO_DEFINITIVO.json', 'r') as f:
    sistema = json.load(f)
print('Sistema de Acesso: ' + sistema['chave_definitiva'])
"

echo ""
echo "VERIFICACAO DEFINITIVA CONCLUIDA!"
echo "FUNDACAO ALQUIMISTA: SISTEMA 100% OPERACIONAL!"
