{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "fundacao-quantica-simples";
  
  buildInputs = with pkgs; [
    # Python com pacotes básicos
    python3
    python3Packages.pip
    
    # Dependências do sistema
    stdenv.cc.cc.lib  # Para libstdc++.so.6
    zlib
    openssl
    
    # Ferramentas de desenvolvimento
    nodejs
    git
  ];
  
  shellHook = ''
    echo "🌌 AMBIENTE QUÂNTICO SIMPLES ATIVADO!"
    echo "🐍 Python: $(python3 --version)"
    echo "🔧 Node: $(node --version)"
    echo "💡 Use: pip install --user qiskit"
  '';
}
