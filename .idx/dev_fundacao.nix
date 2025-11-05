{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.numpy
    python311Packages.scipy
    python311Packages.matplotlib
    python311Packages.pandas
    python311Packages.requests
    python311Packages.psutil
    # python311Packages.coverage   # exemplo de pacote válido
    mailutils
  ];

  shellHook = ''
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo "🌌 Ambiente Nix carregado para a Fundação Alquimista"
    python3 -c "import numpy; print('✅ NumPy disponível:', numpy.__version__)"
  '';
}
