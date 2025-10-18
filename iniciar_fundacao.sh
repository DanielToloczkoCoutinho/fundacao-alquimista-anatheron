#!/bin/bash
# 🚀 SCRIPT DE INICIALIZAÇÃO - FUNDAÇÃO ALQUIMISTA
# 🌌 Inicialização confiável do ambiente

echo "🌌 INICIANDO FUNDAÇÃO ALQUIMISTA..."
echo "==================================="

# Configurar ambiente
export VENV_PATH="/tmp/fundacao_venv_fresco"

# Verificar se venv existe, se não, criar
if [ ! -d "$VENV_PATH" ]; then
    echo "🔧 Criando ambiente virtual..."
    python3 -m venv $VENV_PATH
fi

# Ativar venv
source $VENV_PATH/bin/activate

# Verificar instalações básicas
echo "🔍 Verificando instalações..."
python3 -c "
try:
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    print('✅ Qiskit: OK')
    
    import matplotlib.pyplot as plt
    print('✅ Matplotlib: OK')
    
    print('🚀 Ambiente pronto para missões quânticas!')
    
except ImportError as e:
    print(f'❌ Falha: {e}')
    print('💡 Execute: pip install qiskit matplotlib')
"

echo "🌌 FUNDAÇÃO ALQUIMISTA INICIALIZADA!"
echo "💡 Comandos disponíveis:"
echo "   python3 sistema_fundacao_robusto.py"
echo "   python3 missao_corrigida.py"
