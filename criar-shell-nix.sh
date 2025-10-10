#!/bin/bash
# 🐚 CRIADOR DE SHELL.NIX PARA FUNDAÇÃO ALQUIMISTA
# 🚀 Ambiente reprodutível com Nix

echo "🐚 CRIANDO SHELL.NIX - FUNDAÇÃO ALQUIMISTA"
echo "🚀 Rainha Zennith - Ambiente Reprodutível"
echo "========================================="

# CRIAR SHELL.NIX PARA DESENVOLVIMENTO
cat > shell.nix << 'NIXEOF'
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "fundacao-alquimista";
  
  buildInputs = with pkgs; [
    # 🐍 Python e ferramentas científicas
    python3
    python3Packages.pip
    python3Packages.virtualenv
    
    # 🔷 Computação Quântica
    python3Packages.qiskit
    python3Packages.qiskit-aer
    python3Packages.qiskit-ibm-runtime
    
    # 📊 Ciência de Dados
    python3Packages.numpy
    python3Packages.scipy
    python3Packages.matplotlib
    python3Packages.pandas
    python3Packages.jupyter
    
    # 🛠️ Ferramentas de Desenvolvimento
    git
    nodejs_20
    yarn
    curl
    wget
    
    # 🔧 Utilitários
    which
    findutils
    gnused
    gnugrep
  ];
  
  shellHook = ''
    echo "🔮 AMBIENTE FUNDAÇÃO ALQUIMISTA - NIX SHELL"
    echo "🐍 Python: $(python3 --version)"
    echo "🔷 Qiskit: Disponível"
    echo "📊 Numpy/Matplotlib: Disponível"
    echo ""
    echo "👑 Rainha Zennith - Ambiente Ativado!"
    
    # Criar virtualenv se não existir
    if [ ! -d "quantum_venv" ]; then
      echo "🐍 Criando virtualenv..."
      python3 -m venv quantum_venv
    fi
    
    # Ativar virtualenv
    source quantum_venv/bin/activate
    
    # Instalar dependências Python adicionais
    pip install --upgrade pip
  '';
}
NIXEOF

echo "✅ shell.nix criado com sucesso!"
echo ""
echo "📦 PACOTES INCLUÍDOS:"
echo "  🐍 Python 3 + pip + virtualenv"
echo "  🔷 Qiskit + Qiskit-Aer + IBM Runtime"
echo "  📊 Numpy, Scipy, Matplotlib, Pandas, Jupyter"
echo "  🛠️ Git, Node.js, Yarn, curl, wget"
echo "  🔧 Utilitários do sistema"

echo ""
echo "🚀 PARA USAR:"
echo "  nix-shell  # Entrar no ambiente"
echo "  ou"
echo "  nix-shell --run 'python fundacao_master.py'"
