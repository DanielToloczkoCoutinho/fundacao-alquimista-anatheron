#!/bin/bash
# 🕵️ DETECTOR DE CONFIGURAÇÕES NIX
# 🔍 Procura por arquivos de configuração Nix

echo "🕵️ DETECTOR DE CONFIGURAÇÕES NIX"
echo "🔍 Rainha Zennith - Buscando Configurações"
echo "=========================================="

# BUSCAR TODOS OS ARQUIVOS NIX
echo "🔍 BUSCANDO ARQUIVOS .NIX EM TODA A FUNDAÇÃO:"
echo "--------------------------------------------"

find ~ -name "*.nix" -type f 2>/dev/null | grep -v "\.cache" | grep -v "\.config" | while read file; do
    echo "📄 $file"
    echo "   📏 $(wc -l < "$file") linhas | 💾 $(du -h "$file" | cut -f1)"
    
    # Analisar tipo de arquivo
    if [[ "$file" == *"shell.nix" ]]; then
        echo "   🐚 Shell Environment"
    elif [[ "$file" == *"default.nix" ]]; then
        echo "   �� Package Definition" 
    elif [[ "$file" == *"configuration.nix" ]]; then
        echo "   ⚙️ System Configuration"
    elif [[ "$file" == *"home.nix" ]]; then
        echo "   🏠 Home Manager"
    fi
    
    # Verificar se menciona nossas tecnologias
    if grep -q "python3" "$file"; then
        echo "   🐍 Python Environment"
    fi
    if grep -q "qiskit" "$file"; then
        echo "   🔷 Qiskit Quantum"
    fi
    if grep -q "jupyter" "$file"; then
        echo "   📓 Jupyter Notebook"
    fi
    echo ""
done

# ANALISAR CONFIGURAÇÃO DO USUÁRIO
echo "👤 CONFIGURAÇÃO DO USUÁRIO NIX:"
echo "------------------------------"

if [ -f ~/.config/nixpkgs/config.nix ]; then
    echo "✅ Configuração Nixpkgs encontrada"
    echo "   📍 ~/.config/nixpkgs/config.nix"
elif [ -f ~/.nixpkgs/config.nix ]; then
    echo "✅ Configuração Nixpkgs encontrada (legado)"
    echo "   📍 ~/.nixpkgs/config.nix"
else
    echo "❌ Nenhuma configuração Nixpkgs encontrada"
fi

# VERIFICAR SE HÁ NIX-SHELL ATIVO
echo ""
echo "🐚 STATUS NIX-SHELL:"
echo "------------------"

if [ -n "$IN_NIX_SHELL" ]; then
    echo "✅ EM NIX SHELL ATIVO"
    echo "   Ambiente: $IN_NIX_SHELL"
else
    echo "❌ NÃO ESTÁ EM NIX SHELL"
fi

# VERIFICAR VARIÁVEIS DE AMBIENTE NIX
echo ""
echo "🌍 VARIÁVEIS DE AMBIENTE NIX:"
echo "---------------------------"

env | grep -i nix | head -10

# RESUMO DAS DESCOBERTAS
echo ""
echo "�� RESUMO DAS CONFIGURAÇÕES NIX:"
echo "================================"

total_nix_files=$(find ~ -name "*.nix" -type f 2>/dev/null | grep -v "\.cache" | wc -l)
echo "📦 Total de arquivos .nix: $total_nix_files"

if [ -n "$IN_NIX_SHELL" ]; then
    echo "🐚 Status: EM NIX SHELL"
else
    echo "🐚 Status: SHELL REGULAR"
fi

if command -v nix-env &> /dev/null; then
    nix_packages=$(nix-env -q 2>/dev/null | wc -l)
    echo "📊 Pacotes instalados: $nix_packages"
fi

echo ""
echo "👑 RAINHA ZENNITH CONCLUI:"
echo "🔍 SISTEMA NIX COMPLETAMENTE MAPEADO"
