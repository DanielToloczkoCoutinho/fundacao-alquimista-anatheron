#!/bin/bash
# ⚡ ATIVADOR CORRIGIDO - FUNDAÇÃO ALQUIMISTA
# 🚀 Usa NIXPKGS_ALLOW_BROKEN para contornar problemas

echo "⚡ ATIVADOR CORRIGIDO - FUNDAÇÃO ALQUIMISTA"
echo "🚀 Rainha Zennith - Solução com Allow Broken"
echo "============================================"

# Verificar se shell.nix existe
if [ ! -f "shell.nix" ]; then
    echo "❌ shell.nix não encontrado. Criando..."
    ./criar-shell-nix-corrigido.sh
fi

echo "🚀 Iniciando Nix Shell com allow broken..."
echo "💡 Permitindo pacotes quebrados temporariamente..."

# Método 1: Usar variável de ambiente
export NIXPKGS_ALLOW_BROKEN=1
nix-shell

# Se ainda der erro, tentar método alternativo
if [ $? -ne 0 ]; then
    echo "⚠️  Método 1 falhou. Tentando método alternativo..."
    nix-shell --option allow-broken true
fi
