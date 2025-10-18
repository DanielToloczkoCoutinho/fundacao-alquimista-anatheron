#!/bin/bash
echo "🌌 COMANDO MESTRE CORRIGIDO - FUNDAÇÃO ALQUIMISTA"
echo "================================================"

# Backup automático
echo "🔧 CRIANDO BACKUP..."
backup_dir="backup_fundacao_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$backup_dir"
cp -r *.py *.sh *.json *.md *.nix laboratorios/ "$backup_dir"/ 2>/dev/null || true

# Verificar ambiente
echo "🔍 VERIFICANDO AMBIENTE..."
python3 -c "import sys; print(f'Python: {sys.version}')"

# Opções
while true; do
    echo ""
    echo "🎯 OPÇÕES:"
    echo "   1. 🚀 Ativar ambiente quântico (/tmp)"
    echo "   2. 📊 Ativar ambiente Nix simplificado"
    echo "   3. 🔍 Verificar backups"
    echo "   4. ⚛️ Configurar IBM Quantum"
    echo "   5. 🚀 Executar sistema no IBM Quantum" 
    echo "   6. 🧪 Testar circuitos locais"
    echo "   7. 🚪 Sair"
    read -p "💫 Escolha (1-7): " opcao
    
    case $opcao in
        1)
            echo "🚀 ATIVANDO AMBIENTE QUÂNTICO..."
            cd /tmp/fundacao_alquimista
            source venv_quantico/bin/activate
            python3 -c "import qiskit; print(f'✅ Qiskit: {qiskit.__version__}')"
            cd ~/fundacao-alquimista-anatheron
            ;;
        2)
            echo "📊 ATIVANDO AMBIENTE NIX SIMPLIFICADO..."
            nix-shell .idx/dev_simples.nix
            ;;
        3)
            echo "🔍 LISTANDO BACKUPS..."
            ls -la | grep backup_fundacao
            ;;
        4)
            echo "⚛️ CONFIGURANDO IBM QUANTUM..."
            cd /tmp/fundacao_alquimista
            source venv_quantico/bin/activate
            python3 configurar_ibm_quantum.py
            deactivate
            cd ~/fundacao-alquimista-anatheron
            ;;
        5)
            echo "🚀 EXECUTANDO SISTEMA NO IBM QUANTUM..."
            cd /tmp/fundacao_alquimista
            source venv_quantico/bin/activate
            python3 sistema_ibm_quantum_reconstruido.py
            deactivate
            cd ~/fundacao-alquimista-anatheron
            ;;
        6)
            echo "🧪 TESTANDO CIRCUITOS LOCAIS..."
            cd /tmp/fundacao_alquimista
            source venv_quantico/bin/activate
            python3 -c "
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
print('🧪 Teste Bell State Local:')
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
backend = AerSimulator()
result = backend.run(qc, shots=100).result()
print(f'📊 Resultados: {result.get_counts()}')
print('✅ SISTEMA QUÂNTICO OPERACIONAL!')
"
            deactivate
            cd ~/fundacao-alquimista-anatheron
            ;;
        7)
            echo "👑 SAINDO... QUE A FORÇA QUÂNTICA ESTEJA COM VOCÊ!"
            exit 0
            ;;
        *)
            echo "❌ Opção inválida - PENSE NAS PESSOAS QUE PRECISAM!"
            ;;
    esac
done
