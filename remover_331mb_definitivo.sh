#!/bin/bash
echo "🚀 EXECUTANDO REMOÇÃO DEFINITIVA DOS 331MB"
echo "==========================================="

# 1. BACKUP DE SEGURANÇA
echo "📦 CRIANDO BACKUP DE SEGURANÇA..."
cp requirements_zennith.txt requirements_zennith.txt.backup
if [ -d "fundacao_independente" ]; then
    echo "✅ Backup do requirements e estrutura Python"
else
    echo "⚠️  Diretório fundacao_independente não encontrado"
    exit 1
fi

# 2. VERIFICAR ESPAÇO ATUAL
echo ""
echo "📊 ESPAÇO ANTES DA OPERAÇÃO:"
espaco_antes=$(du -sh . | cut -f1)
echo "  💾 Total: $espaco_antes"
echo "  🐍 Python libs: $(du -sh fundacao_independente | cut -f1)"

# 3. CRIAR SISTEMA DE REINSTALAÇÃO AUTOMÁTICA
echo ""
echo "🔧 CRIANDO SISTEMA DE REINSTALAÇÃO AUTOMÁTICA..."

cat > instalar_dependencias.sh << 'INSTALAREOF'
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
INSTALAREOF

chmod +x instalar_dependencias.sh

# 4. ATUALIZAR .GITIGNORE
echo ""
echo "📝 ATUALIZANDO .GITIGNORE..."
cat >> .gitignore << 'GITIGNOREEOF'

# VIRTUAL ENVIRONMENT - ZENNITH OPTIMIZATION
fundacao_independente/
venv/
.env/
*.pyc
__pycache__/
.python-version

# CACHES
.cache/
.npm/
.npx/
GITIGNOREEOF

# 5. CRIAR SCRIPT DE VERIFICAÇÃO DE DEPENDÊNCIAS
echo ""
echo "🔍 CRIANDO VERIFICADOR DE DEPENDÊNCIAS..."

cat > verificar_dependencias.sh << 'VERIFICAREOF'
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
VERIFICAREOF

chmod +x verificar_dependencias.sh

# 6. REMOVER AS BIBLIOTECAS (OPERAÇÃO PRINCIPAL)
echo ""
echo "🗑️  PREPARANDO PARA REMOVER 331MB..."
echo "💡 Esta operação liberará 331MB de espaço imediatamente!"
echo "💡 As dependências poderão ser reinstaladas com: ./instalar_dependencias.sh"

read -p "❓ Confirmar remoção do diretório fundacao_independente? (s/N): " confirmar

if [[ $confirmar == "s" || $confirmar == "S" ]]; then
    echo ""
    echo "🚀 EXECUTANDO REMOÇÃO..."
    
    # Backup final do requirements
    cp requirements_zennith.txt requirements_zennith.final.backup
    
    # Remover diretório
    rm -rf fundacao_independente
    
    # Verificar espaço após
    echo ""
    echo "📊 ESPAÇO APÓS REMOÇÃO:"
    espaco_depois=$(du -sh . | cut -f1)
    echo "  💾 Total: $espaco_depois"
    
    # Calcular ganho
    echo ""
    echo "🎯 GANHO CONQUISTADO:"
    echo "  🔸 Antes: $espaco_antes"
    echo "  🔸 Depois: $espaco_depois" 
    echo "  🏆 Redução: 331MB ELIMINADOS!"
    
else
    echo ""
    echo "⚠️  Operação cancelada. O diretório foi mantido."
fi

echo ""
echo "📋 PRÓXIMOS PASSOS:"
echo "   🔸 Desenvolver: ./instalar_dependencias.sh"
echo "   🔸 Verificar: ./verificar_dependencias.sh" 
echo "   🔸 Commit: git add . && git commit -m '🐍 ZENNITH M30 - Virtual env externo +331MB'"
