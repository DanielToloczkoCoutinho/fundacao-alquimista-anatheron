#!/bin/bash
echo "🗺️ MAPEANDO TODOS OS MÓDULOS DA FUNDAÇÃO"
echo "========================================"

# 1. Módulos Python
echo "🐍 MÓDULOS PYTHON:"
find /home/user -name "*.py" -exec grep -l "class.*Modulo\|def.*M[0-9]" {} \; | head -30

# 2. Laboratórios Especializados
echo "🔬 LABORATÓRIOS:"
find /home/user -type d -name "*lab*" -o -name "*Lab*" | head -20

# 3. Sistemas de Módulos
echo "⚙️ SISTEMAS DE MÓDULOS:"
find /home/user -name "*.json" -o -name "*.yaml" -o -name "*.yml" | xargs grep -l "modul\|Modul" 2>/dev/null | head -10

# 4. Verificar se há um arquivo de configuração de módulos
echo "📋 CONFIGURAÇÃO DE MÓDULOS:"
find /home/user -name "*modul*" -type f | head -10

echo "========================================"
echo "📊 ESTATÍSTICAS:"
echo "Arquivos Python: $(find /home/user -name "*.py" | wc -l)"
echo "Diretórios com 'mod': $(find /home/user -type d -name "*mod*" | wc -l)"
echo "Arquivos com 'M[0-9]': $(find /home/user -name "*" -type f | xargs grep -l "M[0-9]" 2>/dev/null | wc -l)"
