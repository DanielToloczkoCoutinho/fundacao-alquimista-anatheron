{ pkgs ? import <nixpkgs> { config = { allowBroken = true; }; } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.numpy
    pkgs.python311Packages.scipy
    pkgs.python311Packages.matplotlib
    pkgs.python311Packages.pandas
    pkgs.python311Packages.requests
    pkgs.python311Packages.psutil
    pkgs.python311Packages.qiskit
    pkgs.python311Packages.aiohttp
    pkgs.python311Packages.python-dateutil
    pkgs.libstdcxx5  # Para libstdc++.so.6
    pkgs.gcc
    pkgs.zlib
    pkgs.unixtools.ping
  ];

  shellHook = ''
    echo "🌌 AMBIENTE NIX - FUNDAÇÃO ALQUIMISTA"
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export LD_LIBRARY_PATH=${pkgs.libstdcxx5}/lib:${pkgs.gcc}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH
    export PYTHONPATH="$PWD:$PYTHONPATH"
    echo "🐍 Python: $(python3 --version)"
    echo "📁 Diretório: $(pwd)"
  '';
}
