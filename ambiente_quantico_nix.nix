{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "fundacao-quantica";
  
  buildInputs = with pkgs; [
    # Quantum Computing
    python3
    python3Packages.qiskit
    python3Packages.numpy
    python3Packages.scipy
    
    # Frontend Quantum
    nodejs
    yarn
    
    # Development Tools
    git
    vim
    curl
  ];
  
  shellHook = ''
    echo "🌌 AMBIENTE QUÂNTICO DA FUNDAÇÃO ATIVADO!"
    echo "⚛️  Qiskit: $(python -c 'import qiskit; print(qiskit.__version__)' 2>/dev/null || echo 'Instalando...')"
    echo "🔧 Node: $(node --version)"
    echo "🚀 Pronto para desenvolvimento quântico!"
  '';
}
