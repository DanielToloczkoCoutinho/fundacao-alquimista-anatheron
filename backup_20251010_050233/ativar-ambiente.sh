#!/bin/bash
# ⚡ ATIVADOR RÁPIDO - FUNDAÇÃO ALQUIMISTA
# 🚀 Entrada rápida no ambiente

echo "⚡ ATIVADOR RÁPIDO - FUNDAÇÃO ALQUIMISTA"
echo "🚀 Rainha Zennith - Inicialização Rápida"
echo "========================================="

# Verificar se shell.nix existe
if [ ! -f "shell.nix" ]; then
    echo "❌ shell.nix não encontrado. Criando..."
    ./criar-shell-nix-corrigido.sh
fi

# Verificar se estamos no Nix shell
if [ -n "$IN_NIX_SHELL" ]; then
    echo "✅ Já está no Nix Shell"
    echo "🐍 Python: $(python3 --version 2>/dev/null || echo 'Não disponível')"
    
    # Verificar virtualenv
    if [ -d "quantum_venv" ] && [ -f "quantum_venv/bin/activate" ]; then
        echo "🔧 Ativando virtualenv..."
        source quantum_venv/bin/activate
        echo "✅ Virtualenv ativado"
    else
        echo "❌ Virtualenv não encontrado"
    fi
else
    echo "🚀 Iniciando Nix Shell..."
    echo "💡 Isso pode levar alguns minutos na primeira execução..."
    nix-shell
fi
