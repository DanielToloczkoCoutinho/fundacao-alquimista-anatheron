#!/bin/bash
echo "💥 SOLUÇÃO NUCLEAR - Recriação completa"
echo "======================================"

# Sair completamente
deactivate 2>/dev/null
exit

# Forçar recriação
rm -rf quantum_venv
rm -f shell.nix

# Criar shell.nix super simples mas funcional
cat > shell.nix << 'EOL'
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    (python311.withPackages (ps: with ps; [
      numpy
      matplotlib
      scipy
      pip
      virtualenv
    ]))
    stdenv.cc.cc.lib
    zlib
  ];

  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH"
    python -m venv quantum_venv --system-site-packages
    source quantum_venv/bin/activate
    pip install qiskit qiskit-aer
    echo "✅ Ambiente nuclear criado!"
  '';
}
EOL

nix-shell
