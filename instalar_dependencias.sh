#!/bin/bash
echo "�� SISTEMA DE INSTALAÇÃO AUTOMÁTICA - ZENNITH"
echo "=============================================="

# Verificar se Python está disponível
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale Python primeiro."
    exit 1
fi

# Verificar se pip está disponível
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Instale pip primeiro."
    exit 1
fi

echo "✅ Python3 e pip3 encontrados"

# Criar virtual environment
echo ""
echo "🏗️ CRIANDO VIRTUAL ENVIRONMENT..."
python3 -m venv fundacao_independente

# Ativar e instalar dependências
echo ""
echo "📦 INSTALANDO DEPENDÊNCIAS..."
source fundacao_independente/bin/activate

if [ -f "requirements_zennith.txt" ]; then
    echo "📋 Usando requirements_zennith.txt..."
    pip install -r requirements_zennith.txt
else
    echo "📋 Instalando dependências core..."
    pip install qiskit numpy scipy pandas matplotlib requests tqdm
fi

echo ""
echo "✅ INSTALAÇÃO CONCLUÍDA!"
echo "🔧 Para usar: source fundacao_independente/bin/activate"
echo "🎯 Para desenvolvimento: pip install -r requirements_zennith.txt"
