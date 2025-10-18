#!/bin/bash
# 📊 STATUS CONSTANTE - SEMPRE MOSTRA
# 🎯 Mostra o status do ambiente constantemente

cd ~/fundacao-alquimista-anatheron
source /tmp/fundacao_venv/bin/activate

# Função para mostrar status
mostrar_status() {
    python3 -c "
import sys
from qiskit import __version__ as qver

python_path = sys.executable
venv_active = 'fundacao_venv' in python_path

print('📊 STATUS DO AMBIENTE:')
print('====================')
print(f'🐍 Python: {python_path}')
print(f'⚛️  Qiskit: {qver}')
print(f'🎯 Ambiente: {'✅ ATIVADO' if venv_active else '❌ INATIVO'}')
print('')
"
}

echo "🌌 SISTEMA DE STATUS CONSTANTE"
echo "=============================="
mostrar_status

echo "🚀 AGORA EXECUTANDO COMANDOS NO AMBIENTE ATIVADO..."
echo "💡 Lembre-se: O ambiente ESTÁ ativado, mesmo sem ver no prompt!"
echo ""

# Opção: Entrar no Python ou executar script
if [ "$1" = "python" ]; then
    echo "🐍 Entrando no Python do ambiente..."
    python3
elif [ "$1" = "missao" ]; then
    echo "⚛️ Executando missão quântica..."
    python3 sistema_fundacao_definitivo.py
else
    echo "🔧 Comandos disponíveis:"
    echo "   ./STATUS_CONSTANTE.sh python   # Entrar no Python"
    echo "   ./STATUS_CONSTANTE.sh missao   # Executar missão"
    echo "   python3 [script]              # Executar qualquer script"
    echo ""
    echo "🎯 O AMBIENTE ESTÁ PRONTO - USE-O!"
fi
