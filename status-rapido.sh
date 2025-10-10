#!/bin/bash
# 📊 STATUS RÁPIDO - FUNDAÇÃO ALQUIMISTA
# 🎯 Verificação instantânea

echo "📊 STATUS RÁPIDO - FUNDAÇÃO ALQUIMISTA"
echo "🎯 Rainha Zennith - Verificação Instantânea"
echo "=========================================="

# VERIFICAÇÕES RÁPIDAS
echo "🔍 VERIFICAÇÕES:"

# 1. Shell.nix
if [ -f "shell.nix" ]; then
    echo "✅ shell.nix: PRONTO"
else
    echo "❌ shell.nix: FALTANDO"
fi

# 2. Virtualenv
if [ -d "quantum_venv" ]; then
    echo "✅ quantum_venv: EXISTE"
else
    echo "❌ quantum_venv: FALTANDO"
fi

# 3. Python no PATH
if command -v python3 &> /dev/null; then
    echo "✅ Python3: NO PATH"
else
    echo "❌ Python3: NÃO NO PATH"
fi

# 4. Nix Shell
if [ -n "$IN_NIX_SHELL" ]; then
    echo "✅ Nix Shell: ATIVO"
else
    echo "❌ Nix Shell: INATIVO"
fi

echo ""
echo "🚀 COMANDOS DISPONÍVEIS:"
echo "  ./ativar-ambiente.sh    # ⚡ Entrar no ambiente"
echo "  nix-shell               # 🐚 Ambiente Nix completo"
echo "  ./status-rapido.sh      # 📊 Verificar status"
echo ""
echo "💡 DICA: Use './ativar-ambiente.sh' para entrada automática"
