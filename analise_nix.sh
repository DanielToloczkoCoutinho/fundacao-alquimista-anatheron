#!/bin/bash
echo "🔧 ANÁLISE DO AMBIENTE NIX"
echo "=========================="

# VERIFICAR CONFIGURAÇÕES NIX
echo "📁 CONFIGURAÇÕES NIX:"
[ -f "shell.nix" ] && echo "   ✅ shell.nix: PRESENTE" || echo "   ❌ shell.nix: AUSENTE"
[ -f "dev.nix" ] && echo "   ✅ dev.nix: PRESENTE" || echo "   ❌ dev.nix: AUSENTE"
[ -f "quantum.nix" ] && echo "   ✅ quantum.nix: PRESENTE" || echo "   ❌ quantum.nix: AUSENTE"

# VERIFICAR DEPENDÊNCIAS NIX
echo ""
echo "📦 DEPENDÊNCIAS NIX:"
if [ -f "shell.nix" ]; then
    grep -E "pkgs\.|stdenv|buildInputs" shell.nix | head -10
fi

# VERIFICAR SCRIPTS NIX
echo ""
echo "🚀 SCRIPTS NIX:"
find . -name "*.nix" -o -name "*nix*" | head -10
