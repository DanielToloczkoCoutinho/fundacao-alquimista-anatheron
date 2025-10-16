#!/bin/bash
echo "🏰 ANÁLISE ARQUITETURAL DA FUNDAÇÃO ALQUIMISTA"
echo "=============================================="

# Contar laboratórios
echo "🔬 LABORATÓRIOS:"
find /home/user -name "*laborator*" -type d | wc -l

# Contar módulos  
echo "📦 MÓDULOS:"
find /home/user -name "*modul*" -type d | wc -l

# Contar equações
echo "🧮 EQUAÇÕES:"
find /home/user -name "*.py" -o -name "*.md" | xargs grep -l "equação\|equation" 2>/dev/null | wc -l

# Mapear estrutura principal
echo "🌌 ESTRUTURA PRINCIPAL:"
tree /home/user -L 3 -d 2>/dev/null | head -30
