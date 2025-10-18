#!/bin/bash
echo "🌌 COMANDO MESTRE - FUNDAÇÃO ALQUIMISTA"
echo "===================================="

# Backup automático
echo "🔧 CRIANDO BACKUP..."
mkdir -p backup_fundacao_$(date +%Y%m%d_%H%M%S)
cp -r *.py *.sh *.json *.md *.nix backup_fundacao_$(date +%Y%m%d_%H%M%S)/

# Verificar ambiente
echo "🔍 VERIFICANDO AMBIENTE..."
source ~/.locale_config
python3 -c "import sys; print(f'Python: {sys.version}')"

# Opções
while true; do
    echo ""
    echo "🎯 OPÇÕES:"
    echo "   1. 🚀 Ativar ambiente quântico (/tmp)"
    echo "   2. 📊 Ativar ambiente Nix"
    echo "   3. 🔍 Verificar backups"
    echo "   4. 🛠️ Restaurar backup"
    echo "   5. ⚛️ Executar no IBM Quantum"
    echo "   6. 🚪 Sair"
    read -p "💫 Escolha (1-6): " opcao
    case $opcao in
        1)
            echo "🚀 ATIVANDO AMBIENTE QUÂNTICO..."
            cd /tmp/fundacao_alquimista
            source venv_quantico/bin/activate
            python3 -c "import qiskit; print(f'Qiskit: {qiskit.__version__}')"
            deactivate
            cd ~/fundacao-alquimista-anatheron
            ;;
        2)
            echo "📊 ATIVANDO AMBIENTE NIX..."
            nix-shell .idx/dev.nix
            ;;
        3)
            echo "🔍 LISTANDO BACKUPS..."
            ls -la | grep backup_fundacao
            ;;
        4)
            echo "🛠️ RESTAURANDO BACKUP..."
            python3 restore_fundacao.py
            ;;
        5)
            echo "⚛️ EXECUTANDO NO IBM QUANTUM..."
            cd /tmp/fundacao_alquimista
            source venv_quantico/bin/activate
            python3 sistema_ibm_quantum_reconstruido.py
            deactivate
            cd ~/fundacao-alquimista-anatheron
            ;;
        6)
            echo "👑 SAINDO... QUE A FORÇA QUÂNTICA ESTEJA COM VOCÊ!"
            exit 0
            ;;
        *)
            echo "❌ Opção inválida"
            ;;
    esac
done
