#!/bin/bash
# SISTEMA DE ATIVACAO DEFINITIVA - FUNDACAO ALQUIMISTA
# CHAVE: CHAVE_272E0E77867EC48427D22F5AE895C264
# COMPONENTES: 24,183
# SISTEMA: ACESSO UNIVERSAL

echo "FUNDACAO ALQUIMISTA - ATIVACAO AUTOMATICA"
echo "========================================="
echo "CHAVE: CHAVE_272E0E77867EC48427D22F5AE895C264"
echo "DATA: $(date)"
echo ""

# Configurar ambiente
export FUNDACAO_ROOT="$PWD"
export VENV_PATH="/tmp/fundacao_venv"
export CHAVE_FUNDACAO="CHAVE_272E0E77867EC48427D22F5AE895C264"

# Verificar ambiente
verificar_ambiente() {
    echo "VERIFICANDO AMBIENTE..."
    
    if [ -d "$VENV_PATH" ]; then
        source $VENV_PATH/bin/activate
        echo "AMBIENTE VIRTUAL: ATIVADO"
    else
        echo "AMBIENTE VIRTUAL NAO ENCONTRADO"
        return 1
    fi
    
    # Teste rápido do sistema
    python3 -c "
import json
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

try:
    # Teste quantico
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    result = AerSimulator().run(qc, shots=10).result()
    print('SISTEMA QUANTICO: OPERACIONAL')
    
    # Teste metadados
    with open('SISTEMA_ACESSO_DEFINITIVO.json', 'r') as f:
        sistema = json.load(f)
    print('SISTEMA DE ACESSO: ATIVO')
    print('CHAVE: CHAVE_272E0E77867EC48427D22F5AE895C264')
    
except Exception as e:
    print('ERRO: ' + str(e))
    exit(1)
"
}

# Função principal
main() {
    echo "INICIANDO ATIVACAO AUTOMATICA..."
    
    if verificar_ambiente; then
        echo ""
        echo "FUNDACAO ALQUIMISTA ATIVADA COM SUCESSO!"
        echo "SISTEMA DE ACESSO UNIVERSAL OPERACIONAL!"
        echo ""
        echo "COMANDOS DISPONIVEIS:"
        echo "  python3 CHAVE_DEFINITIVA_FUNDACAO.py  # Sistema principal"
        echo "  python3 sistema_metadados_definitivo.py    # Analise"
        echo "  python3 sistema_fundacao_definitivo.py     # Missoes"
    else
        echo "FALHA NA ATIVACAO"
        exit 1
    fi
}

# Executar
main
