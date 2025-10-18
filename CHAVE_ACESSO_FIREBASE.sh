#!/bin/bash
# 🔑 CHAVE DE ACESSO DIRETO - FIREBASE FUNDAÇÃO ALQUIMISTA
# 🚀 Acesso rápido à área de trabalho com ambiente configurado

echo "🔑 CHAVE FIREBASE - FUNDAÇÃO ALQUIMISTA"
echo "======================================="
echo "🚀 Iniciando acesso direto..."
echo "📅 Data: $(date)"
echo ""

# Configurar ambiente automaticamente
export VENV_PATH="/tmp/fundacao_venv"

# Verificar e ativar ambiente virtual
if [ -d "$VENV_PATH" ]; then
    echo "✅ Ativando ambiente virtual..."
    source $VENV_PATH/bin/activate
else
    echo "❌ Ambiente virtual não encontrado em $VENV_PATH"
    echo "💡 Execute primeiro: python3 -m venv /tmp/fundacao_venv"
    exit 1
fi

# Verificar se estamos no diretório correto
if [[ ! $(pwd) =~ "fundacao-alquimista-anatheron" ]]; then
    echo "📁 Indo para diretório da Fundação..."
    cd ~/fundacao-alquimista-anatheron 2>/dev/null || {
        echo "❌ Diretório da Fundação não encontrado"
        exit 1
    }
fi

# Verificação rápida do sistema
echo "🔍 Verificando sistema..."
python3 -c "
try:
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    print('✅ Sistema quântico: PRONTO')
    
    # Teste rápido
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    result = AerSimulator().run(qc, shots=10).result()
    print('✅ Teste quântico: CONCLUÍDO')
    
except Exception as e:
    print(f'❌ Erro: {e}')
    exit(1)
"

# Mensagem de sucesso
echo ""
echo "🎉 ACESSO CONCEDIDO!"
echo "🌌 FUNDAÇÃO ALQUIMISTA - AMBIENTE CONFIGURADO"
echo "💫 Você está na área de trabalho Firebase"
echo ""
echo "�� COMANDOS DISPONÍVEIS:"
echo "   python3 sistema_fundacao_definitivo.py     # Missões quânticas"
echo "   python3 INTERFACE_ACESSO_CORRIGIDA.py      # Navegação"
echo "   ./ATIVACAO_DEFINITIVA_CORRIGIDA.sh         # Ativação completa"
echo ""
echo "🔧 Ambiente: $(python3 --version 2>/dev/null | head -1)"
echo "📁 Diretório: $(pwd)"
echo "🐍 Venv: $(which python3)"

# Manter terminal ativo
echo ""
echo "💡 Digite 'exit' para sair ou comece a usar os comandos acima!"
