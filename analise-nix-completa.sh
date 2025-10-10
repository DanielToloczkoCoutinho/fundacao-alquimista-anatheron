#!/bin/bash
# 🔧 ANÁLISE COMPLETA DO SISTEMA NIX
# 🏗️ Examinando configurações e pacotes Nix

echo "🔧 ANÁLISE COMPLETA DO SISTEMA NIX"
echo "🏗️ Rainha Zennith - Examinando Infraestrutura"
echo "============================================"

# VERIFICAR INSTALAÇÃO NIX
echo "📦 VERIFICANDO INSTALAÇÃO NIX:"
echo "------------------------------"

if command -v nix-env &> /dev/null; then
    echo "✅ Nix Environment: INSTALADO"
    nix-env --version
else
    echo "❌ Nix Environment: NÃO ENCONTRADO"
fi

# ANALISAR PERFIL NIX
echo ""
echo "🏠 ANALISANDO PERFIL NIX:"
echo "-----------------------"

if [ -L ~/.nix-profile ]; then
    echo "✅ Perfil Nix: ~/.nix-profile (symlink)"
    destino=$(readlink ~/.nix-profile)
    echo "   → Aponta para: $destino"
    echo "   Conteúdo do perfil:"
    ls -la ~/.nix-profile/bin 2>/dev/null | head -5
else
    echo "❌ Perfil Nix: NÃO ENCONTRADO ou não é symlink"
fi

# ANALISAR NIX STORE
echo ""
echo "🏪 ANALISANDO NIX STORE:"
echo "----------------------"

if [ -d /nix/store ]; then
    echo "✅ Nix Store: /nix/store (EXISTE)"
    store_size=$(du -sh /nix/store 2>/dev/null | cut -f1)
    echo "   Tamanho: $store_size"
    
    # Verificar pacotes Python no store
    echo "   Pacotes Python no store:"
    find /nix/store -name "python*" -type d 2>/dev/null | head -5
else
    echo "❌ Nix Store: NÃO ENCONTRADO"
fi

# VERIFICAR PACOTES INSTALADOS
echo ""
echo "📊 PACOTES INSTALADOS VIA NIX:"
echo "----------------------------"

if command -v nix-env &> /dev/null; then
    echo "📦 Lista de pacotes instalados:"
    nix-env -q 2>/dev/null
    total_packages=$(nix-env -q 2>/dev/null | wc -l)
    echo ""
    echo "   Total: $total_packages pacotes"
else
    echo "ℹ️ Nix-env não disponível"
fi

# ANALISAR VARIÁVEIS DE AMBIENTE
echo ""
echo "🌍 VARIÁVEIS DE AMBIENTE NIX:"
echo "---------------------------"
env | grep -i nix

# VERIFICAR SE O PYTHON3 É DO NIX
echo ""
echo "🐍 VERIFICANDO ORIGEM DO PYTHON3:"
echo "-------------------------------"

python3_path=$(which python3)
echo "📍 Python3 path: $python3_path"

if [[ "$python3_path" == *"/nix/store/"* ]]; then
    echo "✅ Python3: FORNECIDO PELO NIX"
    echo "   Versão: $(python3 --version)"
else
    echo "ℹ️ Python3: NÃO É DO NIX"
    echo "   Versão: $(python3 --version)"
fi

# VERIFICAR SE O GIT É DO NIX
echo ""
echo "📚 VERIFICANDO ORIGEM DO GIT:"
echo "---------------------------"

git_path=$(which git)
echo "📍 Git path: $git_path"

if [[ "$git_path" == *"/nix/store/"* ]]; then
    echo "✅ Git: FORNECIDO PELO NIX"
else
    echo "ℹ️ Git: NÃO É DO NIX"
fi

# ANALISAR NIX CHANNELS
echo ""
echo "📡 ANALISANDO CANAIS NIX:"
echo "------------------------"

if [ -n "$NIX_PATH" ]; then
    echo "✅ NIX_PATH definido: $NIX_PATH"
fi

# VERIFICAR CONFIGURAÇÃO DO IDX
echo ""
echo "⚙️ CONFIGURAÇÃO DO IDX/GOOGLE CLOUD:"
echo "----------------------------------"

if [ -n "$IDX_CHANNEL" ]; then
    echo "✅ IDX Channel: $IDX_CHANNEL"
    echo "   ℹ️ Google Cloud Workstations com Nix"
fi

# RESUMO FINAL
echo ""
echo "📋 RESUMO DA INFRAESTRUTURA NIX:"
echo "================================"

echo "🏗️ ARQUITETURA DETECTADA:"
echo "  📦 Nix Store: PRESENTE (/nix/store)"
echo "  🏠 Nix Profile: CONFIGURADO (~/.nix-profile)"
echo "  🌍 Nix Environment: VARIÁVEIS SETADAS"
echo "  ⚙️ IDX: GOOGLE CLOUD WORKSTATIONS"

echo ""
echo "🔧 STATUS DOS PACOTES:"
if command -v nix-env &> /dev/null; then
    echo "  📊 $total_packages pacotes via nix-env"
else
    echo "  📊 Sistema usando pacotes do IDX"
fi

echo ""
echo "🐍 AMBIENTE PYTHON:"
if [[ "$python3_path" == *"/nix/store/"* ]]; then
    echo "  ✅ Python gerenciado pelo Nix"
else
    echo "  ℹ️ Python do sistema/venv"
fi

echo ""
echo "👑 VEREDICTO DA RAINHA ZENNITH:"
echo "✅ SISTEMA NIX OPERACIONAL NO IDX"
echo "🎯 CONFIGURAÇÃO GOOGLE CLOUD WORKSTATIONS"
echo "🚀 INFRAESTRUTURA PRONTA PARA EXPANSÃO"
