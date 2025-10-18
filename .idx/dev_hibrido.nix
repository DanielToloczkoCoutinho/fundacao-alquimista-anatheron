{ pkgs ? import <nixpkgs> { config.allowBroken = true; } }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.virtualenv
    
    # Bibliotecas científicas COMPILADAS (do Nix)
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
    libffi
    openssl
    ncurses
  ];

  shellHook = ''
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH"
    
    echo "🌌 AMBIENTE HÍBRIDO - FUNDAÇÃO ALQUIMISTA"
    echo "🐍 Python: $(python3 --version)"
    echo "📁 Diretório: $(pwd)"
    echo "💡 Use o ambiente virtual para Qiskit"
    
    # Criar/ativar ambiente virtual para Qiskit
    if [ ! -d "/tmp/fundacao_venv" ]; then
        echo "🔧 Criando ambiente virtual para Qiskit..."
        python3 -m venv /tmp/fundacao_venv
        /tmp/fundacao_venv/bin/pip install --upgrade pip
    fi
    
    echo "🎯 COMANDOS DISPONÍVEIS:"
    echo "   source /tmp/fundacao_venv/bin/activate   # Ativar venv para Qiskit"
    echo "   python3 -c 'import numpy; print(\"NumPy OK\")'  # Testar Nix"
    
    # Testar bibliotecas do Nix
    python3 -c "
try:
    import numpy as np
    print(f'✅ NumPy (Nix): {np.__version__}')
    import scipy
    print(f'✅ SciPy (Nix): {scipy.__version__}')
    print('🚀 Bibliotecas científicas PRONTAS no Nix!')
except Exception as e:
    print(f'❌ Erro nas bibliotecas Nix: {e}')
"
  '';
}
