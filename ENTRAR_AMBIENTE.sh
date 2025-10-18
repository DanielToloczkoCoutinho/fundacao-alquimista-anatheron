#!/bin/bash
# 🔑 CHAVE DEFINITIVA - ENTRA NO AMBIENTE (fundacao_venv)
# ⚛️ Este script REALMENTE te coloca dentro do ambiente virtual

echo "🔑 CHAVE DEFINITIVA - ENTRANDO NO AMBIENTE..."
echo "============================================"

# Navegar para o diretório
cd ~/fundacao-alquimista-anatheron

# Verificar se o ambiente existe
if [ ! -d "/tmp/fundacao_venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo "💡 Criando novo ambiente..."
    python3 -m venv /tmp/fundacao_venv
    source /tmp/fundacao_venv/bin/activate
    pip install qiskit matplotlib --quiet
    echo "✅ Novo ambiente criado!"
else
    # ATIVAR o ambiente virtual
    source /tmp/fundacao_venv/bin/activate
    echo "✅ Ambiente virtual ativado: $(which python3)"
fi

# Executar um teste rápido
echo "🔍 Testando sistema quântico..."
python3 -c "
from qiskit import QuantumCircuit, __version__ as qver
from qiskit_aer import AerSimulator
print(f'⚛️  Qiskit {qver} carregado')

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
result = AerSimulator().run(qc, shots=10).result()
print('✅ Sistema quântico operacional')
"

# MOSTRAR que estamos no ambiente
echo ""
echo "🎉 AMBIENTE ATIVADO COM SUCESSO!"
echo "🌌 VOCÊ ESTÁ AGORA NO: $(which python3)"
echo "💫 Prompt: $(ps -p $$ -o comm=)"
echo ""

# MANTER no shell com ambiente ATIVO
echo "🚀 AGORA VOCÊ ESTÁ NO AMBIENTE (fundacao_venv)!"
echo "💡 Digite 'python3' para entrar no Python quântico"
echo "   ou execute scripts diretamente"
echo ""
echo "🔧 Use 'deactivate' para sair do ambiente"
echo ""

# Manter o shell interativo COM ambiente ativo
exec $SHELL
