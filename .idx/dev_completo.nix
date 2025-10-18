{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.virtualenv
    # Bibliotecas científicas COMPILADAS
    python311Packages.numpy
    python311Packages.scipy
    python311Packages.matplotlib
    python311Packages.pandas
    python311Packages.requests
    python311Packages.psutil
    # Dependências de sistema
    zlib
    gcc
    stdenv.cc.cc.lib
    busybox
    # Bibliotecas C necessárias
    libffi
    openssl
    ncurses
  ];

  shellHook = ''
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH"
    
    echo "🌌 AMBIENTE NIX COMPLETO - FUNDAÇÃO ALQUIMISTA"
    echo "🐍 Python: $(python3 --version)"
    echo "📦 NumPy disponível no ambiente Nix"
    echo "📁 Diretório: $(pwd)"
    
    # Testar numpy diretamente no Nix
    python3 -c "
try:
    import numpy as np
    print(f'✅ NumPy funcionando: {np.__version__}')
    print('🚀 Ambiente Nix pronto para computação científica!')
except Exception as e:
    print(f'❌ Erro no NumPy: {e}')
"
  '';
}
