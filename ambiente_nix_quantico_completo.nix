{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "fundacao-quantica-nix-completo";
  
  buildInputs = with pkgs; [
    # Python com pacotes quânticos
    python3
    python3Packages.numpy
    python3Packages.scipy
    python3Packages.matplotlib
    python3Packages.pip
    
    # Qiskit via pip (versões mais recentes)
    python3Packages.qiskit
    python3Packages.qiskit-aer
    python3Packages.qiskit-ibm-runtime
    
    # Dependências de sistema CRÍTICAS
    zlib
    stdenv.cc.cc.lib
    glibc
    gcc
    binutils
    
    # Ferramentas de desenvolvimento
    nodejs
    git
    docker
    docker-compose
  ];
  
  shellHook = ''
    echo "🌌 AMBIENTE NIX QUÂNTICO COMPLETO ATIVADO!"
    echo "🐍 Python: $(python3 --version)"
    echo "📦 NumPy: $(python3 -c 'import numpy; print(numpy.__version__)' 2>/dev/null || echo 'Não instalado')"
    echo "⚛️  Qiskit: $(python3 -c 'import qiskit; print(qiskit.__version__)' 2>/dev/null || echo 'Não instalado')"
    echo "💡 Todas as dependências de sistema incluídas!"
  '';
}
