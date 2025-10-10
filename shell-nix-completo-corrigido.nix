{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.virtualenv
    
    # Bibliotecas Python científicas
    python311Packages.numpy
    python311Packages.matplotlib
    python311Packages.scipy
    
    # BIBLIOTECAS C++ CRÍTICAS
    stdenv.cc.cc.lib  # libstdc++.so.6
    zlib
    numactl
    
    # Runtime libraries
    glibc
    gcc-unwrapped
    
    # Ferramentas
    binutils
  ];

  # Variáveis de ambiente para resolver paths de bibliotecas
  LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:${pkgs.glibc}/lib";
  
  # Preload das bibliotecas
  shellHook = ''
    echo "🔮 AMBIENTE QUÂNTICO COMPLETO - Rainha Zennith"
    echo "🐍 Python + Qiskit + Bibliotecas C++"
    
    # Configurar library path
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:${pkgs.glibc}/lib:$LD_LIBRARY_PATH"
    
    # Criar/ativar virtualenv
    if [ ! -d "quantum_venv" ]; then
      echo "🐍 Criando virtualenv..."
      python -m venv quantum_venv
    fi
    
    source quantum_venv/bin/activate
    
    # Verificar se Qiskit precisa ser instalado
    if ! python -c "import qiskit" 2>/dev/null; then
      echo "📦 Instalando Qiskit..."
      pip install --upgrade pip
      pip install qiskit qiskit-aer
    fi
    
    echo "✅ Ambiente completamente configurado!"
    echo "🚀 Teste com: python fundacao_master.py"
  '';
}
