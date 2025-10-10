#!/bin/bash
# 🐚 SHELL.NIX CORRIGIDO - FUNDAÇÃO ALQUIMISTA
# 🚀 Ambiente sem pacotes quebrados

echo "🐚 CRIANDO SHELL.NIX CORRIGIDO"
echo "🚀 Rainha Zennith - Solução Definitiva"
echo "========================================"

# CRIAR SHELL.NIX FUNCIONAL E SIMPLIFICADO
cat > shell.nix << 'NIXEOF'
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "fundacao-alquimista";
  
  buildInputs = with pkgs; [
    # 🐍 Python básico (sem pacotes quebrados)
    python3
    python3Packages.pip
    python3Packages.virtualenv
    
    # 📊 Ciência de Dados (apenas pacotes estáveis)
    python3Packages.numpy
    python3Packages.matplotlib
    
    # 🛠️ Ferramentas essenciais
    git
    nodejs
    curl
    wget
    
    # 🔧 Utilitários do sistema
    which
    findutils
  ];
  
  shellHook = ''
    echo "🔮 AMBIENTE FUNDAÇÃO ALQUIMISTA - NIX SHELL"
    echo "🐍 Python: $(python3 --version)"
    echo "📊 Numpy/Matplotlib: Disponível"
    echo "💡 Qiskit: Será instalado via pip"
    echo ""
    echo "👑 Rainha Zennith - Ambiente Ativado!"
    
    # Criar virtualenv se não existir
    if [ ! -d "quantum_venv" ]; then
      echo "🐍 Criando virtualenv..."
      python3 -m venv quantum_venv
    fi
    
    # Ativar virtualenv
    source quantum_venv/bin/activate
    
    # Instalar Qiskit e dependências via pip (evita pacotes quebrados do Nix)
    echo "📦 Instalando Qiskit via pip..."
    pip install --upgrade pip
    pip install qiskit qiskit-aer
    
    echo "✅ Ambiente pronto! Use: python fundacao_master.py"
  '';
}
NIXEOF

echo "✅ shell.nix corrigido criado com sucesso!"
echo ""
echo "🎯 ESTRATÉGIA:"
echo "  ✅ Python, Numpy, Matplotlib: Via Nix"
echo "  ✅ Qiskit: Via pip (evita pacotes quebrados)"
echo "  ✅ Virtualenv: Isolamento garantido"

echo ""
echo "🚀 PARA USAR:"
echo "  nix-shell  # Entrar no ambiente"
echo "  python fundacao_master.py  # Testar experimentos"
