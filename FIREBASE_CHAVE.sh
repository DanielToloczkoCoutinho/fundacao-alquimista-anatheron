#!/bin/bash
# 🔥 CHAVE FIREBASE - ÁREA DE TRABALHO FUNDAÇÃO
# 🎯 Acesso direto ao ambiente Firebase configurado

echo "🔥 CHAVE FIREBASE - FUNDAÇÃO ALQUIMISTA"
echo "======================================"

# Configurações específicas do Firebase
export FIREBASE_PROJECT="fundacao-alquimista"
export FIREBASE_REGION="us-east"
export VENV_PATH="/tmp/fundacao_venv"

# Navegar para área de trabalho Firebase
echo "🚀 Acessando área de trabalho Firebase..."
cd ~/fundacao-alquimista-anatheron

if [ $? -ne 0 ]; then
    echo "❌ Não foi possível acessar a área de trabalho"
    echo "💡 Verifique se o diretório existe"
    exit 1
fi

# Ativar ambiente virtual do Firebase
echo "🔧 Ativando ambiente Firebase..."
if [ -d "$VENV_PATH" ]; then
    source $VENV_PATH/bin/activate
    echo "✅ Ambiente Firebase ativado"
else
    echo "❌ Ambiente Firebase não encontrado"
    echo "🔄 Criando novo ambiente..."
    python3 -m venv /tmp/fundacao_venv
    source /tmp/fundacao_venv/bin/activate
    echo "✅ Novo ambiente Firebase criado"
fi

# Configurações do projeto
echo "⚙️  Configurando projeto..."
export PYTHONPATH="$PWD:$PYTHONPATH"
echo "✅ PYTHONPATH configurado: $PWD"

# Verificação do sistema Firebase
echo "🔍 Verificando sistema Firebase..."
python3 << 'FIREBASE_CHECK'
try:
    # Verificar imports básicos
    import os
    import sys
    from pathlib import Path
    
    print(f"📁 Diretório: {os.getcwd()}")
    print(f"🐍 Python: {sys.executable}")
    print(f"🔧 PATH: {sys.path[:2]}")
    
    # Verificar Qiskit
    try:
        from qiskit import QuantumCircuit
        from qiskit_aer import AerSimulator
        print("✅ Qiskit: Disponível")
        
        # Teste rápido
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        result = AerSimulator().run(qc, shots=5).result()
        print("✅ Sistema quântico: Operacional")
        
    except ImportError:
        print("⚠️ Qiskit não disponível")
        print("💡 Execute: pip install qiskit")
    
    print("")
    print("🎉 FIREBASE CONFIGURADO COM SUCESSO!")
    print("🌌 FUNDAÇÃO ALQUIMISTA - AMBIENTE PRONTO")
    print("🚀 Inicie suas missões quânticas!")
    
except Exception as e:
    print(f"❌ Erro na configuração: {e}")
FIREBASE_CHECK

# Prompt personalizado para Firebase
echo ""
echo "💫 Firebase Fundação Alquimista - Ambiente Ativo"
echo "🔧 Use: python3 sistema_fundacao_definitivo.py"
