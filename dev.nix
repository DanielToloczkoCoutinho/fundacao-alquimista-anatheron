{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python completo para execução contínua
    python3
    python3Packages.requests
    python3Packages.pip
    
    # Ferramentas essenciais
    git
    nodejs
    wget
    curl
    
    # Bibliotecas do sistema
    stdenv.cc.cc.lib
    zlib
  ];
  
  shellHook = ''
    echo "🐍 AMBIENTE FUNDAÇÃO ALQUIMISTA - CONFIGURADO"
    echo "✅ Python3 permanente para transmissão contínua"
    echo "🚀 Execute: python transmissor_base_lux.py"
  '';
}
