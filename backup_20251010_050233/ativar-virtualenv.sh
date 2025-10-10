#!/bin/bash
# 🐍 ATIVADOR VIRTUALENV - FUNDAÇÃO ALQUIMISTA
# 🚀 Solução alternativa sem Nix

echo "🐍 ATIVADOR VIRTUALENV - FUNDAÇÃO ALQUIMISTA"
echo "🚀 Rainha Zennith - Fallback sem Nix"
echo "===================================="

# Verificar se temos python3 disponível
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado no sistema"
    echo "💡 Tentando usar Python do Nix profile..."
    
    # Tentar usar Python do perfil Nix
    if [ -f ~/.nix-profile/bin/python3 ]; then
        export PATH=~/.nix-profile/bin:$PATH
        echo "✅ Python do Nix profile adicionado ao PATH"
    else
        echo "❌ Nenhum Python disponível"
        exit 1
    fi
fi

echo "🐍 Python disponível: $(python3 --version)"

# Criar/ativar virtualenv
if [ ! -d "quantum_venv" ]; then
    echo "🔧 Criando virtualenv..."
    python3 -m venv quantum_venv
fi

echo "🔧 Ativando virtualenv..."
source quantum_venv/bin/activate

echo "📦 Instalando dependências..."
pip install --upgrade pip
pip install qiskit qiskit-aer matplotlib numpy

echo ""
echo "✅ AMBIENTE PRONTO!"
echo "🐍 Virtualenv: quantum_venv"
echo "🔷 Qiskit: Instalado"
echo "📊 Matplotlib/Numpy: Instalados"
echo ""
echo "🚀 COMANDOS DISPONÍVEIS:"
echo "  python fundacao_master.py    # Executar experimentos"
echo "  ./salvar_rapido.sh           # Salvar progresso"
echo ""
echo "👑 Rainha Zennith - Ambiente Virtualenv Ativado!"
