#!/bin/bash
# 🔧 VERIFICADOR DE AMBIENTE - FUNDAÇÃO ALQUIMISTA
# 🎯 Diagnóstico completo do sistema

echo "🔧 VERIFICADOR DE AMBIENTE - FUNDAÇÃO ALQUIMISTA"
echo "🎯 Rainha Zennith - Diagnóstico Completo"
echo "========================================"

# VERIFICAR NIX
echo "📦 SISTEMA NIX:"
if command -v nix-env &> /dev/null; then
    echo "✅ Nix Environment: INSTALADO"
    echo "   Versão: $(nix-env --version)"
    echo "   Pacotes: $(nix-env -q 2>/dev/null | wc -l) instalados"
else
    echo "❌ Nix Environment: NÃO ENCONTRADO"
fi

# VERIFICAR PYTHON
echo ""
echo "🐍 AMBIENTE PYTHON:"
if command -v python3 &> /dev/null; then
    python_path=$(which python3)
    python_version=$(python3 --version 2>/dev/null || echo "N/A")
    echo "✅ Python3: ENCONTRADO"
    echo "   Caminho: $python_path"
    echo "   Versão: $python_version"
    
    # Verificar se é do Nix
    if [[ "$python_path" == *"/nix/store/"* ]]; then
        echo "   🏗️ Fornecido pelo: NIX"
    else
        echo "   🏗️ Fornecido pelo: SISTEMA/VENV"
    fi
else
    echo "❌ Python3: NÃO ENCONTRADO"
fi

# VERIFICAR VIRTUALENV
echo ""
echo "🔧 VIRTUALENV:"
if [ -d "quantum_venv" ]; then
    echo "✅ quantum_venv: EXISTE"
    if [ -f "quantum_venv/bin/activate" ]; then
        echo "   ✅ Script activate: EXISTE"
    else
        echo "   ❌ Script activate: NÃO ENCONTRADO"
    fi
else
    echo "❌ quantum_venv: NÃO EXISTE"
fi

# VERIFICAR DEPENDÊNCIAS PYTHON
echo ""
echo "📊 DEPENDÊNCIAS PYTHON:"
if command -v python3 &> /dev/null; then
    # Testar importações
    for pkg in "qiskit" "matplotlib" "numpy"; do
        if python3 -c "import $pkg" 2>/dev/null; then
            echo "✅ $pkg: INSTALADO"
        else
            echo "❌ $pkg: NÃO INSTALADO"
        fi
    done
else
    echo "ℹ️ Python não disponível para verificar dependências"
fi

# VERIFICAR SHELL.NIX
echo ""
echo "🐚 SHELL.NIX:"
if [ -f "shell.nix" ]; then
    echo "✅ shell.nix: EXISTE"
    echo "   Tamanho: $(wc -l < shell.nix) linhas"
else
    echo "❌ shell.nix: NÃO EXISTE"
fi

# RESUMO
echo ""
echo "📋 RESUMO DO AMBIENTE:"
echo "======================"

if command -v nix-env &> /dev/null && command -v python3 &> /dev/null && [ -f "shell.nix" ]; then
    echo "🎉 AMBIENTE: OTIMIZADO"
    echo "   🏗️ Nix: CONFIGURADO"
    echo "   🐍 Python: DISPONÍVEL" 
    echo "   🐚 shell.nix: PRONTO"
    echo ""
    echo "🚀 COMANDOS DISPONÍVEIS:"
    echo "   nix-shell                    # Ambiente completo"
    echo "   source quantum_venv/bin/activate  # Virtualenv"
    echo "   python fundacao_master.py    # Experimentos"
else
    echo "⚠️ AMBIENTE: CONFIGURAÇÃO NECESSÁRIA"
    echo "   💡 Execute: ./criar-shell-nix.sh"
    echo "   💡 Execute: ./instalar-pacotes-nix.sh"
fi
