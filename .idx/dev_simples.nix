{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.numpy
    python311Packages.scipy
    python311Packages.matplotlib
    python311Packages.requests
    python311Packages.psutil
    gcc
    zlib
    busybox
  ];

  shellHook = ''
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo "🌌 AMBIENTE NIX SIMPLIFICADO - FUNDAÇÃO ALQUIMISTA"
    echo "🐍 Python: $(python3 --version)"
    echo "📁 Diretório: $(pwd)"
  '';
}
