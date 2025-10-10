#!/bin/bash
echo "🧪 CORRIGINDO BIBLIOTECAS C++ - Rainha Zennith"
echo "=============================================="

cat > shell.nix << 'EOL'
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.virtualenv
    
    # Bibliotecas científicas Python
    python311Packages.numpy
    python311Packages.matplotlib
    python311Packages.scipy
    
    # Bibliotecas C++ ESSENCIAIS para Qiskit Aer
    stdenv.cc.cc.lib  # libstdc++.so.6
    zlib
    numactl
    
    # Ferramentas de desenvolvimento
    gcc
    gnumake
    cmake
  ];

  # Variáveis de ambiente para Python
  VIRTUAL_ENV = "./quantum_venv";
  PYTHONPATH = "./quantum_venv/lib/python3.11/site-packages";
  
  shellHook = ''
    echo "🔮 AMBIENTE FUNDAÇÃO ALQUIMISTA - NIX SHELL CORRIGIDO"
    echo "🐍 Python: $(python --version)"
    echo "📊 Numpy/Matplotlib: Disponível"
    echo "⚛️  Qiskit: Será instalado via pip"
    echo "🔧 Bibliotecas C++: Incluídas"
    
    # Criar virtualenv se não existir
    if [ ! -d "quantum_venv" ]; then
      echo "🐍 Criando virtualenv..."
      python -m venv quantum_venv
    fi
    
    # Ativar virtualenv
    source quantum_venv/bin/activate
    
    # Instalar Qiskit se não estiver instalado
    if ! python -c "import qiskit" 2>/dev/null; then
      echo "📦 Instalando Qiskit via pip..."
      pip install --upgrade pip
      pip install qiskit qiskit-aer
    fi
    
    echo "✅ Ambiente pronto! Use: python fundacao_master.py"
  '';
}
EOL

echo "✅ shell.nix corrigido criado com bibliotecas C++!"
echo "🚀 Execute: nix-shell --run 'python fundacao_master.py'"
