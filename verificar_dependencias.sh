#!/bin/bash
echo "🔍 VERIFICADOR DE DEPENDÊNCIAS - ZENNITH"
echo "========================================"

# Verificar se virtual env existe
if [ ! -d "fundacao_independente" ]; then
    echo "❌ Virtual environment não encontrado."
    echo "💡 Execute: ./instalar_dependencias.sh"
    exit 1
fi

# Verificar se está ativado
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Virtual environment não está ativado."
    echo "💡 Execute: source fundacao_independente/bin/activate"
fi

# Verificar dependências críticas
echo ""
echo "📦 VERIFICANDO DEPENDÊNCIAS CRÍTICAS:"

source fundacao_independente/bin/activate

declare -A deps=(
    ["qiskit"]="qiskit"
    ["numpy"]="numpy" 
    ["scipy"]="scipy"
    ["pandas"]="pandas"
)

for dep in "${!deps[@]}"; do
    if python3 -c "import ${deps[$dep]}" 2>/dev/null; then
        echo "✅ $dep: INSTALADO"
    else
        echo "❌ $dep: AUSENTE"
    fi
done

echo ""
echo "🎯 STATUS: $(python3 -c "import sys; print(f'Python {sys.version}')")"
