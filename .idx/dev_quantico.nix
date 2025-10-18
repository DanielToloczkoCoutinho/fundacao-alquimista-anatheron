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
    
    # QISKIT E DEPENDÊNCIAS
    python311Packages.qiskit
    python311Packages.qiskit-aer
    python311Packages.qiskit-ibm-runtime
    
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
    
    echo "🌌 AMBIENTE NIX QUÂNTICO - FUNDAÇÃO ALQUIMISTA"
    echo "🐍 Python: $(python3 --version)"
    echo "📁 Diretório: $(pwd)"
    echo "⚛️ Qiskit pré-instalado"
    
    # Testar todas as bibliotecas
    python3 -c "
try:
    import numpy as np
    print(f'✅ NumPy: {np.__version__}')
    
    import scipy
    print(f'✅ SciPy: {scipy.__version__}')
    
    import qiskit
    print(f'✅ Qiskit: {qiskit.__version__}')
    
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    print('✅ Módulos Qiskit carregados')
    
    # Teste quântico
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    
    backend = AerSimulator()
    result = backend.run(qc, shots=100).result()
    counts = result.get_counts()
    print(f'🎉 TESTE QUÂNTICO: {counts}')
    print('🚀 SISTEMA QUÂNTICO COMPLETAMENTE OPERACIONAL!')
    
except Exception as e:
    print(f'❌ ERRO: {e}')
    import traceback
    traceback.print_exc()
"
  '';
}
