{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    nodejs_20
    python3
    git
    # Vercel será instalado via npm global
  ];
  
  shellHook = ''
    export PATH=$PATH:$HOME/.npm-global/bin
    if ! command -v vercel &> /dev/null; then
      echo "📦 Instalando Vercel CLI..."
      npm install -g vercel@latest
    fi
    echo "🌌 Ambiente Nix da Fundação Alquimista ativado!"
    echo "📍 Node: $(node --version)"
    echo "📍 Python: $(python3 --version)" 
    echo "📍 NPM: $(npm --version)"
    echo "📍 Vercel: $(vercel --version 2>/dev/null || echo 'Não instalado')"
  '';
}
