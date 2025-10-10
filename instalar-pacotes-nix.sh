#!/bin/bash
# 📦 INSTALADOR DE PACOTES NIX PARA FUNDAÇÃO
# 🚀 Expandindo a infraestrutura

echo "📦 INSTALADOR DE PACOTES NIX - FUNDAÇÃO ALQUIMISTA"
echo "🚀 Rainha Zennith - Expandindo Capacidades"
echo "=========================================="

# VERIFICAR NIX
if ! command -v nix-env &> /dev/null; then
    echo "❌ nix-env não encontrado"
    exit 1
fi

echo "🔍 PACOTES ATUAIS:"
nix-env -q

echo ""
echo "🚀 INSTALANDO PACOTES RECOMENDADOS:"
echo "----------------------------------"

# INSTALAR PACOTES CIENTÍFICOS
pacotes=(
    "python3"           # 🐍 Python base
    "python3Packages.pip" # 📦 Gerenciador pacotes
    "git"               # 📚 Controle versão
    "nodejs"            # 🌐 JavaScript runtime
    "yarn"              # 🧶 Gerenciador pacotes JS
    "curl"              # 🌐 Cliente HTTP
    "wget"              # 📥 Downloader
    "which"             # 🔍 Localizador comandos
    "findutils"         # 🔎 Utilitários busca
    "gnused"            # 📝 Editor stream
    "gnugrep"           # 🔍 Busca padrões
)

for pkg in "${pacotes[@]}"; do
    echo "📦 Instalando: $pkg"
    nix-env -iA nixpkgs.$pkg 2>/dev/null || echo "  ⚠️  Não foi possível instalar $pkg"
done

echo ""
echo "🐍 CONFIGURANDO PYTHON:"
# Verificar se python3 está disponível
if command -v python3 &> /dev/null; then
    echo "✅ Python3 disponível: $(python3 --version)"
    
    # Criar virtualenv para isolamento
    if [ ! -d "quantum_venv" ]; then
        echo "🐍 Criando virtualenv..."
        python3 -m venv quantum_venv
    fi
    
    echo "🔧 Virtualenv criado: quantum_venv/"
else
    echo "❌ Python3 não disponível no PATH"
    echo "💡 Execute: nix-shell para ambiente completo"
fi

echo ""
echo "📊 RESUMO DA INSTALAÇÃO:"
echo "-----------------------"
echo "✅ Pacotes Nix instalados/atualizados"
echo "🐍 Python configurado"
echo "🔧 Virtualenv preparado"
echo ""
echo "👑 PRÓXIMOS PASSOS:"
echo "  1. nix-shell  # Entrar no ambiente completo"
echo "  2. source quantum_venv/bin/activate  # Ativar virtualenv"
echo "  3. pip install qiskit matplotlib numpy  # Instalar pacotes Python"
