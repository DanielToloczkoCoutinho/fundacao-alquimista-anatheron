#!/bin/bash
# 🔑 CHAVE UNIVERSAL - FIREBASE FUNDAÇÃO ALQUIMISTA
# ⚛️ Acesso garantido em qualquer situação

echo "🔑 INICIANDO CHAVE UNIVERSAL..."
echo "================================"

# Função para configurar ambiente
setup_ambiente() {
    # Tentar diretório da Fundação
    if [ -d "~/fundacao-alquimista-anatheron" ]; then
        cd ~/fundacao-alquimista-anatheron
    elif [ -d "/home/user/fundacao-alquimista-anatheron" ]; then
        cd /home/user/fundacao-alquimista-anatheron
    else
        echo "📁 Buscando diretório da Fundação..."
        find ~ -name "fundacao-alquimista-anatheron" -type d 2>/dev/null | head -1 | while read dir; do
            cd "$dir"
            echo "✅ Encontrado em: $dir"
        done
    fi
    
    # Ativar ambiente virtual
    if [ -d "/tmp/fundacao_venv" ]; then
        source /tmp/fundacao_venv/bin/activate
        echo "✅ Ambiente virtual ativado"
    else
        echo "🔄 Criando ambiente virtual..."
        python3 -m venv /tmp/fundacao_venv
        source /tmp/fundacao_venv/bin/activate
        pip install qiskit matplotlib --quiet
        echo "✅ Novo ambiente criado e ativado"
    fi
}

# Executar configuração
setup_ambiente

# Verificação final
echo "🔍 Verificando sistema..."
python3 -c "
try:
    import sys
    print(f'🐍 Python: {sys.version.split()[0]}')
    
    from qiskit import __version__ as qiskit_ver
    print(f'⚛️ Qiskit: {qiskit_ver}')
    
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    
    result = AerSimulator().run(qc, shots=5).result()
    print('✅ Teste quântico: OK')
    
    print('')
    print('🎉 CHAVE UNIVERSAL ATIVADA!')
    print('🌌 FUNDAÇÃO ALQUIMISTA - SISTEMA OPERACIONAL')
    print('📁 Diretório: ' + __import__('os').getcwd())
    
except Exception as e:
    print(f'❌ Erro: {e}')
    print('💡 Execute: pip install qiskit')
"

echo ""
echo "🚀 PRONTO PARA MISSÕES QUÂNTICAS!"
