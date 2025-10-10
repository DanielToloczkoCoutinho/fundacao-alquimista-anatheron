#!/bin/bash
echo "🔍 ANÁLISE COMPLETA E SEGURA - fundacao_independente (331MB)"
echo "============================================================"

# 1. ANÁLISE DA ESTRUTURA PRINCIPAL
echo "📁 ESTRUTURA PRINCIPAL DO DIRETÓRIO:"
if [ -d "fundacao_independente" ]; then
    echo "✅ Diretório encontrado: $(du -sh fundacao_independente)"
    echo ""
    echo "🌳 ESTRUTURA DE DIRETÓRIOS:"
    find fundacao_independente -type d | head -20
else
    echo "❌ Diretório não encontrado"
    exit 1
fi

# 2. ANÁLISE DAS BIBLIOTECAS INSTALADAS
echo ""
echo "📦 BIBLIOTECAS PYTHON INSTALADAS:"
if [ -d "fundacao_independente/lib/python3.11/site-packages" ]; then
    echo "📊 Total de pacotes: $(ls -1 fundacao_independente/lib/python3.11/site-packages | wc -l)"
    echo ""
    echo "🎯 PRINCIPAIS BIBLIOTECAS (por tamanho):"
    du -sh fundacao_independente/lib/python3.11/site-packages/* 2>/dev/null | sort -hr | head -15
else
    echo "❌ Diretório de pacotes não encontrado"
fi

# 3. ANÁLISE DOS ARQUIVOS .so (BIBLIOTECAS COMPILADAS)
echo ""
echo "🔧 ARQUIVOS .so (BIBLIOTECAS COMPILADAS - MAIORES):"
find fundacao_independente -name "*.so" -exec du -h {} + 2>/dev/null | sort -hr | head -10

# 4. VERIFICAR SE SÃO DEPENDÊNCIAS ESSENCIAIS
echo ""
echo "🎯 VERIFICAÇÃO DE ESSENCIALIDADE:"
echo "🔍 Verificando quais bibliotecas são realmente usadas..."

# Listar bibliotecas críticas
declare -A bibliotecas_criticas=(
    ["qiskit"]="Computação Quântica"
    ["numpy"]="Computação Científica"
    ["scipy"]="Algoritmos Científicos"
    ["pandas"]="Análise de Dados"
    ["matplotlib"]="Visualização"
    ["requests"]="Requisições HTTP"
)

for lib in "${!bibliotecas_criticas[@]}"; do
    if [ -d "fundacao_independente/lib/python3.11/site-packages/$lib" ]; then
        tamanho=$(du -sh "fundacao_independente/lib/python3.11/site-packages/$lib" 2>/dev/null | cut -f1)
        echo "✅ $lib: $tamanho - ${bibliotecas_criticas[$lib]}"
    else
        echo "❌ $lib: AUSENTE - ${bibliotecas_criticas[$lib]}"
    fi
done

# 5. ANÁLISE DE DUPLICAÇÃO
echo ""
echo "🔄 VERIFICANDO DUPLICAÇÃO:"
echo "🔍 Procurando arquivos idênticos..."
find fundacao_independente -type f -exec md5sum {} + 2>/dev/null | sort | uniq -w32 -d | head -5

# 6. ANÁLISE DE ARQUIVOS TEMPORÁRIOS/CACHE
echo ""
echo "🗑️  ARQUIVOS DE CACHE/TEMPORÁRIOS:"
find fundacao_independente -name "__pycache__" -type d | head -5
find fundacao_independente -name "*.pyc" | head -5
