#!/bin/bash
echo "🚀 SISTEMA DE INSTALAÇÃO UNIVERSAL DA FUNDAÇÃO"

# 1. Verificar e instalar Python completo
echo "🐍 VERIFICANDO PYTHON:"
python3 --version
pip --version

# Instalar pacotes Python essenciais
pip install numpy pandas matplotlib scipy jupyter qiskit tensorflow torch

# 2. Verificar e instalar Node.js completo
echo "🟢 VERIFICANDO NODE.JS:"
node --version
npm --version

# Instalar dependências globais
npm install -g vercel firebase-tools

# 3. Instalar ferramentas do sistema
echo "🔧 INSTALANDO FERRAMENTAS:"
nix-env -iA nixpkgs.tree nixpkgs.htop nixpkgs.ncdu nixpkgs.fzf nixpkgs.jq

# 4. Verificar tecnologias da Fundação
echo "💫 VERIFICANDO TECNOLOGIAS DA FUNDAÇÃO:"
technologies=("docker" "firebase" "vercel" "node" "python" "graphql" "mongodb" "react" "next" "typescript")
for tech in "${technologies[@]}"; do
    if command -v $tech &> /dev/null; then
        echo "✅ $tech: INSTALADO"
    else
        echo "❌ $tech: AUSENTE"
    fi
done

echo "🎉 VERIFICAÇÃO COMPLETA!"
